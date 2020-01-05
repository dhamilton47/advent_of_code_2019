# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 01:17:40 2020

@author: Dan J Hamilton
"""


import math
import numpy as np

from computer import Computer
import aoc


# %%
def pointing(theta, turn):
    """ Determine the direction the robot is pointing after it turns """

    if turn:
        theta -= math.pi / 2  # turn right
    else:
        theta += math.pi / 2  # turn left

    return theta


def next_coordinate(pt1, theta, turn, move):
    """ Determine the (x, y) for the location after the robot moves """

    next_theta = pointing(theta, turn) % (2 * math.pi)
    x, y = pt1
    # print(x, y)

    if next_theta == math.pi / 2:
        # x += 0
        y += move

    elif next_theta == math.pi:
        x += -move
        # y += 0

    elif next_theta == (3 * math.pi / 2):
        # x += 0
        y += -move

    elif next_theta == 0:
        x += move
        # y += 0

    else:
        raise ValueError('That angle is not possible for this scenario.')

    return next_theta, (x, y), x, y


def print_direction(theta):
    """ Print the direction pointing in human readable (EN) format """

    if theta == math.pi / 2:
        return 'UP'

    elif theta == math.pi:
        return 'LEFT'

    elif theta == (3 * math.pi / 2):
        return 'DOWN'

    elif theta == 0:
        return 'RIGHT'

    else:
        raise ValueError('That angle is not possible for this scenario.')


def run():
    """ Run the IntCode program """

    # Starting info for position on grid to be painted
    coordinates = {(0, 0): {'color': 0, 'x': 0, 'y': 0}}
    theta = math.pi / 2
    move = 1

    current_position = (0, 0)
    current_color = coordinates[current_position]['color'] | 0

    coordinates[current_position]['color'] = current_color

    # Execute intcode program
    opcode = 0
    x_s = []
    y_s = []

    while opcode != 99:
        opcode = robot.process_run()

        # Coordinate from
        # Input = color currently standing on
        if current_position in coordinates.keys():
            current_color = coordinates[current_position]['color']
        else:
            current_color = 0

        robot.emulated_input = current_color

        # color currently standing on painted

        next_color = robot.output_value
        coordinates[current_position]['color'] = next_color

        # Coordinate to

        # determine next position
        turn = robot.output_value
        # turn = output2
        theta, next_position, row, column = \
            next_coordinate(current_position, theta, turn, move)
        # print(f"from = {current_position}, {print_direction(theta)},"
        #       f" to = {next_position}")

        # add next position to known coordinates
        if next_position not in coordinates.keys():
            coordinates[next_position] = \
                {'color': next_color, 'x': row, 'y': column}
            x_s.append(row)
            y_s.append(column)

        current_position = next_position

    return coordinates, x_s, y_s


def graph(coordinates, x_s, y_s):
    """ Create the graph of the path results """
    max_x = max(x_s)
    min_x = min(x_s)

    max_y = max(y_s)
    min_y = min(y_s)

    range_x = max_x - min_x + 1
    range_y = max_y - min_y + 1

    # Blank grid in the size indicated by the part 1 output
    layout = np.array(['.'] * (range_x * range_y)).reshape((range_x, range_y))

    # Map the coordinates output
    for item in list(coordinates.items()):
        item = list(item)[1]
        row = item['x'] + abs(min_x)
        column = item['y'] + abs(min_y)
        color = item['color']
        # print(row, column, color)
        layout[row, column] = '.' if color == 0 else '#'

    temp = []
    for row in range(range_x):
        # print([''.join(layout[:, j]) for j in range(range_y)])
        temp.append([''.join(layout[:, j]) for j in range(range_y)])

    # display = [''.join([
    #     '\n'.join(layout[i, j]) for j in range(range_y)]
    #     ) for i in range(range_x)]

    return temp


def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.boot()
    computer.program_load()
    computer.flash_memory()
    computer.halt_condition = True
    computer.process_run()

    return computer


def test(library, program):
    """ main() program """

    intcode(library, program)


# %% Development Environment

# robot = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Registration Identifier')

# # Starting info
# coordinates = {(0, 0): {'color': 0, 'x': 0, 'y': 0}}
# theta = math.pi / 2
# move = 1

# current_position = (0, 0)
# current_color = coordinates[current_position]['color'] | 0
# coordinates[current_position]['color'] = current_color

# opcode = 0
# x_s = []
# y_s = []

# while opcode != 99:
#     opcode = robot.process_run()

#     if current_position in coordinates.keys():
#         current_color = coordinates[current_position]['color']
#     else:
#         current_color = 0

#     robot.emulated_input = current_color

#     next_color = robot.output_value
#     coordinates[current_position]['color'] = next_color

#     turn = robot.output_value
#     theta, next_position, row, column = \
#         next_coordinate(current_position, theta, turn, move)
#     print(f"from = {current_position}, {print_direction(theta)},"
#           f" to = {next_position}")
#     # print(coordinates)

#     if next_position not in coordinates.keys():
#         coordinates[next_position] = \
#             {'color': next_color, 'x': row, 'y': column}
#         x_s.append(row)
#         y_s.append(column)

#     current_position = next_position

robot = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Registration Identifier')
coordinates, x_s, y_s = run()

display = graph(coordinates, x_s, y_s)
# print(display)

file1 = open("../data/day11_output.txt", "w")
for item in display:
    file1.write(item[0])

file1.close() #to change file access modes

# %% Production Environment (LOL)

# if __name__ == "__main__":
#     test(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Registration Identifier')

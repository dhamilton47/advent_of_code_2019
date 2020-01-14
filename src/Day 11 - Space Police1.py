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

    theta += (math.pi / 2) * (1 if turn else -1)

    return theta


def next_coordinate(pt1, theta, turn, move):
    """ Determine the (x, y) for the location after the robot moves """

    next_theta = pointing(theta, turn) % (2 * math.pi)
    x, y = pt1
    # print(x, y)

    if next_theta == math.pi / 2:
        y += move

    elif next_theta == math.pi:
        x += -move

    elif next_theta == (3 * math.pi / 2):
        y += -move

    elif next_theta == 0:
        x += move

    else:
        raise ValueError('That angle is not possible for this scenario.')

    return next_theta, (x, y), x, y


def panel_color(coordinates, position):
    """ Return the color of the panel """

    if position in coordinates.keys():
        color = coordinates[position]['color']
    else:
        color = 0

    return color


def print_direction(theta):
    """ Print the direction pointing in human readable (EN) format """

    if theta == math.pi / 2:
        return 'UP'

    if theta == math.pi:
        return 'LEFT'

    if theta == (3 * math.pi / 2):
        return 'DOWN'

    if theta == 0:
        return 'RIGHT'

    raise ValueError('That angle is not possible for this scenario.')


def run(robot):
    """ Run the IntCode program """

    print_flag = False

    # Starting info for position on grid to be painted
    coordinates = {(0, 0): {'color': 0, 'x': 0, 'y': 0}}
    theta = math.pi / 2
    move = 1

    current_position = (0, 0)
    current_color = coordinates[current_position]['color'] | 0

    coordinates[current_position]['color'] = current_color

    # Execute intcode program
    opcode = 0
    x_s = [0]
    y_s = [0]

    robot.emulated_input = [0]

    while opcode != 99:
    # for i in range(4000):

        opcode = robot.process_run()

        robot.emulated_input = [panel_color(coordinates, current_position)]

        if print_flag:
            print(f"\nColor of panel {current_position} prior to move is "
                  f"{['black', 'white'][robot.emulated_input]}")

        color_to_paint_prior_to_moving = robot.output_value


        direction_to_turn = robot.output_value
        coordinates[current_position]['color'] = color_to_paint_prior_to_moving

        if print_flag:
            print(f"Robot outputs are: "
                  f"({color_to_paint_prior_to_moving}, "
                  f"{direction_to_turn})")

        theta, next_position, x, y = \
            next_coordinate(current_position, theta, direction_to_turn, move)

        # If next position is not in coordinates, add next position
        if next_position not in coordinates.keys():
            coordinates[next_position] = \
                {'color': panel_color(coordinates, next_position),
                 'x': x,
                 'y': y}

            x_s.append(x)
            y_s.append(y)

        # Otherwise just update the color
        else:
            coordinates[next_position]['color'] = \
                panel_color(coordinates, next_position)

        if print_flag:
            print(f"  from {current_position}, {print_direction(theta)},"
                  f" to {next_position}\n"
                  f"  color of panel {current_position} after move is "
                  f"{['black', 'white'][color_to_paint_prior_to_moving]}\n"
                  f"  number of unique steps is {len(coordinates)}\n"
                  f"We are now on panel {next_position}")

        current_position = next_position

    args = dimensions(x_s, y_s)

    display = graph(coordinates, *args)
    output_to_file(display)
    steps = len(coordinates)

    # del coordinates

    return steps, coordinates, display


def dimensions(x_s, y_s):
    """ Find the dimensions of the graph we need to create """

    max_x = max(x_s)
    min_x = min(x_s)

    max_y = max(y_s)
    min_y = min(y_s)

    range_x = max_x - min_x + 1
    range_y = max_y - min_y + 1
    print(f"\nRange of the x-axis = {range_x}\n"
          f"  Min x = {min_x}\n"
          f"  Max x = {max_x}\n\n"
          f"Range of the y-axis = {range_y}\n"
          f"  Min y = {min_y}\n"
          f"  Max y = {max_y}")

    return (max_x, max_y, range_x, range_y)


def graph(coordinates, *args):
    """ Create the graph of the path results """

    max_x, max_y, range_x, range_y = args
    print(f"range x = {range_x}, range y = {range_y}")

    # Blank grid in the size indicated by the part 1 output
    layout = np.array(['.'] * (range_x * range_y)).reshape((range_y, range_x))
    print(f"The shape of layout is {layout.shape}")

    # Map the coordinates output
    for item in list(coordinates.items()):
        coord = list(item)[0]
        item = list(item)[1]
        # print(f"Coordinate: {coord}, x = {item['x']}, "
        #       f"y = {item['y']}, color = {item['color']}")
        x = -item['x'] + abs(max_x)
        y = -item['y'] + abs(max_y)
        color = item['color']
        # print(row, column, color)
        layout[y, x] = '.' if color == 0 else '#'

    temp = [''.join(layout[j, :]) for j in range(range_y)]

    return temp


def output_to_file(display):
    """ Output the final graph to a text file so we can actually see it """

    file1 = open("../data/day11_output.txt", "w")
    for item in display:
        file1.write((item + '\n'))

    file1.close()


def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.boot()
    computer.program_load()
    computer.flash_memory()
    computer.halt_condition = True
    # computer.process_run()

    return computer


def test():
    """ main() program """

    robot = \
        intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Registration Identifier')

    steps = run(robot)

    del robot

    return steps


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

steps, coordinates, display = run(robot)


# %% Production Environment (LOL)

# if __name__ == "__main__":
#     steps = test()

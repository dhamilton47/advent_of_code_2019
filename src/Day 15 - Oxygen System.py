# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 00:58:30 2020

@author: Dan J Hamilton
"""


# import math

import aoc
from computer import Computer


# %%

"""
The remote control program executes the following steps in a loop forever:

- Accept a movement command via an input instruction.
- Send the movement command to the repair droid.
- Wait for the repair droid to finish the movement operation.
- Report on the status of the repair droid via an output instruction.

Only four movement commands are understood: north (1), south (2),
west (3), and east (4). Any other command is invalid. The movements
differ in direction, but not in distance: in a long enough east-west
hallway, a series of commands like 4,4,4,4,3,3,3,3 would leave the
repair droid back where it started.

The repair droid can reply with any of the following status codes:

0: The repair droid hit a wall. Its position has not changed.
1: The repair droid has moved one step in the requested direction.
2: The repair droid has moved one step in the requested direction; its new
   position is the location of the oxygen system.

You don't know anything about the area around the repair droid, but you
can figure it out by watching the status codes.
"""


def survey_starter(answer):
    """
    This is the inital survey of the 4 directions one could move based
    on the starting position.  This differs from survey() in that only
    three directions are tested from each open position as we came from
    the fourth and already know its value.

    Parameters
    ----------
    answer : tuple
        Path taken from the origin to the oxygen tank.

    Returns
    -------
    answer : tuple
        Path taken from the origin to the oxygen tank.
    path : tuple
        A tuple representing the path of steps the Droid can make
        from the origin.
    coordinates : dict
        Dictionary containing the detected wall coordinate of the maze.

    """

    paths = {}
    coordinates = {(0,0): charset[1]}
    # coordinates = {(0,0): '. '}
    for i in [1, 2, 3, 4]:
        path = (i, )

        test = move(path)
        # paths[path] = move(path)

        coordinate = map_coordinate(path)
        coordinates[coordinate] = test

        # if test == '#':
        #     coordinate = map_coordinate(path)
        #     coordinates[coordinate] = '#'

        if test == charset[2]:
            answer = answer.append(path)

        if test in (charset[1], charset[2]):
            paths[path] = test

    return answer, paths, path, coordinates


def survey(coordinates, paths, answer):
    """
    Returns the reported responses from the droid for the three unknown
    adjacent squares.

    Parameters
    ----------
    coordinates : dict
        Dictionary containing the detected wall coordinate of the maze.
    answer : tuple
        Path taken from the origin to the oxygen tank.

    Returns
    -------
    answer : tuple
        Path taken from the origin to the oxygen tank.
    path : tuple
        A tuple representing the path of steps the Droid can make
        from the origin.
    coordinates : dict
        Dictionary containing the detected wall coordinate of the maze.

    """
    live_paths = {}
    previous_paths = paths.copy()
    for item in previous_paths:
        for i in [1, 2, 3, 4]:
            if previous_paths[item] != charset[0]:
                if list(item)[-1] == [2, 1, 4, 3][i - 1]:
                    continue

                path = item + (i, )

                test = move(path)

                coordinate = map_coordinate(path)
                coordinates[coordinate] = test

                if test in (charset[1], charset[2]):
                    live_paths[path] = move(path)

                if test == charset[2]:
                    answer = path
                    # answer = answer.append(path)

    return answer, live_paths, path, coordinates


def move(path):
    """
    Runs the droid along the specified path.

    Parameters
    ----------
    path : tuple
        A tuple representing the path of steps the Droid can make
        from the origin.

    Returns
    -------
    string
        Character string representation of the endpoint of the given path.

    """
    machine = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Oxygen System')

    for item in path:
        machine.emulated_input = item
        machine.process_run()

    return charset[machine.output_value]
    # return ['# ', '. ', 'O '][machine.output_value]


def map_coordinate(path):
    """
    Transforms a path into a graphable coordinate displaying the wall
    locations.

    Parameters
    ----------
    path : tuple
        A tuple representing the path of steps the Droid can make
        from the origin.

    Returns
    -------
    ending_x : int64
        The ending x value of the coordinate (x, y).
    ending_y : TYPE
        The ending y value of the coordinate (x, y).

    """

    ending_x = 0
    ending_y = 0

    for item in path:

        adj_x, adj_y = [(0, -1), (0, 1), (-1, 0), (1, 0)][item - 1]
        # adj_x, adj_y = [(0, 1), (0, -1), (-1, 0), (1, 0)][item - 1]
        ending_x += adj_x
        ending_y += adj_y

    return (ending_x, ending_y)


# %%

def dimensions(coordinates):
    """ Find the dimensions of the graph we need to create """

    x_s = []
    y_s = []

    for item in list(coordinates.keys()):
        x, y = item
        x_s.append(x)
        y_s.append(y)

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

    return (min_x, min_y, range_x, range_y)
    # return (min_x, max_y, range_x, range_y)


def create_display(coordinates, droid):
    """ Create the maze after every survey """

    min_x, min_y, range_x, range_y = dimensions(coordinates)
    # min_x, max_y, range_x, range_y = dimensions(coordinates)
    display = [[charset[0] for i in range(range_x)] for j in range(range_y)]
    # display = [['# ' for i in range(range_x)] for j in range(range_y)]
    # display = [['#' for i in range(range_y + 2)] for j in range(range_x + 2)]
    # print(f"rows = {len(display)}, columns = {len(display[0])}")
    # opcode = 0

    for item, value in enumerate(coordinates):
        x, y = value
        # print(f"rows = {len(display)}, columns = {len(display[0])}")
        # print(f"item = {item}, value = {value}, "
        #       f"orig x = {x}, min x = {min_x}, range x = {range_x}, "
        #       f"adj x = {x - min_x + 1}, "
        #       f"orig y = {y}, max y = {max_y}, range y = {range_y}, "
        #       f"adj y = {(y - max_y) + range_y}")
        # display[x - min_x][(y - max_y) + range_y - 1] = coordinates[value]
        display[y - min_y][x - min_x] = coordinates[value]
        # display[x - min_x + 1][(y - max_y) + range_y + 1] = coordinates[value]

    x, y = droid
    # display[(y - max_y) + range_y - 1][x - min_x] = 'D'
    display[y - min_y][x - min_x] = charset[3]

    for row in range(len(display)):
        line = ''.join(display[row][:])
        print(line)

    print()

    return display


# %%
def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.boot()
    computer.program_load()
    computer.flash_memory()
    computer.halt_condition = True

    return computer


def test():
    """ main() program """

    possible_paths = []

    possible_paths, paths, path, coordinates = survey_starter(possible_paths)

    while possible_paths == []:
        possible_paths, paths, path, coordinates = \
            survey(coordinates, paths, possible_paths)

    # del driod, display

    print(f"Shortest path to Oxygen tank has {len(path)} steps.")


# %% Development Environment

possible_paths = []
spacer = ' '
charset = [chr(35) + spacer, chr(46) + spacer, chr(79) + spacer, chr(68) + spacer]
# charset = ['# ', '. ', 'O ']
possible_paths, paths, path, coordinates = \
    survey_starter(possible_paths)

while possible_paths == []:
    possible_paths, paths, path, coordinates = \
        survey(coordinates, paths, possible_paths)


# min_x, max_y, range_x, range_y = dimensions(coordinates)
display = create_display(coordinates, (0,0))
# display = create_display(coordinates, (1 - min_x, max_y + 1))


# %%
# paths = {(2,): '.'}
# # print(coordinates, paths, possible_paths)
# while paths != {}:
#     possible_paths, paths, path, coordinates = \
#         survey(coordinates, paths, possible_paths)
# min_x, max_y, range_x, range_y = dimensions(coordinates)
# display = create_display(coordinates, (1 - min_x, max_y + 1))
# %% Production Environment (LOL)

# if __name__ == "__main__":
#     test()

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

# %%


# def dimensions(x_s, y_s):
#     """ Find the dimensions of the graph we need to create """

#     max_x = max(x_s)
#     min_x = min(x_s)

#     max_y = max(y_s)
#     min_y = min(y_s)

#     range_x = max_x - min_x + 1
#     range_y = max_y - min_y + 1
#     print(f"\nRange of the x-axis = {range_x}\n"
#           f"  Min x = {min_x}\n"
#           f"  Max x = {max_x}\n\n"
#           f"Range of the y-axis = {range_y}\n"
#           f"  Min y = {min_y}\n"
#           f"  Max y = {max_y}")

#     return (max_x, max_y, range_x, range_y)


# def create_display(machine, coordinates, droid):
#     """ Create the maze after every survey """

#     display = [['#' for i in range(44)] for j in range(20)]
#     # opcode = 0

#     for item, value in coordinates.items():
#         x, y = item
#         # display[x][y] = ['#', '.', 'O'][value]

#     x, y = droid
#     display[x][y] = 'D'

#     for row in range(len(display)):
#         line = ''.join(display[row])
#         print(line)

#     print()

#     return display


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

    coordinates = {}
    for i in [1, 2, 3, 4]:
        path = (i, )

        coordinates[path] = move(path)

        if coordinates[path] == 'O':
            answer = answer.append(path)

    return answer, path, coordinates


def survey(coordinates, answer):
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
    path = ()
    previous_paths = coordinates.copy()
    for item in previous_paths:
        # print(f"item = {item}")

        for i in [1, 2, 3, 4]:

            if previous_paths[item] != '#':
                if list(item)[-1] == [2, 1, 4, 3][i - 1]:
                    continue

                path = item + (i, )

                # result = move(path)
                coordinates[path] = move(path)
                # print(result)
                # print(path_to_follow)

                if coordinates[path] == 'O':
                    answer = answer.append(path)

    return answer, path, coordinates


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

    return ['#', '.', 'O'][machine.output_value]


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

        adj_x, adj_y = [(0, 1), (0, -1), (-1, 0), (1, 0)][item - 1]
        ending_x += adj_x
        ending_y += adj_y

    return (ending_x, ending_y)


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

    possible_paths, path, coordinates = survey_starter(possible_paths)

    while possible_paths == []:
        possible_paths, path, coordinates = survey(coordinates, possible_paths)

    # del driod, display

    print(f"Shortest path to Oxygen tank has {len(path)} steps.")


# %% Development Environment


# possible_paths = []

# possible_paths, path, coordinates = survey_starter(possible_paths)

# while possible_paths == []:
#     possible_paths, path, coordinates = survey(coordinates, possible_paths)


# %% Production Environment (LOL)

# if __name__ == "__main__":
#     test()

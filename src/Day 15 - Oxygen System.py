# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 00:58:30 2020

@author: Dan J Hamilton
"""


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


SPACER = ' '
CHARSET = \
    [chr(35) + SPACER, chr(46) + SPACER, chr(79) + SPACER, chr(68) + SPACER]


def survey_starter(start=()):
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

    answer = []
    paths = {}
    coordinates = {(0, 0): CHARSET[1]}
    for i in [1, 2, 3, 4]:
        path = start + (i, )

        test_value = move(path)

        coordinate = map_coordinate(path)
        coordinates[coordinate] = test_value

        if test_value in (CHARSET[1], CHARSET[2]):
            paths[path] = test_value

        if test_value == CHARSET[2]:
            answer = answer.append(path)

    return answer, paths, path, coordinates


def survey(coordinates, paths):
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

    answer = []
    live_paths = {}
    previous_paths = paths.copy()
    for item in previous_paths:
        for i in [1, 2, 3, 4]:
            if previous_paths[item] != CHARSET[0]:
                if list(item)[-1] == [2, 1, 4, 3][i - 1]:
                    continue

                path = item + (i, )

                test_value = move(path)

                coordinate = map_coordinate(path)
                coordinates[coordinate] = test_value

                if test_value in (CHARSET[1], CHARSET[2]):
                    live_paths[path] = test_value

                if test_value == CHARSET[2]:
                    answer = path

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
        machine.io.input_value = [item]
        machine.process_run()

    return CHARSET[machine.io.output_value]


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
        ending_x += adj_x
        ending_y += adj_y

    return (ending_x, ending_y)


# %%

def dimensions(coordinates):
    """ Find the dimensions of the graph we need to create """

    x_s = []
    y_s = []

    for item in list(coordinates.keys()):
        _x, _y = item
        x_s.append(_x)
        y_s.append(_y)

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


def create_display(coordinates, droid):
    """ Create the maze after every survey """

    min_x, min_y, range_x, range_y = dimensions(coordinates)
    display = [[CHARSET[0] for i in range(range_x)] for j in range(range_y)]
    # print(f"rows = {len(display)}, columns = {len(display[0])}")

    for _, value in enumerate(coordinates):
        _x, _y = value
        display[_y - min_y][_x - min_x] = coordinates[value]

        # print(f"rows = {len(display)}, columns = {len(display[0])}")
        # print(f"item = {item}, value = {value}, "
        #       f"orig x = {x}, min x = {min_x}, range x = {range_x}, "
        #       f"adj x = {x - min_x + 1}, "
        #       f"orig y = {y}, max y = {max_y}, range y = {range_y}, "
        #       f"adj y = {(y - max_y) + range_y}")

    droid_x, droid_y = droid
    display[droid_y - min_y][droid_x - min_x] = CHARSET[3]

    for row in range(len(display)):
        line = ''.join(display[row][:])
        print(line)

    print()

    return display


# %%
def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.flash_memory()
    computer.halt_condition = True

    return computer


def main():
    """ main() program """

    # possible_paths, paths, path, coordinates = survey_starter()

    # while possible_paths == []:
    #     possible_paths, paths, path, coordinates = \
    #         survey(coordinates, paths)

    answer, paths, path, coordinates = survey_starter()
    while answer == []:
        answer, paths, path, coordinates = \
            survey(coordinates, paths)
    create_display(coordinates, (0, 0))
    # display = create_display(coordinates, (0, 0))
    distance_offset = len(answer)

    answer, paths, path, coordinates = survey_starter(answer)
    while paths != {}:
        answer, paths, path, coordinates = \
            survey(coordinates, paths)
    create_display(coordinates, (0, 0))
    # display = create_display(coordinates, (0, 0))
    oxygen_distance = len(path) - distance_offset - 1

    del coordinates, path  # display

    print(f"Shortest path to Oxygen tank has {distance_offset} steps.")
    print(f"Time to Oxygenate sector is {oxygen_distance} minutes.")


# %% Development Environment

# answer, paths, path, coordinates = survey_starter()
# while answer == []:
#     answer, paths, path, coordinates = \
#         survey(coordinates, paths)
# display = create_display(coordinates, (0, 0))
# distance_offset = len(answer)
# answer, paths, path, coordinates = survey_starter(answer)
# while paths != {}:
#     answer, paths, path, coordinates = \
#         survey(coordinates, paths)
# display = create_display(coordinates, (0, 0))
# oxygen_distance = len(path) - distance_offset - 1
# print(f"Shortest path to Oxygen tank has {distance_offset} steps.")
# print(f"Time to Oxygenate sector is {oxygen_distance} minutes.")

# %% Production Environment (LOL)

if __name__ == "__main__":
    main()

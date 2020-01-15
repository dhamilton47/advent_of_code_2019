# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 07:38:54 2020

@author: Dan J Hamilton
"""


import numpy as np

import aoc
from computer import Computer


# %%

"""
The program uses two input instructions to request the X and Y position
to which the drone should be deployed. Negative numbers are invalid and
will confuse the drone; all numbers should be zero or positive.

Then, the program will output whether the drone is stationary (0) or
being pulled by something (1). For example, the coordinate X=0, Y=0
is directly in front of the tractor beam emitter, so the drone control
program will always report 1 at that location.

How many points are affected by the tractor beam in the 50x50 area
closest to the emitter?
"""

# %%


def create_array(rows, columns):
    """
    Create a two-dimensional array.  Default values are zero.

    Parameters
    ----------
    rows : int
        Length of the first demension.
    columns : int
        Length of the second demension..

    Returns
    -------
    array : int
        A zero filled two-dimensional array.

    """

    array = np.zeros((rows, columns), dtype=int)

    return array


def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.boot()
    computer.program_load()
    computer.flash_memory()

    return computer


# def test():
#     """ main() program """

#     possible_paths = []

#     possible_paths, paths, path, coordinates = survey_starter(possible_paths)

#     while possible_paths == []:
#         possible_paths, paths, path, coordinates = \
#             survey(coordinates, paths, possible_paths)

#     # del driod, display

#     print(f"Shortest path to Oxygen tank has {len(path)} steps.")


# %% Development Environment

ROWS = 50
COLUMNS = 50

array = create_array(ROWS, COLUMNS)

for row in range(ROWS):
    for column in range(COLUMNS):

        machine = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Tractor Beam')

        machine.emulated_input = [row, column]
        machine.process_run()
        array[row, column] = machine.output_value

        del machine

# print(array)
print(f"Day 19, Part 1 = {array.sum(None)}")

ROWS = 100
COLUMNS = 100

array = create_array(ROWS, COLUMNS)

for row in range(ROWS):
    for column in range(COLUMNS):

        machine = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Tractor Beam')

        machine.emulated_input = [1073 + row, 411 + column]
        machine.process_run()
        array[row, column] = machine.output_value

        del machine

# print(array.sum(None))

print(f"Day 19, Part 2 = {411 + 1073 * 10000}")
# %% Production Environment (LOL)

# if __name__ == "__main__":
#     test()

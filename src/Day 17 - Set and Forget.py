# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:25:12 2020

@author: Dan J Hamilton
"""


import numpy as np

import aoc
from computer import Computer


# %%

"""
Running the ASCII program on your Intcode computer will provide the current
view of the scaffolds. This is output, purely coincidentally,
as ASCII code:
    35 means #,
    46 means .,
    10 starts a new line
    and so on.

(Within a line, characters are drawn left-to-right.)


In the camera output, # represents a scaffold and . represents open space.
The vacuum robot is visible as ^, v, <, or > depending on whether it is
facing up, down, left, or right respectively. When drawn like this, the
vacuum robot is always on a scaffold; if the vacuum robot ever walks off
of a scaffold and begins tumbling through space uncontrollably, it will
instead be visible as X.

The first step is to calibrate the cameras by getting the alignment parameters
of some well-defined points. Locate all scaffold intersections; for each,
its alignment parameter is the distance between its left edge and the left
edge of the view multiplied by the distance between its top edge and the top
edge of the view. Here, the intersections from the above image are marked O
"""

# %%


def reveal_scaffold():
    i = 0
    opcode = 0
    data_as_string = ''
    data_as_matrix = []
    newline_loc = []
    machine = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'ASCII')
    machine.memory.bank[0] = 1

    while opcode != 99:
        opcode = machine.process_run()
        data_as_string += chr(machine.io.output_value)
        data_as_matrix.append(machine.io.output_value)
        if machine.io.output_value == 10:
            newline_loc.append(i)
        i += 1

    print(data_as_string)

    return data_as_matrix, newline_loc


def plot_scaffold(data, newline_loc):
    padding = 2
    columns = padding + (newline_loc[1] - newline_loc[0])
    rows = padding + (len(data) // (columns - padding))
    array = np.zeros((rows, columns), dtype=int)

    index = 0
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            array[i, j] = data[index]

            index += 1

    return array


def check_adjacent(mat, character):
    rows = len(mat)
    columns = len(mat[0])
    count = 0
    coordinates = []

    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            if mat[row, column] == ord(character):
                count = (mat[row - 1, column] +
                         mat[row + 1, column] +
                         mat[row, column - 1] +
                         mat[row, column + 1])

            if count == 4 * ord(character):
                coordinates.append((row, column))

    return coordinates


def alignment_parameters(coordinates):
    alignment_parameter = 0
    sum_of_alignment_parameters = 0

    for item in coordinates:
        left, top = item
        alignment_parameter = (left - 1) * (top - 1)
        sum_of_alignment_parameters += alignment_parameter

    return sum_of_alignment_parameters


def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.flash_memory()
    # computer.flash_memory(len(computer.program.code) + 2000)
    computer.halt_condition = True

    return computer


def main():
    """ main() program """

    scaffold, newline_locs = reveal_scaffold()
    array = plot_scaffold(scaffold, newline_locs)
    coordinates = check_adjacent(array, '#')
    sum_of_alignment_parameters = alignment_parameters(coordinates)
    print(f"Day 17, part 1 - The sum of the alignment parameters "
          f"= {sum_of_alignment_parameters}")


# %% Development Environment
"""
Part 1 - Next Steps

1. set coordinates to path - Planet of Discord adjacent values tech
    (if = 4, then intersection, possible values = [0, 1, 2, 4])
2. find intersections along path
3. calculate alignment values for each of the intersections
4. sum alignment values

"""

# scaffold, newline_locs = reveal_scaffold()
# array = plot_scaffold(scaffold, newline_locs)
# coordinates = check_adjacent(array, '#')
# sum_of_alignment_parameters = alignment_parameters(coordinates)
#


"""
Part 2 - Next Steps

Creatnig a program to figure these step out is mor than necessary to complete
this puzzle.  Hence the following approach will be used:

1. Visually scan to determine each line segment's direction change and
   distance.
2. Determine 'movement functions' in item 1's results.  Should be able
   to determine a maximum of three (3) patterns.
3. Sequence the movement functions to travel from the beginning of
   the scaffold and arrive at the end of it.  This will be the
   'movement routine'.
4. Translate the movement routine and movement functions into ASCCI codes.
    They should have a max length of 20 characters.
5. Set intcode location 0 to the value 2.
6. Enter the translated movement routine and functions as per
   the instructions. Include a newline ASCII code at the end of each
   instruction.
7. Enter y or n for using the live camera feed.


Step 1:
    L10, R8, R6, R10, L12, R8, L12, L10, R8, R6, R10, L12, R8, L12, L10,
    R8, R8, L10, R8, R8, L12, R8, L12, L10, R8, R6, R10, L10, R8, R8,
    L10, R8, R6, R10

Step 2:
    We can break the sequence in step 1 as follows:
    L10, R8, R6, R10, (A)
    L12, R8, L12,     (B)
    L10, R8, R6, R10, (A)
    L12, R8, L12,     (B)
    L10, R8, R8,      (C)
    L10, R8, R8,      (C)
    L12, R8, L12,     (B)
    L10, R8, R6, R10, (A)
    L10, R8, R8,      (C)
    L10, R8, R6, R10  (A)

    This gives us the program functions:
        A: L, 10, R, 8, R, 6, R, 10
        B: L, 12, R, 8, L, 12
        C: L, 10, R, 8, R, 8

Step 3:
    The movement routine is then:
        A, B, A, B, C, C, B, A, C, A
"""

M = 'A,B,A,B,C,C,B,A,C,A\n'
A = 'L,10,R,8,R,6,R,10\n'
B = 'L,12,R,8,L,12\n'
C = 'L,10,R,8,R,8\n'


def ascii_interpreter(val):
    val1 = [ord(val[i]) for i in range(len(val))]

    return val1


M = ascii_interpreter(M)
A = ascii_interpreter(A)
B = ascii_interpreter(B)
C = ascii_interpreter(C)
VIDEO = ascii_interpreter('y\n')

instructions = M + A + B + C + VIDEO

main()
opcode = 0
machine = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'ASCII')
machine.memory.bank[0] = 2
machine.io.input_value = instructions
while opcode != 99:
    opcode = machine.process_run()

print(f"Day 17, Part 2 - Dust collected = {machine.io.output_value}")


# %% Production Environment (LOL)

# if __name__ == "__main__":
#     main()

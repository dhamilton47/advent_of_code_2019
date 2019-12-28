# -*- coding: utf-8 -*-
"""
Created on Tue Dec  24 07:54:20 2019

@author: Dan J Hamilton
"""


from __future__ import annotations

import numpy as np
import functools

import aoc


def transform_program(x):
    x = list(x.strip("\n") + ' ')

    z = np.zeros((7, 7), dtype=int)

    for row in range(1, 6):
        for column in range(1, 7):
            z[row, column] = 1 if x[((row - 1) * 6) + column - 1] == '#' else 0

    return np.array(z, dtype=int).reshape(1, 7, 7)


def check_adjacent(mat):
    z = np.zeros((7, 7), dtype=int)

    for row in range(1, 6):
        for column in range(1, 6):
            count = (mat[row - 1, column] +
                     mat[row + 1, column] +
                     mat[row, column - 1] +
                     mat[row, column + 1])

            z[row, column] = bug_no_bug(mat[row, column], count)

    return z


def bug_no_bug(x, count):
    if x == 1:
        z = 0 if count != 1 else 1

    if x == 0:
        z = 1 if (count == 1 or count == 2) else 0

    if x == 99:
        z = 99

    return z


def biodiversity(layout):
    power_matrix = [2 ** i for i in range(25)]
    power_matrix = np.array(power_matrix).reshape(1, 5, 5)

    x_product = np.multiply(power_matrix, layout[1:6, 1:6]).flatten()

    return functools.reduce(lambda a, b: a + b, x_product)


def layers_at_minute(x):
    return 3 + 2 * ((x % 2) + (x // 2))


def print_layer(layer):
    out = ''
    for j in range(5):
        for k in range(5):
            if layer[j, k] == 1:
                add_to_out = '# '
            elif layer[j, k] == 0:
                add_to_out = '. '
            else:
                add_to_out = '? '

            out += add_to_out
        out += '\n'

    print(out)


def count_critters(matrix, layers_needed):
    count = 0
    for i in range(1, layers_needed - 1):
        for j in range(1, 6):
            for k in range(1, 6):
                if j == 3 and k == 3:
                    count += 0
                else:
                    count += matrix[i, j, k]

    return count


def sum_5(matrix, plane, row, column, direction):
    """
    """
    if direction == 'across':
        x = functools.reduce(lambda x, y: x + y,
                             matrix[plane, row, column:column + 5])
    elif direction == 'down':
        x = functools.reduce(lambda x, y: x + y,
                             matrix[plane, row:row + 5, column])

    return x


def handle_outer_padding(matrix, planes):
    """
    Get the outer values needed for the next plane and place in
    appropriate pad spaces of that next frame.

    matrix = the complete folded space required to reach the end of the time
             frame.
    planes = number of planes to process, excluding the end padding planes,
             for the complete time frame.
    """
    for plane in range(1, planes - 1):
        # Top
        matrix[plane, 0, 1:6] = matrix[plane - 1, 2, 3]

        # Left
        matrix[plane, 1:6, 0] = matrix[plane - 1, 3, 2]

        # Bottom
        matrix[plane, 6, 1:6] = matrix[plane - 1, 4, 3]

        # Right
        matrix[plane, 1:6, 6] = matrix[plane - 1, 3, 4]

    return matrix


def check_adjacent_folding(matrix, planes):
    """
    Determine count of bugs in the 4 adjacent sides within the non-padded
    portion of each plane.  The four spaces adjacent to the center are
    adjusted for the next planes outer values.

    matrix = the complete folded space required to reach the end of the time
             frame.
    planes = number of planes to process, excluding the end padding planes,
             for the complete time frame.
    """
    matrix_copy = matrix.copy()

    for plane in range(1, planes - 1):
        count_top = sum_5(matrix, plane + 1, 1, 1, 'across')
        count_bottom = sum_5(matrix, plane + 1, 5, 1, 'across')
        count_left = sum_5(matrix, plane + 1, 1, 1, 'down')
        count_right = sum_5(matrix, plane + 1, 1, 5, 'down')

        for row in range(1, 6):
            for column in range(1, 6):
                count = (matrix[plane, row - 1, column] +
                         matrix[plane, row + 1, column] +
                         matrix[plane, row, column - 1] +
                         matrix[plane, row, column + 1])

                if row == 2 and column == 3:
                    count += count_top
                if row == 4 and column == 3:
                    count += count_bottom
                if row == 3 and column == 2:
                    count += count_left
                if row == 3 and column == 4:
                    count += count_right

                matrix_copy[plane, row, column] = \
                    bug_no_bug(matrix[plane, row, column], count)

    return matrix_copy


def day24_part1(dwarf_planet, minutes):
    for i in range(1, minutes):
        next_minute = check_adjacent(dwarf_planet[i - 1, :, :])
        next_minute = next_minute.reshape(1, 7, 7)
        dwarf_planet = np.concatenate((dwarf_planet, next_minute), axis=0)

        for j in range(i - 1):
            truthy = np.array_equal(dwarf_planet[i, :, :],
                                    dwarf_planet[j, :, :])
            if truthy:
                return dwarf_planet[i, :, :]


def day24_part2(eris_initiator, minutes):
    layers_needed = layers_at_minute(minutes)
    initial_layer = ((layers_needed - 1) // 2)

    # We are setting up the folded space matrix to have one extra layer at each
    # end.  This way we can execute each layer using the same set of positional
    # functions as opposed to writing inner layer functions and end layer ones.

    eris = np.zeros((layers_needed, 7, 7), dtype=int)
    eris[initial_layer, :, :] = eris_initiator
    eris[:, 3, 3] = 0

    # loop on time
    for minute in range(1, minutes + 1):
        eris_copy = eris.copy()

    # process outer padding
        eris_copy = handle_outer_padding(eris, layers_needed)

    # process inner sums
        eris_copy = check_adjacent_folding(eris, layers_needed)

        eris_copy[:, 3, 3] = 0

        eris = eris_copy

    # count critters
    print(f"Day 24, Part 2 - There are currently "
          f"{count_critters(eris, layers_needed)}"
          f" bugs present.")


# %% Development Environment

# # set up total time-line 3-d matrix
# txtfile = "../data/adventofcode_2019_day_24_input.txt"
# contents = aoc.read_program(txtfile)
# eris_initiator = transform_program(contents)
# minutes = 200

# layers_needed = layers_at_minute(minutes)
# initial_layer = ((layers_needed - 1) // 2)

# # We are setting up the folded space matrix to have one extra layer at each
# # end.  This way we can execute each layer using the same set of positional
# # functions as opposed to writing inner layer functions and end layer ones.

# eris = np.zeros((layers_needed, 7, 7), dtype=int)
# eris[initial_layer, :, :] = eris_initiator
# len_eris = layers_needed - 2
# eris[:, 3, 3] = 0
# eris_one_minute_later = np.zeros((layers_needed, 7, 7), dtype=int)
# eris_one_minute_later[initial_layer, :, :] = eris_initiator

# # loop on time
# for minute in range(1, minutes + 1):
#     eris_copy = eris.copy()

# # process outer padding
#     eris_copy = handle_outer_padding(eris, layers_needed)

# # process inner sums
#     eris_copy = check_adjacent_folding(eris, layers_needed)

#     eris_copy[:, 3, 3] = 0

#     eris = eris_copy

# # count critters
# print(f"Day 24, Part 2 - There are currently "
#       f"{count_critters(eris, layers_needed)}"
#       f" bugs present.")


# %% Production Environment

txtfile = "../data/adventofcode_2019_day_24_input.txt"
contents = aoc.read_program(txtfile)
eris = transform_program(contents)
minutes = 50

layer = day24_part1(eris, minutes)
biodiversity_rating = biodiversity(layer)
print(f"Day 24, Part 1 - Biodiversity rating = {biodiversity_rating}")

txtfile = "../data/adventofcode_2019_day_24_input.txt"
contents = aoc.read_program(txtfile)
eris_initiator = transform_program(contents)
minutes = 200

day24_part2(eris_initiator, minutes)

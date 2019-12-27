# -*- coding: utf-8 -*-
"""
Created on Tue Dec  24 07:54:20 2019

@author: Dan J Hamilton
"""


from __future__ import annotations
from typing import Set, Sequence, Tuple

import numpy as np
import functools
import scipy.signal as sg
import timeit

import aoc


# %% Transform the "XXXX" from a string to a list
def transform_program(x):
    x = list(x.strip("\n") + ' ')

    z = np.zeros((7, 7), int)

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
    # print(x,count)
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


# # %% Import the "XXXX" data (as a string)
# def read_program(txtfile):
#     f = open(txtfile, "r")
#     if f.mode == 'r':
#         contents = f.read()
#     f.close()

#     return contents


# %% Transform the "XXXX" from a string to a list
def transform_program_5_x_5(x):
    x = list(x.strip("\n"))
    y = []
    for i in x:
        if i == '.':
            y.append(0)
        elif i == '#':
            y.append(1)
        else:
            continue

    eris = np.array(y, dtype='int16').reshape(1, 5, 5)

    return eris


# def check_adjacent(mat):
#     z = np.zeros((5, 5), dtype='int16')

#     for i in range(5):
#         for j in range(5):
#             if mat[i, j] == 0:
#                 z = bug_born(mat, z, i, j)
#             else:
#                 z[i, j] = 0

#     for i in range(5):
#         for j in range(5):
#             if mat[i, j]:
#                 z = bug_dies(mat, z, i, j)

#     return z


# def bug_dies(mat, z, i, j):
#     count = 0
#     if j == 0:
#         if mat[i, j + 1]:
#             count += 1
#     elif j == 4:
#         if mat[i, j - 1]:
#             count += 1
#     else:
#         if mat[i, j + 1]:
#             count += 1
#         if mat[i, j - 1]:
#             count += 1

#     if i == 0:
#         if mat[i + 1, j]:
#             count += 1
#     elif i == 4:
#         if mat[i - 1, j]:
#             count += 1
#     else:
#         if mat[i - 1, j]:
#             count += 1
#         if mat[i + 1, j]:
#             count += 1

#     z[i, j] = 1 if count == 1 else 0

#     return z


# def bug_born(mat: np.array, z: int, j: int, k: int) -> int:
#     count = 0
#     if k == 0:
#         count += 0
#     else:
#         if mat[j, k - 1]:
#             count += 1

#     if k == 4:
#         count += 0
#     else:
#         if mat[j, k + 1]:
#             count += 1

#     if j == 0:
#         count += 0
#     else:
#         if mat[j - 1, k]:
#             count += 1

#     if j == 4:
#         count += 0
#     else:
#         if mat[j + 1, k]:
#             count += 1

#     z[j, k] = 1 if count == 1 or count == 2 else 0

#     return z


# def biodiversity(layout):
#     power_matrix = [2 ** i for i in range(25)]
#     power_matrix = np.array(power_matrix).reshape(1, 5, 5)

#     x_product = np.multiply(power_matrix, layout).flatten()

#     return functools.reduce(lambda a, b: a + b, x_product)


# def day24_part1(dwarf_planet, minutes):
#     for i in range(1, minutes):
#         next_minute = check_adjacent(dwarf_planet[i - 1, :, :])
#         next_minute = next_minute.reshape(1, 5, 5)
#         dwarf_planet = np.concatenate((dwarf_planet, next_minute), axis=0)

#         for j in range(i - 1):
#             truthy = np.array_equal(dwarf_planet[i, :, :],
#                                     dwarf_planet[j, :, :])
#             if truthy:
#                 return dwarf_planet[i, :, :]


# def dead_bug(x, count):
#     # print(x, count)
#     z = x
#     if x == 1:
#         z = 0 if count != 1 else 1
#         # if count != 1:
#         #     z = 0
#         # else:
#         #     z = 1

#     return z


# # def baby_bug(x, count):
# def baby_bug(x, count):
#     z = x
#     if x == 0:
#         z = 1 if (count == 1 or count == 2) else 0

#        # if (count == 1 or count == 2):
#         #     z = 1
#         # else:
#         #     z = 0

#     return z


def inner_8s_top(m, x, i, j, k):
    """
    This is an 8-side touching, top, center function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i + 0, j - 1, k] \
        + m[i + 1, 0, 0] \
        + m[i + 1, 0, 1] \
        + m[i + 1, 0, 2] \
        + m[i + 1, 0, 3] \
        + m[i + 1, 0, 4] \
        + m[i + 0, j, k - 1] \
        + m[i + 0, j, k + 1]

    z = bug_no_bug(x, count)

    return z


def inner_8s_left(m, x, i, j, k):
    """
    This is an 8-side touching, left, center function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i + 0, j - 1, k] \
        + m[i + 0, j + 1, k] \
        + m[i + 0, j, k - 1] \
        + m[i + 1, 0, 0] \
        + m[i + 1, 1, 0] \
        + m[i + 1, 2, 0] \
        + m[i + 1, 3, 0] \
        + m[i + 1, 4, 0]

    z = bug_no_bug(x, count)

    return z


def inner_8s_right(m, x, i, j, k):
    """
    This is an 8-side touching, right, center function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i + 0, j - 1, k] \
        + m[i + 0, j + 1, k] \
        + m[i + 1, 0, 4] \
        + m[i + 1, 1, 4] \
        + m[i + 1, 2, 4] \
        + m[i + 1, 3, 4] \
        + m[i + 1, 4, 4] \
        + m[i + 0, j, k + 1]

    # print(f"level {i}, x = {x}, row = {j}, column = {k}, 4 count = {count}, z1 = {z}")
    # print(f"level {i}, x = {x}, row = {j}, column = {k}, 4 count = {count}, z2 = {z}\n")
    z = bug_no_bug(x, count)

    return z


def inner_8s_bottom(m, x, i, j, k):
    """
    This is an 8-side touching, bottom, center function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i + 1, 4, 0] \
        + m[i + 1, 4, 1] \
        + m[i + 1, 4, 2] \
        + m[i + 1, 4, 3] \
        + m[i + 1, 4, 4] \
        + m[i + 0, j + 1, k] \
        + m[i + 0, j, k - 1] \
        + m[i + 0, j, k + 1]

    z = bug_no_bug(x, count)

    return z


def inner_4s(m, x, i, j, k):
    """
    This is a 4-side touching, same level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i - 0, j - 1, k] \
        + m[i - 0, j + 1, k] \
        + m[i - 0, j, k - 1] \
        + m[i - 0, j, k + 1]

    z = bug_no_bug(x, count)

    return z


def outer_4s_top(m, x, i, j, k):
    """
    This is a 4-side touching, top-only different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i - 1, 1, 2] \
        + m[i - 0, j + 1, k] \
        + m[i - 0, j, k - 1] \
        + m[i - 0, j, k + 1]

    z = bug_no_bug(x, count)

    return z


def outer_4s_left(m, x, i, j, k):
    """
    This is a 4-side touching, left-only different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """
    # print(i, j, k)
    count \
        = m[i - 0, j - 1, k] \
        + m[i - 0, j + 1, k] \
        + m[i - 1, 1, 2] \
        + m[i - 0, j, k + 1]

    z = bug_no_bug(x, count)

    return z


def outer_4s_right(m, x, i, j, k):
    """
    This is a 4-side touching, right-only different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i - 0, j - 1, k] \
        + m[i - 0, j + 1, k] \
        + m[i - 0, j, k - 1] \
        + m[i - 1, 2, 3]

    z = bug_no_bug(x, count)

    return z


def outer_4s_bottom(m, x, i, j, k):
    """
    This is a 4-side touching, bottom-only different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i - 0, j - 1, k] \
        + m[i - 1, 3, 2] \
        + m[i - 0, j, k - 1] \
        + m[i - 0, j, k + 1]

    z = bug_no_bug(x, count)

    return z


def outer_4s_bottomleft(m, x, i, j, k):
    """
    This is a 4-side touching, bottom-left different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i - 0, j - 1, k] \
        + m[i - 1, 3, 2] \
        + m[i - 1, 2, 1] \
        + m[i - 0, j, k + 1]

    z = bug_no_bug(x, count)

    return z


def outer_4s_bottomright(m, x, i, j, k):
    """
    This is a 4-side touching, bottom-right different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i - 0, j - 1, k] \
        + m[i - 1, 3, 2] \
        + m[i - 0, j, k - 1] \
        + m[i - 1, 2, 3]

    z = bug_no_bug(x, count)

    return z


def outer_4s_topleft(m, x, i, j, k):
    """
    This is a 4-side touching, top-left different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i - 1, 1, 2] \
        + m[i - 0, j + 1, k] \
        + m[i - 1, 2, 1] \
        + m[i - 0, j, k + 1]

    z = bug_no_bug(x, count)

    return z


def outer_4s_topright(m, x, i, j, k):
    """
    This is a 4-side touching, top-right different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count \
        = m[i - 1, 1, 2] \
        + m[i - 0, j + 1, k] \
        + m[i - 0, j, k - 1] \
        + m[i - 1, 2, 3]

    z = bug_no_bug(x, count)

    return z


def inner_99(m, x, i, j, k):
    z = 99

    return z


layer_dict = {
    (0, 0): outer_4s_topleft,
    (0, 1): outer_4s_top,
    (0, 2): outer_4s_top,
    (0, 3): outer_4s_top,
    (0, 4): outer_4s_topright,

    (1, 0): outer_4s_left,
    (1, 1): inner_4s,
    (1, 2): inner_8s_top,
    (1, 3): inner_4s,
    (1, 4): outer_4s_right,

    (2, 0): outer_4s_left,
    (2, 1): inner_8s_left,
    (2, 2): inner_99,
    (2, 3): inner_8s_right,
    (2, 4): outer_4s_right,

    (3, 0): outer_4s_left,
    (3, 1): inner_4s,
    (3, 2): inner_8s_bottom,
    (3, 3): inner_4s,
    (3, 4): outer_4s_right,

    (4, 0): outer_4s_bottomleft,
    (4, 1): outer_4s_bottom,
    (4, 2): outer_4s_bottom,
    (4, 3): outer_4s_bottom,
    (4, 4): outer_4s_bottomright,
    }


def which_function(j, k):
    return layer_dict[(j, k)]


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
            # out.append('#' if layer[j, k] else '.')
        out += '\n'
        # out.append('\n')

    print(out)


def count_critters(m, layers_needed):
    count = 0
    for i in range(1, layers_needed - 1):
        for j in range(5):
            for k in range(5):
                if j == 2 and k == 2:
                    count += 0
                else:
                    count += m[i, j, k]
        # print(f"layer = {i}, Count = {count}")
                # print(f"layer = {i}, row = {j}, column = {k}, "
                #        f"m[{i}, {j}, {k}] = {m[i, j, k]}, Count = {count}")
    return count


def sum_top():
    pass


def sum_bottom():
    pass


def sum_right():
    pass


def sum_left():
    pass


def sum_5(matrix, plane, row, column, direction):
    if direction == 'across':
        x = functools.reduce(lambda x, y: x + y,
                             matrix[plane, row, column:column + 5])
    else:
        x = functools.reduce(lambda x, y: x + y,
                             matrix[plane, row:row + 5, column:column + 5])

    return x

matrix = np.zeros((5, 7, 7), int)
plane = 1


def handle_outer_padding(matrix, planes):
    for plane in range(1, planes - 1):
        matrix[plane, 0, 1:6] = matrix[plane - 1, 1, 2]
        # matrix[plane,0,1] = matrix[plane - 1, 1, 2]
        # matrix[plane,0,2] = matrix[plane - 1, 1, 2]
        # matrix[plane,0,3] = matrix[plane - 1, 1, 2]
        # matrix[plane,0,4] = matrix[plane - 1, 1, 2]
        # matrix[plane,0,5] = matrix[plane - 1, 1, 2]
        matrix[plane, 1:6, 1] = matrix[plane - 1, 2, 1]
        # matrix[plane,1,1] = matrix[plane - 1, 2, 1]
        # matrix[plane,2,1] = matrix[plane - 1, 2, 1]
        # matrix[plane,3,1] = matrix[plane - 1, 2, 1]
        # matrix[plane,4,1] = matrix[plane - 1, 2, 1]
        # matrix[plane,5,1] = matrix[plane - 1, 2, 1]
        matrix[plane, 6, 1:6] = matrix[plane - 1, 3, 2]
        # matrix[plane,6,1] = matrix[plane - 1, 3, 2]
        # matrix[plane,6,2] = matrix[plane - 1, 3, 2]
        # matrix[plane,6,3] = matrix[plane - 1, 3, 2]
        # matrix[plane,6,4] = matrix[plane - 1, 3, 2]
        # matrix[plane,6,5] = matrix[plane - 1, 3, 2]
        matrix[plane,1:6,6] = matrix[plane - 1, 2, 3]
        # matrix[plane,1,6] = matrix[plane - 1, 2, 3]
        # matrix[plane,2,6] = matrix[plane - 1, 2, 3]
        # matrix[plane,3,6] = matrix[plane - 1, 2, 3]
        # matrix[plane,4,6] = matrix[plane - 1, 2, 3]
        # matrix[plane,5,6] = matrix[plane - 1, 2, 3]

    return matrix


def check_adjacent_folding(mat, matrix, plane):
    z = np.zeros((7, 7), dtype=int)

    count_top = sum_5(matrix, plane + 1, 1, 1, 'across')
    count_bottom = sum_5(matrix, plane + 1, 6, 1, 'across')
    count_left = sum_5(matrix, plane + 1, 1, 1, 'down')
    count_right = sum_5(matrix, plane + 1, 1, 6, 'down')
    for row in range(1, 6):
        for column in range(1, 6):
            count = (mat[row - 1, column] +
                     mat[row + 1, column] +
                     mat[row, column - 1] +
                     mat[row, column + 1])

            z[row, column] = bug_no_bug(mat[row, column], count)

    return z


# %% Development Environment

txtfile = "../data/adventofcode_2019_day_24_input1.txt"
contents = aoc.read_program(txtfile)
eris_initiator = transform_program_5_x_5(contents)
# eris[0, 2, 2] = 99
minutes = 10

layers_needed = layers_at_minute(minutes)
initial_layer = ((layers_needed - 1) // 2)

# We are setting up the folded space matrix to have one extra layer at each
# end.  This way we can execute each layer using the same set of positional
# functions as opposed to writing inner layer functions and end layer ones.

eris = np.zeros((layers_needed, 5, 5), dtype='int16')
eris[initial_layer, :, :] = eris_initiator
len_eris = len(eris) - 2
eris_one_minute_later = np.zeros((layers_needed, 5, 5), dtype='int16')
eris_one_minute_later[initial_layer, :, :] = eris_initiator
# eris[0, 2, 2] = 1
# in2 = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0]).reshape((3, 3))
# print(eris[0, :, :])
# print(in2)

# p1 = sg.convolve2d(eris_initiator[0, :, :], in2, mode='same', boundary='fill', fillvalue=0)
# print(p1)

# print(f"\nMinute {0}:\n")
# print(f"Layer 0:")
# print(f"{matrix[initial_layer, :, :]}\n")


# for minute in range(1, minutes + 1):
#     eris_copy = eris.copy()
#     for layer in range(1, len_eris + 1):
#         for row in range(5):
#             for column in range(5):
#                 result = which_function(row, column)
#                 x = eris_copy[layer, row, column]
#                 args = [eris_copy, x, layer, row, column]
#                 eris_one_minute_later[layer, row, column] = result(*args)
#                 # if m == 2 and i == 1:
#                 #     print(f"Minute = {m}, "
#                 #           f"i = {1}, j = {j}, k = {k}\n"
#                 #           f"result = {result}\n"
#                 #           f"{eris[1, :, :]}\n"
#                 #           f"\n{eris_one_minute_later[1, :, :]}\n")
#     eris = eris_one_minute_later

# print(f"There are currently "
#       f"{count_critters(eris, layers_needed)}"
#       f" bugs present.")


def day24_part2(mat0, mat1, minutes, len_eris):
    for minute in range(1, minutes + 1):
        matrix_copy = mat0.copy()
        for layer in range(1, len_eris + 1):
            for row in range(5):
                for column in range(5):
                    result = which_function(row, column)
                    x = matrix_copy[layer, row, column]
                    args = [matrix_copy, x, layer, row, column]
                    mat1[layer, row, column] = result(*args)
                    # if m == 2 and i == 1:
                        # print(f"i = {1}, j = {j}, k = {k}\n"
                        #       f"result = {result}\n"
                        #       f"{eris[1, :, :]}\n"
                        #       f"\n{eris_one_minute_later[1, :, :]}\n")

        mat0 = mat1

    return mat0


    # print(f"\nMinute {m}:\n")
    # print(f"Layer 0:")
    # print(f"{matrix[initial_layer, :, :]}\n")
eris_200 = day24_part2(eris, eris_one_minute_later, minutes, len_eris)
print(f"There are currently "
      f"{count_critters(eris_200, layers_needed)} "
      f"bugs present.")

# print(f"\nMinute {m}:\n")
# test = '''
# def day24_part2(matrix, minutes):
#     for m in range(1, minutes + 1):
#         for i in range(1, len(matrix) - 1):
#             for j in range(5):
#                 for k in range(5):
#                     result = which_function(i, j)
#                     args = [matrix, matrix[i, j, k], i, j, k]
#                     matrix1[i, j, k] = result(*args)

#         matrix = matrix1

#     return matrix
# '''

# print(timeit.timeit(test))
# for i in range(1, len(matrix1) - 1):
for i in range(1, layers_needed - 1):
    print(f"Layer {i - (layers_needed - 1) // 2}:")
    print_layer(eris_200
                [i, :, :])

# for i in range(1, len_eris ++1):
#     print(np.array_equal(eris[i, :, :], eris_200[i, :, :]))


# set up total time-line 3-d matrix

# loop on time

# process outer padding

# process inner sums

# process each plane

# count critters



# %% Production Environment

# txtfile = "../data/adventofcode_2019_day_24_input.txt"
# contents = aoc.read_program(txtfile)
# eris = transform_program(contents)
# minutes = 50

# layer = day24_part1(eris, minutes)
# biodiversity_rating = biodiversity(layer)
# print(f"Day 24, Part 1 - Biodiversity rating = {biodiversity_rating}")


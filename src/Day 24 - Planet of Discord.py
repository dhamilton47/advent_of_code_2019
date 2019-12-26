# -*- coding: utf-8 -*-
"""
Created on Tue Dec  24 07:54:20 2019

@author: Dan J Hamilton
"""


import numpy as np
import functools


# %% Import the "XXXX" data (as a string)
def read_program(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    return contents


# %% Transform the "XXXX" from a string to a list
def transform_program(x):
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


def check_adjacent(mat):
    z = np.zeros((5, 5), dtype='int16')

    for i in range(5):
        for j in range(5):
            if mat[i, j] == 0:
                z = bug_born(mat, z, i, j)
            else:
                z[i, j] = 0

    for i in range(5):
        for j in range(5):
            if mat[i, j]:
                z = bug_dies(mat, z, i, j)

    return z


def bug_dies(mat, z, i, j):
    count = 0
    if j == 0:
        if mat[i, j + 1]:
            count += 1
    elif j == 4:
        if mat[i, j - 1]:
            count += 1
    else:
        if mat[i, j + 1]:
            count += 1
        if mat[i, j - 1]:
            count += 1

    if i == 0:
        if mat[i + 1, j]:
            count += 1
    elif i == 4:
        if mat[i - 1, j]:
            count += 1
    else:
        if mat[i - 1, j]:
            count += 1
        if mat[i + 1, j]:
            count += 1

    z[i, j] = 1 if count == 1 else 0

    return z


def bug_born(mat, z, i, j):
    count = 0
    if j == 0:
        count += 0
    else:
        if mat[i, j - 1]:
            count += 1

    if j == 4:
        count += 0
    else:
        if mat[i, j + 1]:
            count += 1

    if i == 0:
        count += 0
    else:
        if mat[i - 1, j]:
            count += 1

    if i == 4:
        count += 0
    else:
        if mat[i + 1, j]:
            count += 1

    z[i, j] = 1 if count == 1 or count == 2 else 0

    return z


def biodiversity(layout):
    power_matrix = [2 ** i for i in range(25)]
    power_matrix = np.array(power_matrix).reshape(1, 5, 5)

    x_product = np.multiply(power_matrix, layout).flatten()

    return functools.reduce(lambda a, b: a + b, x_product)


def day24_part1(dwarf_planet, minutes):
    for i in range(1, minutes):
        next_minute = check_adjacent(dwarf_planet[i - 1, :, :])
        next_minute = next_minute.reshape(1, 5, 5)
        dwarf_planet = np.concatenate((dwarf_planet, next_minute), axis=0)

        for j in range(i - 1):
            truthy = np.array_equal(dwarf_planet[i, :, :],
                                    dwarf_planet[j, :, :])
            if truthy:
                return dwarf_planet[i, :, :]


def dead_bug(x, count):
    # print(x, count)
    z = x
    if x == 1:
        z = 0 if count != 1 else 1
        # if count != 1:
        #     z = 0
        # else:
        #     z = 1

    return z


# def baby_bug(x, count):
def baby_bug(x, count):
    z = x
    if x == 0:
        z = 1 if (count == 1 or count == 2) else 0

       # if (count == 1 or count == 2):
        #     z = 1
        # else:
        #     z = 0

    return z


def bug_no_bug(x, count):
    if x == 1:
        z = 0 if count != 1 else 1

    if x == 0:
        z = 1 if (count == 1 or count == 2) else 0

    return z


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

    count = m[i, j - 1, k] \
        + m[i + 1, 0, 0] \
        + m[i + 1, 0, 1] \
        + m[i + 1, 0, 2] \
        + m[i + 1, 0, 3] \
        + m[i + 1, 0, 4] \
        + m[i, j, k - 1] \
        + m[i, j, k + 1]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

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

    count = m[i, j - 1, k] \
        + m[i, j + 1, k] \
        + m[i, j, k - 1] \
        + m[i + 1, 0, 0] \
        + m[i + 1, 1, 0] \
        + m[i + 1, 2, 0] \
        + m[i + 1, 3, 0] \
        + m[i + 1, 4, 0]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

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

    count = m[i, j - 1, k] \
        + m[i, j + 1, k] \
        + m[i + 1, 0, 4] \
        + m[i + 1, 1, 4] \
        + m[i + 1, 2, 4] \
        + m[i + 1, 3, 4] \
        + m[i + 1, 4, 4] \
        + m[i, j, k + 1]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)
    # print(f"level {i}, x = {x}, row = {j}, column = {k}, 4 count = {count}, z1 = {z}") 

    # new bug infestation?
    # z = baby_bug(x, count)
    # print(f"level {i}, x = {x}, row = {j}, column = {k}, 4 count = {count}, z2 = {z}\n") 

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

    count = m[i + 1, 4, 0] \
        + m[i + 1, 4, 1] \
        + m[i + 1, 4, 2] \
        + m[i + 1, 4, 3] \
        + m[i + 1, 4, 4] \
        + m[i, j + 1, k] \
        + m[i, j, k - 1] \
        + m[i, j, k + 1]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

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

    count = m[i, j - 1, k] \
        + m[i, j + 1, k] \
        + m[i, j, k - 1] \
        + m[i, j, k + 1]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)
    # print(f"level {i}, x = {x}, row = {j}, column = {k}, 4 count = {count}, z2 = {z}\n") 

    # new bug infestation?
    # z = baby_bug(x, count)
    # print(f"level {i}, x = {x}, row = {j}, column = {k}, 4 count = {count}, z1 = {z}") 

    return z


def inner_4s_top(m, x, i, j, k):
    """
    This is a 4-side touching, top-only different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count = m[i - 1, 1, 2] \
        + m[i, j + 1, k] \
        + m[i, j, k - 1] \
        + m[i, j, k + 1]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

    return z


def inner_4s_left(m, x, i, j, k):
    """
    This is a 4-side touching, left-only different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count = m[i, j - 1, k] \
        + m[i, j + 1, k] \
        + m[i - 1, 1, 2] \
        + m[i, j, k + 1]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

    return z


def inner_4s_right(m, x, i, j, k):
    """
    This is a 4-side touching, right-only different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count = m[i, j - 1, k] \
        + m[i, j + 1, k] \
        + m[i, j, k - 1] \
        + m[i - 1, 2, 3]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

    return z


def inner_4s_bottom(m, x, i, j, k):
    """
    This is a 4-side touching, bottom-only different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count = m[i, j - 1, k] \
        + m[i - 1, 3, 2] \
        + m[i, j, k - 1] \
        + m[i, j, k + 1]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

    return z


def inner_4s_bottomleft(m, x, i, j, k):
    """
    This is a 4-side touching, bottom-left different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count = m[i, j - 1, k] \
        + m[i - 1, 3, 2] \
        + m[i - 1, 2, 1] \
        + m[i, j, k + 1]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

    return z


def inner_4s_bottomright(m, x, i, j, k):
    """
    This is a 4-side touching, bottom-right different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count = m[i, j - 1, k] \
        + m[i - 1, 3, 2] \
        + m[i, j, k - 1] \
        + m[i - 1, 2, 3]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

    return z


def inner_4s_topleft(m, x, i, j, k):
    """
    This is a 4-side touching, top-left different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count = m[i - 1, 1, 2] \
        + m[i, j + 1, k] \
        + m[i - 1, 2, 1] \
        + m[i, j, k + 1]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)

    # new bug infestation?
    # z = baby_bug(x, count)

    return z


def inner_4s_topright(m, x, i, j, k):
    """
    This is a 4-side touching, top-right different level function

    m = the visible folding space
    i = the level of the folded space
    j = the width of level i
    k = the height of level i
    l = the +/- 1 level offset for the next level
    x = the location on the i, j, k plane we are interrogating
    """

    count = m[i - 1, 1, 3] \
        + m[i, j + 1, k] \
        + m[i, j, k - 1] \
        + m[i + 1, 2, 3]

    # Dead bug?
    z = bug_no_bug(x, count)
    # z = dead_bug(x, count)
    # print(f"count = {count}, x = {x}, z = {z}")


    # new bug infestation?
    # z = baby_bug(x, count)
    # print(f"count = {count}, x = {x}, z = {z}\n")

    return z


# def end_3s_t(m, x, i, j, k):
#     """
#     This is a 3-side touching, top, end function

#     m = the visible folding space
#     i = the level of the folded space
#     j = the width of level i
#     k = the height of level i
#     l = the +/- 1 level offset for the next level
#     x = the location on the i, j, k plane we are interrogating
#     """

#     count = m[i, j, k - 1] + m[i, j, k + 1] + m[i, j + 1, k]

#     # new bug infestation?
#     z = baby_bug(x, count)

#     # Dead bug?
#     z = dead_bug(x, count)

#     return z


# def end_3s_r(m, x, i, j, k):
#     """
#     This is a 3-side touching, right, end function

#     m = the visible folding space
#     i = the level of the folded space
#     j = the width of level i
#     k = the height of level i
#     l = the +/- 1 level offset for the next level
#     x = the location on the i, j, k plane we are interrogating
#     """

#     count = m[i, j - 1, k] + m[i, j + 1, k] + m[i, j, k - 1]

#     # new bug infestation?
#     z = baby_bug(x, count)

#     # Dead bug?
#     z = dead_bug(x, count)

#     return z


# def end_3s_l(m, x, i, j, k):
#     """
#     This is a 3-side touching, left, end function

#     m = the visible folding space
#     i = the level of the folded space
#     j = the width of level i
#     k = the height of level i
#     l = the +/- 1 level offset for the next level
#     x = the location on the i, j, k plane we are interrogating
#     """

#     count = m[i, j - 1, k] + m[i, j + 1, k] + m[i, j, k + 1]

#     # new bug infestation?
#     z = baby_bug(x, count)

#     # Dead bug?
#     z = dead_bug(x, count)

#     return z


# def end_3s_b(m, x, i, j, k):
#     """
#     This is a 3-side touching, bottom, end function

#     m = the visible folding space
#     i = the level of the folded space
#     j = the width of level i
#     k = the height of level i
#     l = the +/- 1 level offset for the next level
#     x = the location on the i, j, k plane we are interrogating
#     """

#     count = m[i, j, k - 1] + m[i, j, k + 1] + m[i, j - 1, k]

#     # new bug infestation?
#     z = baby_bug(x, count)

#     # Dead bug?
#     z = dead_bug(x, count)

#     return z


# def end_2s_tl(m, x, i, j, k):
#     """
#     This is a 2-side touching, top-left, end function

#     m = the visible folding space
#     i = the level of the folded space
#     j = the width of level i
#     k = the height of level i
#     l = the +/- 1 level offset for the next level
#     x = the location on the i, j, k plane we are interrogating
#     """

#     count = m[i, j + 1, k] + m[i, j, k + 1]

#     # new bug infestation?
#     z = baby_bug(x, count)

#     # Dead bug?
#     z = dead_bug(x, count)

#     return z


# def end_2s_tr(m, x, i, j, k):
#     """
#     This is a 2-side touching, top-right, end function

#     m = the visible folding space
#     i = the level of the folded space
#     j = the width of level i
#     k = the height of level i
#     l = the +/- 1 level offset for the next level
#     x = the location on the i, j, k plane we are interrogating
#     """

#     count = m[i, j + 1, k] + m[i, j, k - 1]

#     # new bug infestation?
#     z = baby_bug(x, count)

#     # Dead bug?
#     z = dead_bug(x, count)

#     return z


# def end_2s_bl(m, x, i, j, k):
#     """
#     This is a 2-side touching, bottom-right, end function

#     m = the visible folding space
#     i = the level of the folded space
#     j = the width of level i
#     k = the height of level i
#     l = the +/- 1 level offset for the next level
#     x = the location on the i, j, k plane we are interrogating
#     """

#     count = m[i, j - 1, k] + m[i, j, k + 1]

#     # new bug infestation?
#     z = baby_bug(x, count)

#     # Dead bug?
#     z = dead_bug(x, count)

#     return z


# def end_2s_br(m, x, i, j, k):
#     """
#     This is a 2-side touching, bottom-left, end function

#     m = the visible folding space
#     i = the level of the folded space
#     j = the width of level i
#     k = the height of level i
#     l = the +/- 1 level offset for the next level
#     x = the location on the i, j, k plane we are interrogating
#     """

#     count = m[i, j, k - 1] + m[i, j - 1, k]

#     # new bug infestation?
#     z = baby_bug(x, count)

#     # Dead bug?
#     z = dead_bug(x, count)

#     return z


def inner_99(m, x, i, j, k):
    z = 99

    return z


layer_dict = {
    ('i', 0, 0): inner_4s_topleft,
    ('i', 0, 1): inner_4s_top,
    ('i', 0, 2): inner_4s_top,
    ('i', 0, 3): inner_4s_top,
    ('i', 0, 4): inner_4s_topright,

    ('i', 1, 0): inner_4s_left,
    ('i', 1, 1): inner_4s,
    ('i', 1, 2): inner_8s_top,
    ('i', 1, 3): inner_4s,
    ('i', 1, 4): inner_4s_right,

    ('i', 2, 0): inner_4s_left,
    ('i', 2, 1): inner_8s_left,
    ('i', 2, 2): inner_99,
    ('i', 2, 3): inner_8s_right,
    ('i', 2, 4): inner_4s_right,

    ('i', 3, 0): inner_4s_left,
    ('i', 3, 1): inner_4s,
    ('i', 3, 2): inner_8s_bottom,
    ('i', 3, 3): inner_4s,
    ('i', 3, 4): inner_4s_right,

    ('i', 4, 0): inner_4s_bottomleft,
    ('i', 4, 1): inner_4s_bottom,
    ('i', 4, 2): inner_4s_bottom,
    ('i', 4, 3): inner_4s_bottom,
    ('i', 4, 4): inner_4s_bottomright,
    }


def which_function(i, j):
    return layer_dict[('i', j, k)]


# %% Development Environment

txtfile = "../data/adventofcode_2019_day_24_input1.txt"
contents = read_program(txtfile)
eris = transform_program(contents)
eris[0, 2, 2] = 99
minutes = 1


def layers_at_minute(x):
    return 3 + 2 * ((x % 2) + (x // 2))

layers_needed = layers_at_minute(minutes)
# print(timeperiod(0))
# print(timeperiod(1))
# print(timeperiod(2))
# print(timeperiod(3))
# print(timeperiod(4))
# print(timeperiod(5))
# print(timeperiod(6))
# print(timeperiod(7))
# print(timeperiod(8))
# print(timeperiod(9))
# print(timeperiod(10))





# layer = day24_part1(eris, minutes)
# biodiversity_rating = biodiversity(layer)
# print(f"Day 24, Part 1 - Biodiversity rating = {biodiversity_rating}")

# We are setting up the folded space matrix to have one extra layer at each
# end.  This way we can execute each layer using the same set of positional
# functions as opposed to writing inner layer functions and end layer ones.

matrix = np.zeros((layers_needed, 5, 5), dtype='int16')
initial_layer = ((layers_needed - 1) // 2)
matrix[initial_layer, :, :] = eris
len_matrix = len(matrix) - 2

matrix1 = np.zeros((layers_needed, 5, 5), dtype='int16')
matrix1[initial_layer, :, :] = eris

# print(f"\nMinute {0}:\n")
# print(f"Layer 0:")
# print(f"{matrix[initial_layer, :, :]}\n")


# print(f"Layer 3:")
# print(f"{matrix[2, :, :]}\n")
# print(f"Layer 4:")
# print(f"{matrix[3, :, :]}\n")

# for m in range(1, minutes + 1):
#     for i in range(len(matrix)):
for m in range(1, minutes + 1):
    for i in range(1, len(matrix) - 1):
        for j in range(5):
            for k in range(5):
                # if j == 2 and k == 2:
                #     matrix[i, 2, 2] = 
                #     continue
                result = which_function(i, j)
                # print(result)
                args = [matrix, matrix[i, j, k], i, j, k]
                matrix1[i, j, k] = result(*args)
                # print(f"minute {m}, layer {i}, row {j}, column {k} = {matrix[i, j, k]}")
    matrix = matrix1
    # print(f"\nMinute {m}:\n")
    # print(f"Layer 2:")
    # print(f"{matrix[1, :, :]}\n")
    # print(f"Layer 0:")
    # print(f"{matrix[initial_layer, :, :]}\n")
    # print(f"Layer 4:")
    # print(f"{matrix[3, :, :]}\n")

# print(f"\nMinute {m}:\n")

# print(f"Layer -5:")
# print(f"{matrix[1, :, :]}\n")
# print(f"Layer -4:")
# print(f"{matrix[2, :, :]}\n")
# print(f"Layer -3:")
# print(f"{matrix[3, :, :]}\n")
# print(f"Layer -2:")
# print(f"{matrix[4, :, :]}\n")
# print(f"Layer -1:")
# print(f"{matrix[5, :, :]}\n")
# print(f"Layer 0:")
# print(f"{matrix[6, :, :]}\n")
# print(f"Layer 1:")
# print(f"{matrix[7, :, :]}\n")
# print(f"Layer 2:")
# print(f"{matrix[8, :, :]}\n")
# print(f"Layer 3:")
# print(f"{matrix[9, :, :]}\n")
# print(f"Layer 4:")
# print(f"{matrix[10, :, :]}\n")
# print(f"Layer 5:")
# print(f"{matrix[11, :, :]}\n")
    
    
# for i in range(1, len(matrix1) - 1):
for i in range(1, layers_needed - 1):
    print(f"Layer {i - (layers_needed - 1) // 2}:")
    print(f"{matrix[i, :, :]}\n")

# %% Production Environment

# txtfile = "../data/adventofcode_2019_day_24_input.txt"
# contents = read_program(txtfile)
# eris = transform_program(contents)
# minutes = 50

# layer = day24_part1(eris, minutes)
# biodiversity_rating = biodiversity(layer)
# print(f"Day 24, Part 1 - Biodiversity rating = {biodiversity_rating}")

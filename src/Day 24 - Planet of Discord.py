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


# %% Development Environment

# txtfile = "../data/adventofcode_2019_day_24_input.txt"
# contents = read_program(txtfile)
# eris = transform_program(contents)
# minutes = 50

# layer = day24_part1(eris, minutes)
# biodiversity_rating = biodiversity(layer)
# print(f"Day 24, Part 1 - Biodiversity rating = {biodiversity_rating}")

# %% Production Environment

txtfile = "../data/adventofcode_2019_day_24_input.txt"
contents = read_program(txtfile)
eris = transform_program(contents)
minutes = 50

layer = day24_part1(eris, minutes)
biodiversity_rating = biodiversity(layer)
print(f"Day 24, Part 1 - Biodiversity rating = {biodiversity_rating}")

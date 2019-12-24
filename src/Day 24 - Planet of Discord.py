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
#    memory_length = len(memory)
    y = []
    for i in x:
        if i == '.':
            y.append(0)
        elif i == '#':
            y.append(1)
        else:
            continue
#        memory[i] = int(memory[i])

    eris = np.array(y, dtype='int16').reshape(1, 5, 5)

    return eris

def check_adjacent(mat):
    count = 0
    z = np.zeros((5, 5), dtype='int16')
    
    for i in range(5):
        for j in range(5):
            if mat[i, j] == 0:
                z = bug_born(mat, z, i, j)
            else:
                z[i, j] = 0
            # if mat[i, j] == 0:
            #     if mat[i, j - 1]:
            #         count += 1
            #     if mat[i - 1, j]:
            #         count += 1
            #     if mat[i, j + 1]:
            #         count += 1
            #     if mat[i + 1, j]:
            #         count += 1

            # if count == 2 or count:
            #     z[0, i, j] = count

    for i in range(5):
        for j in range(5):
            if mat[i, j]:
                z = bug_dies(mat, z, i, j)
            # if mat[i, j]:
    #         #     if mat[i, j - 1]:
    #         #         count += 1
    #         #     if mat[i - 1, j]:
    #         #         count += 1
    #         #     if mat[i, j + 1]:
    #         #         count += 1
    #         #     if mat[i + 1, j]:
    #         #         count += 1

    #         if count:
    #             z[0, i, j] = count

    return z


def bug_dies(mat, z, i, j):
    count = 0
    # if mat[i, j]:
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

    # print(f"Dies: {i},{j} = {count}")
    if count == 1:
        z[i, j] = 1
    else:
        z[i, j] = 0

    return z


def bug_born(mat, z, i, j):
    count = 0
    # if mat[i, j] == 0:
    if j == 0:
        count += 0
    else:
        if mat[i, j - 1]:
            count += 1
        # else:
        #     count

    if j == 4:
        count += 0
    else:
        if mat[i, j + 1]:
            count += 1
        # else:
        #     count

    if i == 0:
        count += 0
    else:
        if mat[i - 1, j]:
            count += 1
        # else:
        #     count

    if i == 4:
        count += 0
    else:
        if mat[i + 1, j]:
            count += 1
        # else:
        #     count

    # print(f"Born: {i},{j} = {count}")
    if count == 1 or count == 2:
        z[i, j] = 1
    else:
        z[i, j] = 0

    return z


# %% Development Environment

txtfile = "../data/adventofcode_2019_day_24_input.txt"
contents = read_program(txtfile)
eris = transform_program(contents)
minutes = 50
truth = []
for i in range(1, minutes):
    next_eris = check_adjacent(eris[i - 1, :, :])
    next_eris = next_eris.reshape(1, 5, 5)
    eris = np.concatenate((eris, next_eris), axis=0)

    for j in range(i - 1):
        truthy = np.array_equal(eris[i, :, :], eris[j, :, :])
        if truthy:
            truth.append((i, j))
            break

biodiversity_rating = [2 ** i for i in range(25)]
biodiversity_rating = np.array(biodiversity_rating).reshape(1, 5, 5)
print(np.multiply(biodiversity_rating, eris[44, :, :]))
x = np.multiply(biodiversity_rating, eris[44, :, :]).flatten()

y = functools.reduce(lambda a, b: a + b, x)
print(y)

# %% Production Environment

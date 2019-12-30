# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

# if two or more points share the same angle (theta) from a given point,
# then points beyond the closest on that angle are blocked


import pandas as pd
import math

import aoc


# %% Transform the "XXXX" from a string to a list
def transform_program(contents):
    memory = list(contents.split("\n"))
    height = len(memory)
    width = validate(memory)

    table = []
    for i in memory:
        row = []
        for j in range(width):
            row.append(i[j])
        table.append(row)
    return table, height, width


def validate(data):
    width = len(data[0])
    for i in range(len(data)):
        if width != len(data[i]):
            raise Exception('Corrupt Data - lines of differing length')

    return width


def point(x, y):
    return [x, y]


def distance(pt1, pt2):
    dx = pt2[1] - pt1[1]
    dy = pt2[0] - pt1[0]

    return dx, dy, (dy ** 2 + dx ** 2) ** 0.5


def locate_asteroids(table, h, w):
    '''
    Create a list of asteroid cartesian points from an import source

    table = transformed import source
    h, w = height, width of the table
    '''

    lst = []

    for j in range(h):
        for i in range(w):
            if table[j][i] == '#':
                lst.append(point(i, j))

    return lst


def other_asteroids(a, i):
    '''
    Take one down. Pass it around. 99 bottles of..

    Create a list of remaining asteroids after choosing one as a test base

    a = complete list of asteroids
    i = asteroid chosen as test base
    '''

    x = []
    for y in range(len(a)):
        if a[y] != i:
            x.append(a[y])
    return x

# %%


def number_of_asteroids_seen_from_a_given_asteroid(remaining_asteroids, base):
    '''
    Return the count of asteroids which can been seen from a test asteroid.

    remaining_asteroids = complete list of asteroids after removing the test
        asteroid
    base = asteroid chosen as test base
    '''

    thetas = []
    rs = []

    for i in remaining_asteroids:
        dx, dy, r = distance(i, base)
        thetas.append(math.atan2(dy, dx))
        rs.append(r)

    count = len(set(sorted(thetas)))

    return count


def how_well_can_i_see(asteroids):
    '''
    From a set of asteroids, determine the one with the maximum view of
    other asteroids  This asteroid will be the new base.

    asteroids = complete list of asteroids
    '''

    max_seen = 0
    where_seen = []

    for item in asteroids:
        remaining_asteroids = other_asteroids(asteroids, item)
        seen = number_of_asteroids_seen_from_a_given_asteroid(
            remaining_asteroids, item)

        if seen > max_seen:
            max_seen = seen
            where_seen = item

    return max_seen, where_seen


# %%


def asteroids_seen_from_new_base(remaining_asteroids, base):
    '''
    Return the angle (theta) and distance (r) of asteroids which can been
    seen from the new base.

    remaining_asteroids = complete list of asteroids after removing the test
        asteroid
    base = asteroid chosen as test base
    '''

    thetas = []
    dxs = []
    dys = []
    rs = []

    for i in remaining_asteroids:
        dx, dy, r = distance(i, base)
        dxs.append(dx)
        dys.append(dy)
        thetas.append(math.atan2(dy, dx))
        rs.append(r)

    dx = pd.Series(dxs, name='dx')
    dy = pd.Series(dys, name='dy')
    theta = pd.Series(thetas, name='theta')
    r = pd.Series(rs, name='radius')

    df = pd.DataFrame()
    df['point'] = remaining_asteroids
    df['dx'] = dx
    df['dy'] = dy
    df['theta'] = theta
    df['radius'] = r

    return df

# %%


def best_base(txtfile):
    # Preprocess data
    contents = aoc.read_program(txtfile)
    table, height, width = transform_program(contents)

    # Locate asteroids
    asteroids = locate_asteroids(table, height, width)

    # Calculate maximum number of visible asteroids from the best base location
    max_seen, where_seen = how_well_can_i_see(asteroids)

    print('Day 10, Part 1 - Max asteroids visible = {} from asteroid at {}'
          .format(max_seen, where_seen))

    return max_seen, where_seen

# %%


def blast_rotation(txtfile):
    # Preprocess data
    contents = aoc.read_program(txtfile)
    table, height, width = transform_program(contents)

    # Locate asteroids
    asteroids = locate_asteroids(table, height, width)

    # Calculate maximum number of visible asteroids from the best base location
    max_seen, where_seen = how_well_can_i_see(asteroids)

    # create vector of the seen asteroid locations from the new base
    remaining_asteroids = other_asteroids(asteroids, where_seen)
    lst = asteroids_seen_from_new_base(remaining_asteroids, where_seen)
    lst = lst.loc[lst.groupby('theta')['radius'].idxmin()]

    # Sort the vector to enable visual determination of Part 2 answer
    lst = lst.sort_values('theta').reset_index()

    return lst

# %% Development Environment
# txtfile = "../data/adventofcode_2019_day_10_input.txt"
# contents = aoc.read_program(txtfile)
# table, height, width = transform_program(contents)

# asteroids = locate_asteroids(table, height, width)
# # Convert cartesian to polar coordinates

# # r = (x ** 2 + y ** 2) ** 0.5
# # theta = tan-1 (y / x)

# # Use Math.atan2(x,y) to determine angle in correct quadrant

# # ds = []
# # thetas = []

# # number_of_visible_asteroids = how_well_can_i_see(asteroids)
# # print('Maximum number of visible asteroids = {}'
# #       .format(number_of_visible_asteroids))

# # txtfile = "../data/adventofcode_2019_day_10a_input.txt"
# max_seen, where_seen = best_base(txtfile)

# remaining_asteroids = other_asteroids(asteroids, where_seen)

# lst1 = asteroids_seen_from_new_base(remaining_asteroids, where_seen)
# # lst3 = [item - math.pi / 2 for item in lst1]

# x = lst1.loc[lst1.groupby('theta')['radius'].idxmin()]
# xindex = x.index
# lst2 = lst1.drop(xindex[:], axis=0)
# lst3 = x.sort_values('theta').reset_index()

# %% Production Environment


txtfile = "../data/AoC2019_day_10_input.txt"
answer = best_base(txtfile)
answer2 = blast_rotation(txtfile)

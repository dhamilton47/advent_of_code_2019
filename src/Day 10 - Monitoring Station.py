# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

# if two or more points share the same angle (theta) from a given point,
# then points beyond the closest on that angle are blocked


# import pandas as pd
import math


# %% Import the data (as a matrix)


def read_program(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    return contents


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
    dy = pt2[1] - pt1[1]
    dx = pt2[0] - pt1[0]

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
    x = []
    for y in range(len(a)):
        if a[y] != i:
            x.append(a[y])

    return x


def number_of_asteroids_seen_from_a_given_asteroid(remaining_asteroids, base):
    ds = []
    thetas = []

    for i in remaining_asteroids:
        dx, dy, d = distance(i, base)
        ds.append(d)
        thetas.append(math.atan2(dy, dx))
        count = len(set(sorted(thetas)))

    return count


def how_well_can_i_see(asteroids):
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


def best_base(txtfile):
    # Preprocess data
    contents = read_program(txtfile)
    table, height, width = transform_program(contents)

    # Locate asteroids
    asteroids = locate_asteroids(table, height, width)

    # Calculate maximum number of visible asteroids from the best base location
    max_seen, where_seen = how_well_can_i_see(asteroids)

    print('Day 10, Part 1 - Max asteroids visible = {} from asteroid at {}'
          .format(max_seen, where_seen))


# %% Development Environment
# txtfile = "../data/adventofcode_2019_day_10_input.txt"
# contents = read_program(txtfile)
# table, height, width = transform_program(contents)

# asteroids = locate_asteroids(table, height, width)

# Convert cartesian to polar coordinates

# r = (x ** 2 + y ** 2) ** 0.5
# theta = tan-1 (y / x)

# Use Math.atan2(x,y) to determine angle in correct quadrant

# ds = []
# thetas = []

# number_of_visible_asteroids = how_well_can_i_see(asteroids)
# print('Maximum number of visible asteroids = {}'
#       .format(number_of_visible_asteroids))

# txtfile = "../data/adventofcode_2019_day_10_input.txt"
# answer = best_base(txtfile)    
# %% Production Environment

txtfile = "../data/adventofcode_2019_day_10a_input.txt"
answer = best_base(txtfile)

txtfile = "../data/adventofcode_2019_day_10b_input.txt"
answer = best_base(txtfile)

txtfile = "../data/adventofcode_2019_day_10c_input.txt"
answer = best_base(txtfile)

txtfile = "../data/adventofcode_2019_day_10d_input.txt"
answer = best_base(txtfile)

txtfile = "../data/adventofcode_2019_day_10_input.txt"
answer = best_base(txtfile)

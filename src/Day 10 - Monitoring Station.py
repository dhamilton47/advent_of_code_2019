# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

# if two or more points share the same slople from a given point, then points
# beyond the closest are blocked

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

#    memory_length = len(memory)
#    for i in range(memory_length):
#        memory[i] = int(memory[i])


def validate(data):
    width = len(data[0])
    for i in range(len(data)):
        if width != len(data[i]):
            raise Exception('Corrupt Data - lines of differing length')

    return width


def point(x, y):
    return [x, y]


def slope(pt1, pt2):
    dy = pt2[1] - pt1[1]
    dx = pt2[0] - pt1[0]
    return dy / dx if dx else float("inf")


def distance(pt1, pt2):
    dy = pt2[1] - pt1[1]
    dx = pt2[0] - pt1[0]
    return (dy ** 2 + dx ** 2) ** 0.5


def slope_intercept(pt1, pt2):
    a = slope(pt1, pt2)
    b = a * pt1[0] - pt1[1]

    return b


def unique(lst):
    unique_lst = []
    for x in lst:
        if x not in unique_lst:
            unique_lst.append(x)

    # print(unique_lst)
    # print(len(unique_lst))
    return len(unique_lst)


def locate_asteroids(table, height, width):
    asteroids = []

    for j in range(height):
        for i in range(width):
            if table[j][i] == '#':
                asteroids.append(point(i, j))

    return asteroids


def other_asteroids(a, i):
    x = []
    for y in range(len(a)):
        if a[y] != i:
            x.append(a[y])

    return x


def calculate_slopes_matrix(asteroids):
    slopes_matrix = []

    for i in asteroids:
        slopes = []
        asteroids1 = other_asteroids(asteroids, i)
        for j in asteroids1:
            slopes.append(slope(i, j))

        slopes_matrix.append(slopes)

    return slopes_matrix


def unique_slopes_counts(slopes_matrix):
    unique_counts = []

    for i in slopes_matrix:
        unique_counts.append(unique(i))

    return unique_counts


def best_base(txtfile):
    # Preprocess data
    contents = read_program(txtfile)
    table, height, width = transform_program(contents)

    # Locate asteroids
    asteroids = locate_asteroids(table, height, width)

    # Calculate slopes vector for each asteroid
    slopes_matrix = calculate_slopes_matrix(asteroids)

    # Detemine number of unique slope values for each asteroid
    unique_counts = unique_slopes_counts(slopes_matrix)

    print('Day 10, Part 1 - Max asteroids visible = {}'
          .format(max(unique_counts)))


# %% Development Environment
txtfile = "../data/adventofcode_2019_day_10a_input.txt"
contents = read_program(txtfile)
table, height, width = transform_program(contents)
# height = len(transformed_contents)
# width = len(transformed_contents[0])

# set asteroid list
asteroids = []

for j in range(height):
    for i in range(width):
        if table[j][i] == '#':
            asteroids.append(point(i, j))

base = [5, 8]
asteroids1 = other_asteroids(asteroids, base)


slopes = []
distances = []
for j in asteroids1:
    # print('i = {}, j = {}, slope = {}'
    #       .format(asteroids[0], j, slope(asteroids[0], j)))
    # slopes.append(slope([5, 8], j))
    slopes.append(slope(base, j))
    distances.append(distance(base, j))


# number_of_visible_asteroids = 0
# slopes_matrix = []
# distances_matrix = []
# for i in asteroids:
#     slopes = []
#     distances = []
# #    asteroids1 = build_phase_choices(asteroids, [5, 8])
#     asteroids1 = other_asteroids(asteroids, i)
#     for j in asteroids1:
#         # print('i = {}, j = {}, slope = {}'
#         #       .format(asteroids[0], j, slope(asteroids[0], j)))
#         # slopes.append(slope([5, 8], j))
#         slopes.append(slope(i, j))
#         distances.append(distance(i, j))
#     slopes_matrix.append(slopes)
#     distances_matrix.append(distances)

#     # print('i = {}, seen = {}'
#     #       .format(i, unique(slopes)))

# unique_count = []
# for i in slopes_matrix:
#     unique_count.append(unique(i))
#     # if unique(slopes) > number_of_visible_asteroids:
#     #     number_of_visible_asteroids = unique(slopes)
#     #     # print('i = {}, j = {}, seen = {}'
#     #     #       .format(asteroids[0], j, number_of_visible_asteroids))
#     #     point = i

# print('Maximum number of visible asteroids = {} at point {}'
#       .format(number_of_visible_asteroids, point))

# %% Production Environment

# txtfile = "../data/adventofcode_2019_day_10a_input.txt"
# answer = best_base(txtfile)

# txtfile = "../data/adventofcode_2019_day_10b_input.txt"
# answer = best_base(txtfile)

# txtfile = "../data/adventofcode_2019_day_10c_input.txt"
# answer = best_base(txtfile)

# txtfile = "../data/adventofcode_2019_day_10d_input.txt"
# answer = best_base(txtfile)

# txtfile = "../data/adventofcode_2019_day_10_input.txt"
# answer = best_base(txtfile)

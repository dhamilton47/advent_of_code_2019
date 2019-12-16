# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from itertools import groupby


# Given the positions of the 4 largest moons of Jupiter and starting velocity
# vectors for each of zero, calculate the motionsof the moons in time steps.

# For each step:
# 1. Update the velocity vector for the effect of gravity. v(x, y, z)
# 2. Update position by applying velocity. p(x, y, z)
# 3.Time progresses by one step.

# To apply gravity, consider every pair of moons.  Each velocity axis of
# each moon changes +/- 1 to pull each moon together based on comparison of
# their respective position axes.  If a pair of moons has equal positional
# axis values, that axis does not change.

# Updating position is simply position beginning plus updated velocity.

# Total energy calculation:
# 1. Per moon = potential energy times kinetic energy.
# 2. Potential energy = |p(x)| + |p(y)| + |p(z)|
# 3. Kinetic energy = |v(x)| + |v(y)| + |v(z)|

# %% Functions
def read_program(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    return contents



def transform_program(contents):
    for item in ['<', '>', '=', 'x', 'y', 'z', ',']:
        contents = [''.join(j).strip(item) for sub in contents
                    for k, j in groupby(sub, str.isdigit)]

    memory = str(''.join(contents)).replace('\n', ' ').split(' ')
    return [int(item) for item in memory]


def convert_moon_list_to_dictionary(transformed_contents):
    for i in range(4):
        for j in range(3):
            y = (3 * i) + j
            moons[i][0][j] = transformed_contents[y]


def print_format(moons, time_steps):
    pos = ['0', '1', '2', '3', '4', '5']
    num = ': 3d}'

    format_string0 = 'x={' + pos[0] + num \
        + ', y={' + pos[1] + num \
        + ', z={' + pos[2] + num
    format_string1 = 'x={' + pos[3] + num \
        + ', y={' + pos[4] + num \
        + ', z={' + pos[5] + num
    format_string2 = ' pos=<' + format_string0 \
        + '>, vel=<' + format_string1 + '>'

    print('Time step {}'.format(time_steps))

    print(('Io:\t\t' + format_string2)
          .format(moons[0][0][0], moons[0][0][1], moons[0][0][2],
                  moons[0][1][0], moons[0][1][1], moons[0][1][2]))
    print(('Europa:\t\t' + format_string2)
          .format(moons[1][0][0], moons[1][0][1], moons[1][0][2],
                  moons[1][1][0], moons[1][1][1], moons[1][1][2]))
    print(('Ganymede:\t' + format_string2)
          .format(moons[2][0][0], moons[2][0][1], moons[2][0][2],
                  moons[2][1][0], moons[2][1][1], moons[2][1][2]))
    print(('Callisto:\t' + format_string2)
          .format(moons[3][0][0], moons[3][0][1], moons[3][0][2],
                  moons[3][1][0], moons[3][1][1], moons[3][1][2]))

    print()


def gravity_effect_per_pair(a, b):
    for i in range(3):
        if a[0][i] > b[0][i]:
            a[1][i] -= 1
            b[1][i] += 1
        elif a[0][i] < b[0][i]:
            a[1][i] += 1
            b[1][i] -= 1
        else:
            return


def gravity_effects_per_step(moon_pairs, moons):
    for moon_pair in moon_pairs:
        moon1 = moons[moon_pair[0]]
        moon2 = moons[moon_pair[1]]
        gravity_effect_per_pair(moon1, moon2)


def position_at_end_of_time_step(moons):
    for moon in range(4):
        for axis in range(3):
            moons[moon][0][axis] = moons[moon][0][axis] + moons[moon][1][axis]


# %%  Set up variables

moon_names = {0: 'Io', 2: 'Europa', 3: 'Ganymede', 4: 'Callisto'}

vector_names = {0: 'pos', 1: 'vel'}

vector_axes = {0: 'x', 1: 'y', 2: 'z'}

moons = {0: {0: {0: 0, 1: 0, 2: 0},
             1: {0: 0, 1: 0, 2: 0}},
         1: {0: {0: 0, 1: 0, 2: 0},
             1: {0: 0, 1: 0, 2: 0}},
         2: {0: {0: 0, 1: 0, 2: 0},
             1: {0: 0, 1: 0, 2: 0}},
         3: {0: {0: 0, 1: 0, 2: 0},
             1: {0: 0, 1: 0, 2: 0}}}

pairs = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

# moons1 = {'Io': {'pos': {'x': 0, 'y': 0, 'z': 0},
#                 'vel': {'x': 0, 'y': 0, 'z': 0}},
#          'Europa': {'pos': {'x': 0, 'y': 0, 'z': 0},
#                     'vel': {'x': 0, 'y': 0, 'z': 0}},
#          'Ganymede': {'pos': {'x': 0, 'y': 0, 'z': 0},
#                       'vel': {'x': 0, 'y': 0, 'z': 0}},
#          'Callisto': {'pos': {'x': 0, 'y': 0, 'z': 0},
#                       'vel': {'x': 0, 'y': 0, 'z': 0}}}

# for i, item in enumerate(['Io', 'Europa', 'Ganymede', 'Callisto']):
#     for j, item1 in enumerate(['x', 'y', 'z']):
#         y = (3 * i) + j
#         moons[item]['pos'][item1] = transformed_contents[y]



# for i in range(4):
#     for j in range(3):
#         y = (3 * i) + j
#         moons[i][0][j] = transformed_contents[y]
        
# pos = ['0', '1', '2', '3', '4', '5']
# num = ': 3d}'

# format_string0 = 'x={' + pos[0] + num \
#     + ', y={' + pos[1] + num \
#     + ', z={' + pos[2] + num
# format_string1 = 'x={' + pos[3] + num \
#     + ', y={' + pos[4] + num \
#     + ', z={' + pos[5] + num
# format_string2 = ' pos=<' + format_string0 + '>, vel=<' + format_string1 + '>'

# # Moons we are tracking:
# print(('Io:\t\t' + format_string2)
#       .format(moons['Io']['pos']['x'],
#               moons['Io']['pos']['y'],
#               moons['Io']['pos']['z'],
#               moons['Io']['vel']['x'],
#               moons['Io']['vel']['y'],
#               moons['Io']['vel']['z']))
# print(('Europa:\t\t' + format_string2)
#       .format(moons['Europa']['pos']['x'],
#               moons['Europa']['pos']['y'],
#               moons['Europa']['pos']['z'],
#               moons['Europa']['vel']['x'],
#               moons['Europa']['vel']['y'],
#               moons['Europa']['vel']['z']))
# print(('Ganymede:\t' + format_string2)
#       .format(moons['Ganymede']['pos']['x'],
#               moons['Ganymede']['pos']['y'],
#               moons['Ganymede']['pos']['z'],
#               moons['Ganymede']['vel']['x'],
#               moons['Ganymede']['vel']['y'],
#               moons['Ganymede']['vel']['z']))
# print(('Callisto:\t' + format_string2)
#       .format(moons['Callisto']['pos']['x'],
#               moons['Callisto']['pos']['y'],
#               moons['Callisto']['pos']['z'],
#               moons['Callisto']['vel']['x'],
#               moons['Callisto']['vel']['y'],
#               moons['Callisto']['vel']['z']))


# Moons we are tracking:
# print(('Io:\t\t' + format_string2)
#       .format(moons[0][0][0], moons[0][0][1], moons[0][0][2],
#               moons[0][1][0], moons[0][1][1], moons[0][1][2])) 
# print(('Europa:\t\t' + format_string2)
#       .format(moons[1][0][0], moons[1][0][1], moons[1][0][2],
#               moons[1][1][0], moons[1][1][1], moons[1][1][2]))
# print(('Ganymede:\t' + format_string2)
#       .format(moons[2][0][0], moons[2][0][1], moons[2][0][2],
#               moons[2][1][0], moons[2][1][1], moons[2][1][2]))
# print(('Callisto:\t' + format_string2)
#       .format(moons[3][0][0], moons[3][0][1], moons[3][0][2],
#               moons[3][1][0], moons[3][1][1], moons[3][1][2]))


# %%


# update velocity

# %% Development Environment

txtfile = "../data/adventofcode_2019_day_12a_input.txt"
contents = read_program(txtfile)
transformed_contents = transform_program(contents)
convert_moon_list_to_dictionary(transformed_contents)

time_steps = 0
print_format(moons, time_steps)

gravity_effects_per_step(pairs, moons)
position_at_end_of_time_step(moons)
time_steps += 1
print_format(moons, time_steps)

# %% Production Environment

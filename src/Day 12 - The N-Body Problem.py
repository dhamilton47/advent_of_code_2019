# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from itertools import groupby

import aoc

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
def transform_input(data):
    for item in ['<', '>', '=', 'x', 'y', 'z', ',']:
        data = [''.join(j).strip(item) for sub in data
                for k, j in groupby(sub, str.isdigit)]

    data = str(''.join(data)).replace('\n', ' ').split(' ')

    return [int(item) for item in data]


def create_new_moons(a, b, c):
    return {o:
            {m:
             {n:
              0
              for n in range(a)}
             for m in range(b)}
            for o in range(c)}


def convert_moon_list_to_dictionary(data, a, b, c):
    new_moons = create_new_moons(a, b, c)

    for i in range(c):
        for j in range(a):
            y = (3 * i) + j
            new_moons[i][0][j] = data[y]

    return new_moons


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
            continue


def gravity_effects_per_step(sister_moons, moons):
    for sister_moon in sister_moons:
        moon1 = moons[sister_moon[0]]
        moon2 = moons[sister_moon[1]]
        gravity_effect_per_pair(moon1, moon2)

    return moons


def position_at_end_of_time_step(moons):
    for moon in range(4):
        for axis in range(3):
            moons[moon][0][axis] = moons[moon][0][axis] + moons[moon][1][axis]

    return moons


def energy(moons):
    e_tot = 0
    for i in range(4):
        e_p = abs(moons[i][0][0]) + abs(moons[i][0][1]) + abs(moons[i][0][2])
        e_k = abs(moons[i][1][0]) + abs(moons[i][1][1]) + abs(moons[i][1][2])
        e_tot += e_p * e_k

    return e_tot


def moon_shot(new_moons, moons, max_steps):
    time_steps = 0
    print_format(moons, time_steps)
    e = energy(moons)
    print('Total energy in the system = {}'.format(e))
    print()

    for i in range(max_steps):
        harvest_moons = gravity_effects_per_step(pairs, moons)
        quarter_moons = position_at_end_of_time_step(harvest_moons)
        e = energy(quarter_moons)
        time_steps += 1
        if not(time_steps % 100000):
            print('Passing time step...{0:,d}'.format(time_steps))
        # if quarter_moons == new_moons:
        #     break
        if e == 0:
            break

    print_format(quarter_moons, time_steps)
    print('Total energy in the system = {}'.format(e))
    print()


# %%  Set up variables

pairs = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

# %% Development Environment

txtfile = "../data/AoC2019_day_12_input.txt"
start = aoc.read_program(txtfile)
start_vector = transform_input(start)
new_moons = convert_moon_list_to_dictionary(start_vector, 3, 2, 4)
full_moons = convert_moon_list_to_dictionary(start_vector, 3, 2, 4)

moon_shot(new_moons, full_moons, 100000000000)

# %% Production Environment

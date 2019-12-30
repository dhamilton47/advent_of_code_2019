# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


import functools

import aoc


# %% Transform the "XXXX" from a string to a list
def transform_input(contents):
    return [int(contents[i]) for i in range(len(contents))]


def extend_input(data, loops):
    datacopy = []
    for i in range(loops):
        datacopy.extend(data)
    return datacopy


def transform_pattern(memory):
    return [int(memory[i]) for i in range(len(memory))]


def FFT(data, phase):
    y = []
    size = len(data)

    n = 1
    for n in range(1, size + 1):
        pattern = (''.join(['0,' * n, '1,' * n, '0,' * n, '-1,' * n])
                   * (size // (4 * n) + 1)).split(",")[1:size + 1]

        pattern = transform_pattern(pattern)

        new_data = map(lambda x, y: x * y, pattern, data)
        y.append(abs(functools.reduce(lambda x, y: x + y, new_data)) % 10)

    # print(f"After {phase} phase{'s' if phase > 1 else ''}: {y[:8]}")

    return y


def final_answer(answer, final_shift):
    a = ''.join([str(answer[i])
                 for i in range(final_shift, final_shift + 8)])
    return a


def upper_triangle(data):
    dl = len(data)
    cumulative_sum = 0
    up_tri = []
    for i in range(dl - 1, -1, -1):
        cumulative_sum += data[i]
        up_tri.append(cumulative_sum)

    # This result is already the length of the extended data.
    # Just plug into the next loop.
    return up_tri


def modulus10(data):
    # Modulus 10 of each digit
    data = list(map(lambda x: x % 10, data))
    data.reverse()

    return data


def phaser(stun, data, shift):
    # Repeat the 'phases' times
    for i in range(stun):
        data = upper_triangle(data)
        data = modulus10(data)
        a = final_answer(data, shift)
        # print(f"Phase {i} signal = {a}")

    return data


def final_answer2(answer, final_shift):
    answer = ''.join([str(answer[i])
                      for i in range(final_shift, final_shift + 8)])
    return print(f"Day 16, Part 2 Result = {answer}")


def day16_part1(phases, data):
    for i in range(1, phases + 1):
        data = FFT(data, i)

    print(f"Day 16, Part 1 Result"
          f" = {''.join([str(data[i]) for i in range(8)])}")


def day16_part2(phases, base_signal, data_len, final_shift):
    # Detemine the portion of the total signal we need to focus on.
    # This will begin at the start of the repetition of the base
    # signal containing
    # the clean signal  and then continuing to the end of the signal.
    reps = (((10000 * data_len) - final_shift) // data_len) + 1
    # reps2 = (10000 * data_len) - final_shift
    remaining_shift = reps * data_len - ((10000 * data_len) - final_shift)
    # reps4 = reps * data_len

    extended_data = extend_input(base_signal, reps)

    answer = phaser(phases, extended_data, remaining_shift)
    final_shift = (reps * data_len) - ((10000 * data_len) - final_shift)
    final_answer2(answer, final_shift)


# %% Development Environment
# txtfile = "../data/adventofcode_2019_day_16g_input.txt"
# Import the base data text file as a text string
# base_signal = read_program(txtfile)

# Determine the index of where the clean signal starts
# final_shift = int(base_signal[:7])

# Transform the data into a list of integers
# base_signal = transform_input(base_signal)
# data_len = len(base_signal)
# print(f"Base date length = {data_len} integers")

# Detemine the portion of the total signal we need to focus on.
# This will begin at the start of the repetition of the base signal containing
# the clean signal  and then continuing to the end of the signal.
# reps = (((10000 * data_len) - final_shift) // data_len) + 1
# reps2 = (10000 * data_len) - final_shift
# remaining_shift = reps * data_len - ((10000 * data_len) - final_shift)
# reps4 = reps * data_len

# extended_data = extend_input(base_signal, reps)


# phases = 100
# cumulative_sum = 0
# sm_upper = []


# Calculate each cross-product of each poisiton in the upper triangle
# print the result
# answer = phaser(phases, extended_data, remaining_shift)
# final_shift = (reps * data_len) - ((10000 * data_len) - final_shift)
# final_answer2(answer, final_shift)

# %% Production Environment

txtfile = "../data/AoC2019_day_16_input.txt"
base_signal = aoc.read_program(txtfile)
final_shift = int(base_signal[:7])
base_signal = transform_input(base_signal)
data_len = len(base_signal)
print(f"Base date length = {data_len} integers\n")

phases = 100
day16_part1(phases, base_signal)
day16_part2(phases, base_signal, data_len, final_shift)

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:20:31 2020

@author: danha
"""

import aoc
import oxygen


# %%

def dimensions(coordinates):
    """ Find the dimensions of the graph we need to create """

    x_s = []
    y_s = []

    for item in list(coordinates.keys()):
        x, y = item
        x_s.append(x)
        y_s.append(y)

    max_x = max(x_s)
    min_x = min(x_s)

    max_y = max(y_s)
    min_y = min(y_s)

    range_x = max_x - min_x + 1
    range_y = max_y - min_y + 1
    print(f"\nRange of the x-axis = {range_x}\n"
          f"  Min x = {min_x}\n"
          f"  Max x = {max_x}\n\n"
          f"Range of the y-axis = {range_y}\n"
          f"  Min y = {min_y}\n"
          f"  Max y = {max_y}")

    return (min_x, max_y, range_x, range_y)


# %%


# def create_display(machine, coordinates, droid):
def create_display(coordinates, droid):
    """ Create the maze after every survey """

    min_x, max_y, range_x, range_y = dimensions(coordinates)
    display = [['#' for i in range(range_y + 2)] for j in range(range_x + 2)]
    # print(f"rows = {len(display)}, columns = {len(display[0])}")
    # opcode = 0

    for item, value in enumerate(coordinates):
        # print(item, value)
        # print(len(value))
        x, y = value
        # print(x, y)
        # print(x - min_x + 1, (y - max_y) + range_y)
        # print(f"rows = {len(display)}, columns = {len(display[0])}")
        # print(f"item = {item}, value = {value}, "
        #       f"orig x = {x}, min x = {min_x}, range x = {range_x}, "
        #       f"adj x = {x - min_x + 1}, "
        #       f"orig y = {y}, max y = {max_y}, range y = {range_y}, "
        #       f"adj y = {(y - max_y) + range_y}")
        display[x - min_x + 1][(y - max_y) + range_y + 1] = coordinates[value]
        # display[x - min_x + 1][(y - max_y) + range_y + 1] = value
        # # display[x][y] = ['#', '.', 'O'][value]

    x, y = droid
    display[x][y] = 'D'

    for row in range(len(display)):
        # print(display[1][:])
        line = ''.join(display[row][:])
        print(line)

    print()

    return display


# %% Development Environment

possible_paths = []

possible_paths, paths, path, coordinates = \
    oxygen.survey_starter(possible_paths)

while possible_paths == []:
    possible_paths, paths, path, coordinates = \
        oxygen.survey(coordinates, paths, possible_paths)


# %% Development Environment

min_x, max_y, range_x, range_y = dimensions(coordinates)
# display = [[' ' * range_x] * range_y]
# machine = oxygen.intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Oxygen System')
display = create_display(coordinates, (1 - min_x, max_y + 1))
# display = create_display(machine, coordinates, (1 - min_x, max_y + 1))

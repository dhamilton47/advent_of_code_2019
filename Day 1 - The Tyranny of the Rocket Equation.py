# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:12:44 2019

@author: Dan J Hamilton
"""


# import pandas as pd
from functools import reduce


# %%
def read_text_file(txtfile):
    contents_split_int = 0
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
        contents_split = contents.splitlines()
        contents_split_int = [int(contents_split[i]) for i
                              in range(len(contents_split))]

    f.close()

    return contents_split_int


# %%
def fuel(x):
    return (x // 3) - 2


# %%
def get_fuel(mass):
    fuel1 = fuel(mass)
    return fuel1 + get_fuel(fuel1) if fuel1 > 0 else 0


# %%
def tyranny_of_the_Rocket_Equation1(data):
    lines = read_text_file(data)

    # Fuel requirement for modules only
    result1 = reduce(lambda x, y: x + fuel(y), lines, 0)

    # Fuel requirement for modules and fuel
    result2 = reduce(lambda x, y: x + get_fuel(y), lines, 0)

    print('Day 1 - Part 1 - Total Fuel Required = {:,d}'.format((result1)))
    print('Day 1 - Part 2 - Total Fuel Required = {:,d}'.format((result2)))


# %% Run code
text = "./data/adventofcode_2019_day_1_input.txt"
tyranny_of_the_Rocket_Equation1(text)

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:12:44 2019

@author: danha
"""


import pandas as pd
from functools import reduce


input = pd.read_csv("./data/adventofcode_2019_day_1_input.txt", sep="\n",
                    names=["data"], header=None, index_col=False)

input_test1 = pd.DataFrame([105311], columns=['data'])
input_test2 = pd.DataFrame([117290], columns=['data'])
input_test3 = pd.DataFrame([97762], columns=['data'])
input_test4 = pd.DataFrame([124678], columns=['data'])
input_test5 = pd.DataFrame([105311, 117290, 97762, 124678], columns=['data'])


def fuel(x):
    return (x // 3) - 2


def tyranny_of_the_Rocket_Equation(df):
    result = 0
    for i in range(len(df)):
        module_weight = df.data[i]

        while fuel(module_weight) >= 0:
            delta = fuel(module_weight)
            result += delta
#            print('module weight = ', module_weight, '\tdelta = ',
#                  '\tIntermediate Result:', result)
            module_weight = delta

    return result


print(tyranny_of_the_Rocket_Equation(input))


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


def get_fuel(mass):
    fuel1 = fuel(mass)
    return fuel1 + get_fuel(fuel1) if fuel1 > 0 else 0


def tyranny_of_the_Rocket_Equation1(data):
    result = 0
    lines = read_text_file(data)

    result = reduce(lambda x, y: x + get_fuel(y), lines, 0)
#    for i in range(len(lines)):
#        result += lines[i] // 3 - 2
    print(result)


text = "./data/adventofcode_2019_day_1_input.txt"
tyranny_of_the_Rocket_Equation1(text)

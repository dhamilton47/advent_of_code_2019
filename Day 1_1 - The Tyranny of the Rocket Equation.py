# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:23:46 2019

@author: danha
"""


import pandas as pd
from functools import reduce


text_file = pd.read_csv("./data/adventofcode_2019_day_1_input.txt", sep="\n",
                        names=["data"], header=None, index_col=False)


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


def tyranny_of_the_Rocket_Equation(data):
    result = 0
    for datum in range(len(data)):
        x = (data.data[datum] // 3) - 2
        result += x

    print(result)


def tyranny_of_the_Rocket_Equation1(data):
    result = 0
    lines = read_text_file(data)
    result = reduce(lambda x, y: x + y // 3 - 2, lines, 0)
#    for i in range(len(lines)):
#        result += lines[i] // 3 - 2
    print(result)


text = "./data/adventofcode_2019_day_1_input.txt"
# arr = list(contents.split(","))

tyranny_of_the_Rocket_Equation(text_file)
tyranny_of_the_Rocket_Equation1(text)

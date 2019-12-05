# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:34:08 2019

@author: danha
"""


import pandas as pd


# input = pd.read_csv("./data/adventofcode_2019_day_2_input.txt", sep=",",
#                    names=["data"], header=None, index_col=False)
#f = open("./data/adventofcode_2019_day_2_input.txt", "r")
#if f.mode == 'r':
#    contents = f.read()
#
#arr = list(contents.split(","))
#arr[1] = 12
#arr[2] = 2


# %%
def read_intcode(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    return contents


# %%
def set_memory(x):
    memory = list(x.split(","))
    return memory


# %%
def initiate_code_sequence(code, x, y):
    memory = set_memory(code)
    memory[1] = x
    memory[2] = y
    return memory


# %%
#input1 = pd.DataFrame([1, 0, 0, 0, 99], columns=['Column_Name'])
#input2 = list([1, 0, 0, 0, 99])
#input3 = list([2, 3, 0, 3, 99])
#input4 = list([2, 4, 4, 5, 99, 0])
#input5 = list([1, 1, 1, 4, 99, 5, 6, 0, 99])


def IntCode(x):
    index = 0
#    print('Original array =', x)
    for i in range(len(x)):
        x[i] = int(x[i])

#    print('length of array =', len(x))
    while index < len(x):
#        print('index = ', index)
        if x[index] == 1:
            x[x[index + 3]] = x[x[index + 1]] + x[x[index + 2]]
            index += 4
        elif +x[index] == 2:
            x[x[index + 3]] = x[x[index + 1]] * x[x[index + 2]]
            index += 4
        elif x[index] == 99:
            print('Day 2 - Part 1 - Output = {:,d}'.format(x[0]))
            index = len(x)
        else:
            print(str(100 * x[index] + x[index + 1]),
                  'program alarm')
            index += 4


# %% Run code
txtfile = "./data/adventofcode_2019_day_2_input.txt"
contents = read_intcode(txtfile)
memory = initiate_code_sequence(contents, 12, 2)
IntCode(memory)

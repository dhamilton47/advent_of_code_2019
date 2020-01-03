# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


import numpy as np

import aoc


# %% Transform the "XXXX" from a string to a list
def transform_program(contents):
    memory = list(contents.split("\n"))
#     memory2 = np.arange(contents)
#     memory1= np.char.split(contents, '\n')
# #    memory_length = len(memory)
# #    for i in range(memory_length):
# #        memory[i] = int(memory[i])

    return memory

txtfile = "../data/AoC2019_day_20_input.txt"
contents = aoc.read_program(txtfile)
transformed_contents = transform_program(contents)
# print(len(contents))
# print(len(transformed_contents))
# print(len(contents) / len(transformed_contents))

# # for i in range(len(transformed_contents)):
# #     print(len(transformed_contents[i]))
# print(tc1.shape)
# print(tc2.shape)

tc4 = np.array(transformed_contents)
# tc3 = np.fromfile(txtfile, dtype=np.string_, count=-1, sep='\n')

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


import aoc


# %% Transform the "XXXX" from a string to a list
def transform_program(contents):
    memory = list(contents.split(","))
#    memory_length = len(memory)
#    for i in range(memory_length):
#        memory[i] = int(memory[i])

    return memory


txtfile = "../data/AoC2019_day_15_input.txt"
contents = aoc.read_program(txtfile)
transformed_contents = transform_program(contents)

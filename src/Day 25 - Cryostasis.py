# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


import numpy as np

import aoc
from computer import Computer


def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.flash_memory()
    computer.halt_condition = True

    return computer


def main():
    pass


# %% Development Environment

opcode = 0
machine = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Search Droid')


# txtfile = "../data/AoC2019_day_25_input.txt"
# contents = aoc.read_program(txtfile)
# transformed_contents = transform_program(contents)

# %% Production Environment (LOL)

# if __name__ == "__main__":
#     main()

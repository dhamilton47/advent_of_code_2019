# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:34:08 2019

@author: Dan J Hamilton
"""

import sys

import aoc
from computer import Computer


# %%
def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.flash_memory()
    computer.halt_condition = True

    return computer


def main(library, program):
    """ main() program """

    machine = intcode(library, program)
    machine.memory.bank[1] = 12
    machine.memory.bank[2] = 2
    machine.process_run()
    print(f"Day 2 - Part 1 - Output = {machine.memory.bank[0]:d}")

    for i in range(100):
        for j in range(100):
            machine = intcode(library, program)
            machine.memory.bank[1] = i
            machine.memory.bank[2] = j
            machine.process_run()
            if machine.memory.bank[0] == 19690720:
                noun = machine.memory.bank[1]
                verb = machine.memory.bank[2]
                answer = 100 * noun + verb
                print(f"Day 2 - Part 2 - 100 * noun + verb = {answer:d}\n"
                      f"Day 2 - Part 2 - Check = {machine.memory.bank[0]:d}")
                sys.exit()


# %% Production Environment (LOL)

if __name__ == "__main__":
    main(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Gravity Assist')

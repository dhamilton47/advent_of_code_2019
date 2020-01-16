# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 02:04:57 2020

@author: Dan J Hamilton
"""

from computer import Computer

import aoc


# %%
def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.boot()
    computer.program_load()
    computer.flash_memory()
    # computer.process_run()

    return computer


# def test(library, program):
#     """ main() program """

#     intcode(library, program)
def test(library, program):
    """ main() program """

    machine = intcode(library, program)
    machine.io.input_value = [1]
    machine.process_run()
    print(f"Day 5, Part 1 - Diagnostic code = {machine.io.output_value}")

    machine = intcode(library, program)
    machine.io.input_value = [5]
    machine.process_run()
    print(f"Day 5, Part 2 - Diagnostic code = {machine.io.output_value}")

# %% Development Environment

# Create Computer
# computer = Computer(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'System Diagnostics')
# computer.boot()
# computer.program_load()
# computer.flash_memory()
# computer.process_run()


# %% Production Environment (LOL)

if __name__ == "__main__":
    test(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'System Diagnostics')

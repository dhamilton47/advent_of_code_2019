# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 00:11:17 2020

@author: Dan J Hamilton
"""

from computer import Computer

import aoc


# %%
def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.flash_memory()

    return computer


def main(library, program):
    """ main() program """

    machine = intcode(library, program)
    machine.io.input_value = [1]
    machine.process_run()
    print(f"Day 9, Part 1 - BOOST keycode = {machine.io.output_value}")

    machine = intcode(library, program)
    machine.io.input_value = [2]
    machine.process_run()
    print(f"Day 9, Part 2 - Distress signal coordinates "
          f"= {machine.io.output_value}")

    return machine

# %% Production Environment (LOL)


if __name__ == "__main__":
    sensor = main(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'BOOST')

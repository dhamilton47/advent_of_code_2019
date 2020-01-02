# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from computer_v1 import Computer

import aoc
import phases
# from phase_generator import phase_generator

# Day 7, Part 1 needs:
#     Multiple programs running on the computer
#     Buffer(s) or stack to add instruction command control
#     Inputs coming from the stack
#     Outputs placed on the stack
#     Inputs:
#         Phase setting
#         Signal

# %%


def TEST(library=aoc.PROGRAMS_AVAILABLE_DICTIONARY):
    computer = Computer(library)
    computer.boot()

    # Select a program to run & flash memory
    computer.program_load()

    if 'Diagnostics' in computer.programs_loaded_keys:
        computer.buffers['Diagnostics'].register[0] = True
        computer.flash_memory()

        computer.process_scheduler()
        computer.process_run()

    if 'ampA' in computer.programs_loaded_keys:
        phase_input = phases.phase_generator()
        print(f"Number of phase combinations to run = {len(phase_input)}")

        for index in range(len(phase_input)):
            # index = 29
            computer.program_reload(computer.programs_available_dictionary['Amp'])
            computer.flash_memory()

            # if 'ampA' in computer.programs_loaded_keys:
            phases.phase_load(computer, phase_input, index)
            print(phase_input[index])
            # if 'ampA' in computer.programs_loaded_keys:
            computer.buffers['ampA'].register[0] = True
            computer.buffers['ampA'].register[2] = 0

            computer.process_scheduler()
            computer.process_run()


# %% Development Environment

# Create TEST
computer = Computer(aoc.PROGRAMS_AVAILABLE_DICTIONARY)
computer.boot()

# Select a program to run & flash memory
computer.program_load()
# computer.flash_memory()

if 'Diagnostics' in computer.programs_loaded_keys:
    computer.buffers['Diagnostics'].register[0] = True
    computer.flash_memory()

    computer.process_scheduler()
    computer.process_run()

if 'ampA' in computer.programs_loaded_keys:
    phase_input = phases.phase_generator()
    print(f"Number of phase combinations to run = {len(phase_input)}")

    for index in range(len(phase_input)):
        # index = 29
        computer.program_reload(computer.programs_available_dictionary['Amp'])
        computer.flash_memory()

        # if 'ampA' in computer.programs_loaded_keys:
        phases.phase_load(computer, phase_input, index)
        print(phase_input[index])
        # if 'ampA' in computer.programs_loaded_keys:
        computer.buffers['ampA'].register[0] = True
        computer.buffers['ampA'].register[2] = 0

# when multiple copies of a program are running, how are they executed:
#     1. in a fixed sequence, or
#     2. in a variable (event) driven sequence
# Check if instruction_next needed for any of the running programs

        computer.process_scheduler()
        computer.process_run()


# test.instruction_next()

# Determine next instruction to process and execute it.


# %% Production Environment (LOL)

# TEST()

# if __name__ == "__main__":
#     TEST()

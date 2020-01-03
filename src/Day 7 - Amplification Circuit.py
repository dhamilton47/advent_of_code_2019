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


def test(library=aoc.PROGRAMS_AVAILABLE_DICTIONARY):
    """ main() program """
    computer = Computer(library)
    computer.boot()

    # Select a program to run & flash memory
    computer.program_load()

    if computer.program_name == 'Diagnostics':
        computer.buffers['Diagnostics'].register[0] = True
        computer.flash_memory()

        computer.process_scheduler()
        computer.process_run()

    if computer.program_name == 'Amp':
        phase_input = phases.phase_generator()
        print(f"Number of phase combinations to run = {len(phase_input)}")

        thruster_max = 0

        for index in range(len(phase_input)):
            # index = 29
            computer.program_reload(computer.library['Amp'])
            computer.flash_memory()

            # if 'ampA' in computer.programs_loaded_keys:
            phases.phase_load(computer, phase_input, index)
            print(phase_input[index])
            # if 'ampA' in computer.programs_loaded_keys:
            computer.buffers['ampA'].register[0] = True
            computer.buffers['ampA'].register[2] = 0

            computer.process_scheduler()
            computer.process_run()
            thruster_max = thruster_max if thruster_max > \
                computer.buffers[computer.process_active].register[3] \
                else computer.buffers[computer.process_active].register[3]
            print(computer.buffers[computer.process_active].register[3])
            print('we got here')
        print(f"Maximum thruster signal = {thruster_max}")


# %% Development Environment

# Create TEST
COMPUTER = Computer(aoc.PROGRAMS_AVAILABLE_DICTIONARY)
computer = COMPUTER
COMPUTER.boot()

# Select a program to run & flash memory
COMPUTER.program_load()
# computer.flash_memory()

if COMPUTER.program_name == 'Diagnostics':
    COMPUTER.buffers['Diagnostics'].register[0] = True
    COMPUTER.flash_memory()

    COMPUTER.process_scheduler()
    COMPUTER.process_run()

if COMPUTER.program_name == 'Amp':
    PHASE_INPUT = phases.phase_generator()
    print(f"Number of phase combinations to run = {len(PHASE_INPUT)}")
    COMPUTER.process_scheduler()

    thruster_max = 0

    for index in range(len(PHASE_INPUT)):
        # index = 29
        COMPUTER.program_reload(COMPUTER.library['Amp'])
        COMPUTER.flash_memory()

        # if 'ampA' in computer.programs_loaded_keys:
        phases.phase_load(COMPUTER, PHASE_INPUT, index)
        # print(PHASE_INPUT[index])
        # if 'ampA' in computer.programs_loaded_keys:
        COMPUTER.buffers['ampA'].register[0] = True
        COMPUTER.buffers['ampA'].register[2] = 0

# when multiple copies of a program are running, how are they executed:
#     1. in a fixed sequence, or
#     2. in a variable (event) driven sequence
# Check if instruction_next needed for any of the running programs

        # COMPUTER.process_scheduler()
        COMPUTER.process_run()

        thruster_max = thruster_max if thruster_max > \
            computer.buffers[computer.process_active].register[3] \
            else computer.buffers[computer.process_active].register[3]
        # print(computer.buffers[computer.process_active].register[3])
        # print('we got here')
    print(f"Maximum thruster signal = {thruster_max}")


# test.instruction_next()

# Determine next instruction to process and execute it.


# %% Production Environment (LOL)

# test()

# if __name__ == "__main__":
#     TEST()

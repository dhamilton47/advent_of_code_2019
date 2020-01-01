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


def TEST(library=aoc.programs_available_dictionary):
    computer = Computer(library)
    memory, cpu, io, stack = computer.boot()

    # Select a program to run & flash memory
    program = computer.program_load()
    memory.register = memory.flash(program)
    # print_vitals_for_TEST(test, memory, cpu, program)

    # Execute program
    opcode = 0

    while opcode != 99:
        instruction = computer.instruction_next(memory)
        instruction = cpu.instruction_execute(computer, memory, instruction)

        computer.ip += instruction['length']
        # print(instruction)
        opcode = instruction['opcode']


# %% Development Environment

# phases = phase_generator()

# Create TEST
computer = Computer(aoc.programs_available_dictionary)
computer.boot()

# Select a program to run & flash memory
computer.program_load()
computer.flash_memory()

if 'ampA' in computer.programs_loaded_keys:
    phase_input = phases.phase_generator()

    index = 29

if 'ampA' in computer.programs_loaded_keys:
    phases.phase_load(computer, phase_input, index)

if 'ampA' in computer.programs_loaded_keys:
    computer.buffers['ampA'].register[0] = True
    computer.buffers['ampA'].register[2] = 0

# Execute program
# opcode = 0

# while opcode != 99:
# when multiple copies of a program are running, how are they executed:
#     1. in a fixed sequence, or
#     2. in a variable (event) driven sequence
# Check if instruction_next needed for any of the running programs
computer.process_scheduler()
computer.process_run()

# test.instruction_next()

# Determine next instruction to process and execute it.


# TEST()

# %% Production Environment (LOL)

# TEST()

# if __name__ == "__main__":
#     TEST()

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from intcode_v5 import Computer

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


# def print_vitals(memory, cpu, program={}, instruction=[]):
#     print('\nComputer Properties:')
#     print('  Computer Name:', test.name)
#     print('  Programs available:', test.programs_available())
#     print('  Program loaded:', test.program_loaded)
#     print('  Instruction Pointer:', test.ip)

#     print('\nMemory Properties:')
#     print('  Register:', memory.register)

#     if program != {}:
#         print('\nProgram Properties:')
#         print('  Program Name:', program.name)
#         print('  Program Binary:', program.binary)
#         print('  Program Code:', program.code)

#     print('\n')


# def print_vitals_for_TEST(computer, memory, cpu, program={}):
#     print('\nComputer Properties:')
#     print('  Computer Name:', computer.name)
#     print('  Programs available:', computer.programs_available())
#     print('  Program loaded:', computer.program_loaded)
#     print('  Instruction Pointer:', computer.ip)

#     print('\nMemory Properties:')
#     print('  Register:', memory.register)

#     if program != {}:
#         print('\nProgram Properties:')
#         print('  Program Name:', program.name)
#         print('  Program Binary:', program.binary)
#         print('  Program Code:', program.code)

#     print('\n')


def TEST(library=aoc.programs_available_dictionary):
    test = Computer(library)
    memory, cpu, io, stack = test.boot()

    # Select a program to run & flash memory
    program = test.program_load()
    memory.register = memory.flash(program)
    # print_vitals_for_TEST(test, memory, cpu, program)

    # Execute program
    opcode = 0

    while opcode != 99:
        instruction = test.instruction_next(memory)
        instruction = cpu.instruction_execute(test, memory, instruction)

        test.ip += instruction['length']
        # print(instruction)
        opcode = instruction['opcode']

    # ampA = Program('Amp')
    # ampA.read_binary('Amp')
    # ampA.code = ampA.read_binary(Program.programs['Amp']['binary'])
    # ampA = Program(test.programs['Amp'])


# %% Development Environment

# phases = phase_generator()

# Create TEST
test = Computer(aoc.programs_available_dictionary)
test.boot()

# Select a program to run & flash memory
test.program_load()
test.flash_memory()

if 'ampA' in test.programs_loaded_keys:
    phase_input = phases.phase_generator()

    index = 0

if 'ampA' in test.programs_loaded_keys:
    phases.phase_load(test, phase_input, index)

if 'ampA' in test.programs_loaded_keys:
    test.buffers['ampA'].register[0] = True
    test.buffers['ampA'].register[2] = 0

# Execute program
# opcode = 0

# while opcode != 99:
# when multiple copies of a program are running, how are they executed:
#     1. in a fixed sequence, or
#     2. in a variable (event) driven sequence
# Check if instruction_next needed for any of the running programs
test.process_scheduler()
# test.process()

test.instruction_next()

# Determine next instruction to process and execute it.


# TEST()

# %% Production Environment (LOL)

# TEST()

# if __name__ == "__main__":
#     TEST()

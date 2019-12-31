# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from intcode_v5 import Computer

import aoc

# Day 7, Part 1 needs:
#     Multiple programs running on the computer
#     Buffer(s) or stack to add instruction command control
#     Inputs coming from the stack
#     Outputs placed on the stack
#     Inputs:
#         Phase setting
#         Signal

# Day 7, Part 2 needs:

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


# def print_instruction():
#     # print('IP:', IP)
#     # while IP < program_lenth:
#     # instruction = ampA.get_instruction(0)
#     # print(instruction)
#     # print('Length =', instruction.instruction_length)
#     # print('OpCode =', instruction.opcode)
#     # print('Parameters =', instruction.parameters)
#     # print('Modes =', instruction.parameter_modes)
#     pass


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


# def day2_part1():
#     number_of_computers = 1
#     message_out1 = 'Day 2, Part 1 - Value at position 0 ='
#     pass


# def day2_part2():
#     number_of_computers = 1
#     message_out2 = 'Day 2, Part 2 - 100 * noun + verb ='
#     pass


# def day5():
#     # Create TEST
#     test = Computer(aoc.programs_available_dictionary)
#     cpu, io, memory = test.boot()

#     program = test.program_load()
#     memory.register = memory.flash(program)

#     # Execute program
#     opcode = 0

#     while opcode != 99:
#         instruction = test.instruction_next(memory)
#         instruction = cpu.instruction_execute(test,
#                                               program,
#                                               memory,
#                                               instruction)

#         test.ip += instruction['length']

#         opcode = instruction['opcode']


# def day7_part1():
#     number_of_computers = 5
#     arrangement = 'sequential'

#     message_in_ampA_phase = 'AmpA phase = '
#     message_in_ampA_signal = 'AmpA input signal = '
#     message_out_ampA = 'AmpA output signal = '

#     message_in_ampB_phase = 'AmpB phase = '
#     message_in_ampB_signal = 'AmpB input signal = '
#     message_out_ampB = 'AmpB output signal = '

#     message_in_ampC_phase = 'AmpC phase = '
#     message_in_ampC_signal = 'AmpC input signal = '
#     message_out_ampC = 'AmpC output signal = '

#     message_in_ampD_phase = 'AmpD phase = '
#     message_in_ampD_signal = 'AmpD input signal = '
#     message_out_ampD = 'AmpD output signal = '

#     message_in_ampE_phase = 'AmpE phase = '
#     message_in_ampE_signal = 'AmpE input signal = '
#     message_out_ampE = 'AmpE output signal = '

#     message_out = 'Day 7, Part 1 - Largest output signal ='
#     pass


# def day7_part2():
#     number_of_computers = 5
#     arrangement = 'parallel'

#     message_in_ampA_phase = 'AmpA phase = '
#     message_in_ampA_signal = 'AmpA input signal = '
#     message_out_ampA = 'AmpA output signal = '

#     message_in_ampB_phase = 'AmpB phase = '
#     message_in_ampB_signal = 'AmpB input signal = '
#     message_out_ampB = 'AmpB output signal = '

#     message_in_ampC_phase = 'AmpC phase = '
#     message_in_ampC_signal = 'AmpC input signal = '
#     message_out_ampC = 'AmpC output signal = '

#     message_in_ampD_phase = 'AmpD phase = '
#     message_in_ampD_signal = 'AmpD input signal = '
#     message_out_ampD = 'AmpD output signal = '

#     message_in_ampE_phase = 'AmpE phase = '
#     message_in_ampE_signal = 'AmpE input signal = '
#     message_out_ampE = 'AmpE output signal = '

#     message_out = 'Day 7, Part 2 - Largest output signal ='
#     pass


# def day9_part1():
#     number_of_computers = 1
#     pass


# def day9_part2():
#     number_of_computers = 1
#     pass


# %% Development Environment

# phases = permutations()

# Create TEST
test = Computer(aoc.programs_available_dictionary)
test.boot()
# cpu, io, memory, stack = test.boot()
# print_vitals(memory, cpu)

# Select a program to run & flash memory
test.program_load()
test.flash_memory()
# amp = test.program_load()
# print(f"top level: {amp}\n")
# memory.bank = memory.flash(amp)
# print_vitals(memory, cpu, program)

# Execute program
# opcode = 0

# while opcode != 99:
# Check if instruction_next needed for any of the running programs
test.instruction_next()

# for item in test.ips.items():
#     print(item[1], test.ips_last[item[0]])
#     if item[1] == test.ips_last[item[0]]:
#         instructions[item[0]] = test.instruction_next(memory, item[0])

# instruction = cpu.instruction_execute(test,
#                                       amp,
#                                       memory,
#                                       io,
#                                       instruction)

# test.ip += instruction['length']
# # print(instruction)
# opcode = instruction['opcode']


# While Instruction loop

#     Get input

#     Print output

# Cleanup

# Repeat the above if more than one computer in play


# TEST()

# Create Computer
# intcode = IntCode(1)
# program, memory = intcode.initialize_program(intcode.program_number)
# ops = OS_AoC19()
# stack = Stack()
# cpu = CPU()
# io = IO_AoC19()

# ampA = Program(thermal_radiators, thermal_radiators_textfile)
# ampA.run_program()
# ampA.get_input('Enter phase number: ')
# ampA.get_input('Enter input signal: ')
# ampA_output_signal.get_output()

# ampB = IntCode(readable_program)
# ampB.run_program()
# ampB.get_input('Enter phase number: ')
# ampB.get_input('Enter input signal: ')
# ampB_output_signal.get_output()

# ampC = IntCode(readable_program)
# ampC.run_program()
# ampC.get_input('Enter phase number: ')
# ampC.get_input('Enter input signal: ')
# ampC_output_signal.get_output()

# ampD = IntCode(readable_program)
# ampD.run_program()
# ampD.get_input('Enter phase number: ')
# ampD.get_input('Enter input signal: ')
# ampD_output_signal.get_output()

# ampE = IntCode(readable_program)
# ampE.run_program()
# ampE.get_input('Enter phase number: ')
# ampE.get_input('Enter input signal: ')
# ampE_output_signal.get_output()

# %%

def build_phase_choices(a, i):
    x = []
    for y in range(len(a)):
        if a[y] != i:
            x.append(a[y])

    return x


# %% Create 5P5 (permutations)

def permutations():
    phase0 = [0, 1, 2, 3, 4]
    phases = []
    for index, i in enumerate(phase0):
        phase1 = build_phase_choices(phase0, phase0[index])
        for index, j in enumerate(phase1):
            phase2 = build_phase_choices(phase1, phase1[index])
            for index, k in enumerate(phase2):
                phase3 = build_phase_choices(phase2, phase2[index])
                for index, l in enumerate(phase3):
                    phase4 = build_phase_choices(phase3, phase3[index])
                    m = phase4[0]
                    phases.append([i, j, k, l, m])

    return phases


# %% Programs Dictionary

# programs_available_dictionary = {
#     'Amp': {'name': 'Amplifier Controller',
#             'binary': '../data/adventofcode_2019_day_7_input1.txt'},
#     'None': {'name': '',
#              'binary': ''}, }

# %% Production Environment (LOL)

# TEST()

# if __name__ == "__main__":
#     TEST()

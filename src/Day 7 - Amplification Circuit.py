# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from intcode.intcode_v2 import IntCode
# from memory import Memory


# %% Import the "program" data (as a string)

def read_program(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    return contents


# %% Transform the "program" from a string to a list of integers

def transform_program(contents):
    memory = list(contents.split(","))
    memory_length = len(memory)
    for i in range(memory_length):
        memory[i] = int(memory[i])

    return memory


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


# %%

def TEST(self_initialize=True, noun=0, verb=0):

    txtfile = "../data/adventofcode_2019_day_5_input.txt" \
        if self_initialize else "../data/adventofcode_2019_day_2_input.txt"

    # Create IntCode instance
    intcode = IntCode()
    intcode.load_program(txtfile)
    # if not(self_initialize):
    #     intcode.noun = noun
    #     intcode.verb = verb

    # Run code
    intcode.run_program()


# %% Development Environment

txtfile7 = "../data/adventofcode_2019_day_7_input.txt"
txtfile5 = "../data/adventofcode_2019_day_5_input.txt"
# program = read_program(txtfile7)
# readable_program = transform_program(program)

phases = permutations()

ampA = IntCode()
program = ampA.read_program(txtfile5)

program_lenth = ampA.memory_size
IP = ampA.instruction_pointer

while IP < program_lenth:
    instruction = ampA.get_instruction(IP)
    ampA.execute_instruction(instruction)
    ampA.prt0()
    IP = ampA.instruction_pointer

# IP = ampA.instruction_pointer
# print('Instruction pointer = {}'.format(IP))
# instruction = ampA.get_instruction(IP)
# print('Instruction = {}'.format(instruction))
# # ampA.decode_opcode()
# ampA.execute_instruction(instruction)

# IP = ampA.instruction_pointer
# print('Instruction pointer = {}'.format(IP))

# ampA.get_input('Enter phase number: ')
# ampA.get_input('Enter input signal: ')

# ampA_output_signal.get_output()
# ampA.load_program(txtfile5)
# ampA.read_program(txtfile7)
# ampA.transform_program()
# a = ampA.run_program()

# ampB = IntCode(readable_program)
# b = ampB.run_program()
# ampB.read_program(txtfile5)

# ampC = IntCode(readable_program)
# c = ampC.run_program()
# ampC.read_program(txtfile5)

# ampD = IntCode(readable_program)
# d = ampD.run_program()
# ampD.read_program(txtfile5)

# ampE = IntCode(readable_program)
# e = ampE.run_program()
# ampE.read_program(txtfile5)

# %% Production Environment (LOL)

# TEST()

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from intcode.intcode_v4 import Computer
from intcode.intcode_v4 import Program
from intcode.intcode_v4 import Instruction


# %% Programs Dictionary

programs_available_dictionary = {
    'Amp': {'name': 'Amplifier Controller',
            'binary': '../data/adventofcode_2019_day_7_input1.txt'},
    'None': {'name': '',
              'binary': ''}, }

# # %% Import the "program" data (as a string)

# def read_program(txtfile):
#     f = open(txtfile, "r")
#     if f.mode == 'r':
#         contents = f.read()
#     f.close()

#     return contents


# # %% Transform the "program" from a string to a list of integers

# def transform_program(contents):
#     memory = list(contents.split(","))
#     memory_length = len(memory)
#     for i in range(memory_length):
#         memory[i] = int(memory[i])

#     return memory


# %%

# def TEST(self_initialize=True, noun=0, verb=0):

#     txtfile = "../data/adventofcode_2019_day_5_input.txt" \
#         if self_initialize else "../data/adventofcode_2019_day_2_input.txt"

#     # Create IntCode instance
#     intcode = IntCode()
#     intcode.load_program(txtfile)
#     # if not(self_initialize):
#     #     intcode.noun = noun
#     #     intcode.verb = verb

#     # Run code
#     intcode.run_program()

def print_vitals(memory, cpu, program={}, instruction=[]):
    print('Computer Name:', test.name)
    print('Programs available:',test.get_programs_available())
    print('Programs running:', test.programs_running)
    print('Instruction Pointers:', test.instruction_pointers)
    # print(Program.programs['Amp']['binary'])

    # print('Memory code:', memory.code)
    print('Memory:', memory.memory)

    if program != {}:
        print('Program Name:', program.name)
        print('Program Text File:', program.binary)
        print('Program Code:', program.code)

    if instruction != []:
        print('Raw OpCode:', instruction.raw_opcode)
        print('OpCode:', instruction.opcode)
        print('Parameters:', instruction.parameters)
        print('Modes:', instruction.modes)

    print('\n')


def TEST(library):
    test = Computer(library)
    memory, cpu = test.boot()
    # ampA, memory, instruction, cpu = test.boot()
    print_vitals(memory, cpu)

    # Create Program
    ampA = Program('Amp')
    # ampA.read_binary('Amp')
    ampA.code = ampA.read_binary(Program.programs['Amp']['binary'])
    # ampA = Program(test.programs['Amp'])


# %% Development Environment

# Programs
amplifier_controller = "../data/adventofcode_2019_day_7_input1.txt"
thermal_radiators = "thermal_radiators"
thermal_radiators_textfile = "../data/adventofcode_2019_day_5_input.txt"

# program = read_program(txtfile7)
# readable_program = transform_program(program)

# phases = permutations()


# Create TEST
test = Computer(programs_available_dictionary)
memory, cpu = test.boot()
# ampA, memory, instruction, cpu = test.boot()
print_vitals(memory, cpu)

# print('Computer Name:', test.name)
# print(Program.programs['Amp']['binary'])

# Select a program to run
which_program = test.load_program()


# Create Program
ampA = Program('Amp')
# ampA.read_binary('Amp')
ampA.code = ampA.read_binary(Program.programs['Amp']['binary'])
# ampA = Program(test.programs['Amp'])

print_vitals(memory, cpu, ampA)
# print('Program Name:', ampA.name)
# print('Program Text File:', ampA.binary)
# print('Program Code:', ampA.code)
# print('Memory code:', memory.code)
# print('Memory:', memory.memory)
# print('Instruction Pointer:', ampA.instruction_pointer)
# print('Raw OpCode:', instruction.raw_opcode)
# print('OpCode:', instruction.opcode)
# print('Parameters:', instruction.parameters)
# print('Modes:', instruction.modes)
# print('Memory Size:', memory.memory_size)

# ampA.get_instruction(ampA.instruction_pointer)

# TEST(programs_available_dictionary)


# Create Computer
# intcode = IntCode(1)
# program, memory = intcode.initialize_program(intcode.program_number)
# ops = OS_AoC19()
# stack = Stack()
# cpu = CPU()
# io = IO_AoC19()

# Install program
# program = intcode.load_program1(intcode.program_number)
# print(program)
# print('Program Name:', program.name)
# print('Program Text File:', program.program_txtfile)
# print('Program Code', program.code)
# print('Memory name:', memory.name)
# print('Memory:', memory.memory)
# print('Memory Size:', memory.memory_size)

# Initialize memory for program



# program = intcode.load_program(thermal_radiators, thermal_radiators_textfile)
# ampA = Program(thermal_radiators, thermal_radiators_textfile)
# print(ampA.program_names, ampA.programs)
# program = ampA.read_program(thermal_radiators)
# ampA.initialize_memory()
# ampA.programs[0].initialize_memory()
# ampA.memory[0] = ampA.programs[0].initialize_memory()
# print(ampA.programs[0], ampA.programs[0].memory_size[0], ampA.programs[0].memory[0])
# IP = ampA.instruction_pointer
# print('IP:', IP)
# while IP < program_lenth:
# instruction = ampA.get_instruction(0)
# print(instruction)
# print('Length =', instruction.instruction_length)
# print('OpCode =', instruction.opcode)
# print('Parameters =', instruction.parameters)
# print('Modes =', instruction.parameter_modes)

# instruction = ampA.get_instruction(2)
# print(instruction)
# print('Length =', instruction.instruction_length)
# print('OpCode =', instruction.opcode)
# print('Parameters =', instruction.parameters)
# print('Modes =', instruction.parameter_modes)

# instruction = ampA.get_instruction(6)
# print(instruction)
# print('Length =', instruction.instruction_length)
# print('OpCode =', instruction.opcode)
# print('Parameters =', instruction.parameters)
# print('Modes =', instruction.parameter_modes)

# run_instruction = Instruction(instruction)
#instruction = ampA.get_instruction(2)
#print(instruction)
#instruction = ampA.get_instruction(10)
#print(instruction)
# ampA.execute_instruction(instruction)
#     ampA.prt0()
#     IP = ampA.instruction_pointer

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

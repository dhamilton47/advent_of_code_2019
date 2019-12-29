# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from intcode.intcode_v4 import Computer
from intcode.intcode_v4 import Program
from intcode.intcode_v4 import Instruction


# %% Programs Dictionary

programs_available_dictionary1 = {
    'Amp': {'name': 'Amplifier Controller',
            'binary': '../data/adventofcode_2019_day_7_input1.txt'},
    'None': {'name': '',
              'binary': ''}, }

programs_available_dictionary = {
    'Gravity Assist': {'name': 'Gravity Assist',
                       'copies': ['GravAsst'],
                       'binary': '../data/adventofcode_2019_day_2_input.txt'},

    'Diagnostics': {'name': 'Diagnostic Program',
                    'copies': ['Diagnostics'],
                    'binary': '../data/adventofcode_2019_day_5_input.txt'},

    'Thrusters': {'name': 'Amplifier Controller Software',
                  'copies': ['ampA', 'ampB', 'ampC', 'ampD'],
                  'binary': '../data/adventofcode_2019_day_7_input1.txt'},

    'BOOST': {'name': 'Basic Operation Of System Test',
              'copies': ['BOOST'],
              'binary': '../data/adventofcode_2019_day_9_input.txt'},

    'Registration Identifier': {'name': 'Emergency Hull Painting',
                                'copies': ['Registration'],
                                'binary': '../data/' +
                                'adventofcode_2019_day_11_input.txt'},

    'Arcade Cabinet': {'name': 'Arcade Game',
                       'copies': ['Arcade'],
                       'binary': '../data/adventofcode_2019_day_13_input.txt'},

    'Oxygen System': {'name': 'Remote Repair Program',
                      'copies': ['Oxygen'],
                      'binary': '../data/adventofcode_2019_day_15_input.txt'},

    'ASCII': {'name': 'Aft Scaffolding Control and Information Interface',
              'copies': ['ASCII'],
              'binary': '../data/adventofcode_2019_day_17_input.txt'},

    'Tractor Beam': {'name': 'Drone Control',
                     'copies': ['TractorBeam'],
                     'binary': '../data/adventofcode_2019_day_19_input.txt'},

    'Springdroid': {'name': 'springscript',
                    'copies': ['Springdroid'],
                    'binary': '../data/adventofcode_2019_day_21_input.txt'},

    'Ship Network': {'name': 'Network Interface Controller',
                     'copies': ['NIC'],
                     'binary': '../data/adventofcode_2019_day_23_input.txt'},

    'Search Droid': {'name': 'Droid Communications',
                     'copies': ['Search'],
                     'binary': '../data/adventofcode_2019_day_25_input.txt'},

    'None': {'name': '',
             'copies': [],
             'binary': ''}, }


# %%

def print_vitals(memory, cpu, program={}, instruction=[]):
    print('\nComputer Properties:')
    print('  Computer Name:', test.name)
    print('  Programs available:', test.programs_available())
    print('  Program loaded:', test.program_loaded)
    print('  Instruction Pointer:', test.ip)
    # print(Program.programs['Amp']['binary'])

    # print('Memory code:', memory.code)
    print('\nMemory Properties:')
    print('  Memory:', memory.register)

    if program != {}:
        print('\nProgram Properties:')
        print('  Program Name:', program.name)
        print('  Program Binary:', program.binary)
        print('  Program Code:', program.code)

    if instruction != []:
        print('\nInstruction Properties:')
        print('  Raw OpCode:', instruction.raw_opcode)
        print('  OpCode:', instruction.opcode)
        print('  Parameters:', instruction.parameters)
        print('  Modes:', instruction.modes)

    print('\n')


def print_instruction():
    # print('IP:', IP)
    # while IP < program_lenth:
    # instruction = ampA.get_instruction(0)
    # print(instruction)
    # print('Length =', instruction.instruction_length)
    # print('OpCode =', instruction.opcode)
    # print('Parameters =', instruction.parameters)
    # print('Modes =', instruction.parameter_modes)
    pass


def TEST(library):
    test = Computer(library)
    memory, cpu = test.boot()
    # ampA, memory, instruction, cpu = test.boot()
    print_vitals(memory, cpu)

    # Create Program
    # ampA = Program('Amp')
    # ampA.read_binary('Amp')
    # ampA.code = ampA.read_binary(Program.programs['Amp']['binary'])
    # ampA = Program(test.programs['Amp'])


# %% Development Environment

# Programs
# amplifier_controller = "../data/adventofcode_2019_day_7_input1.txt"
# thermal_radiators = "thermal_radiators"
# thermal_radiators_textfile = "../data/adventofcode_2019_day_5_input.txt"

# program = read_program(txtfile7)
# readable_program = transform_program(program)

# phases = permutations()


# Create TEST
test = Computer(programs_available_dictionary)
memory, cpu = test.boot()
print_vitals(memory, cpu)

# Select a program to run & flash memory
program = test.load_program(test.name)
memory.register = memory.flash(program.code)
print_vitals(memory, cpu, program)

# Execute program
# instruction = test.instruction_next(memory, test.ip)
# test.ip += instruction[-1]
# print(test.ip)
opcode = 0
# opcode = instruction[0]

while opcode != 99:
    # print(memory.address(ip))
    instruction = test.instruction_next(memory, test.ip)
    # test.instruction_execute(instruction)
    # instruction = test.instruction_next(memory, test.ip)

    test.ip += instruction[-1]
    print(instruction)
    opcode = instruction[0]
    # opcode = 99


# While Instruction loop

#     Get input

#     Print output

# Cleanup

# Repeat the above if more than one computer in play


# TEST(programs_available_dictionary)


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

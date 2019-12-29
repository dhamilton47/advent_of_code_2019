# -*- coding: utf-8 -*-
"""
Created on Sun Dec  22 15:49:41 2019

@author: Dan J Hamilton
"""


import sys
# from memory import Memory
# from program import Program

import aoc


# %% Define the IntCode class

# class Computer
#     Sub Classes
#         class Program
#         class Memory
#         class Instruction
#         class IO
#         class CPU
#         class OS
#             class Instruction
#         class Stack

#     Properties
#         name
#         programs_available
#         programs_running
#         instruction_pointers

#     Methods
#         boot
#         instruction_next
#         instruction_execute
#         program_install
#         program_load
#         program_menu
#         programs_available
#         initialize_memory
#         input
#         output

# class Program
#     Properties
#         programID
#         name
#         binary
#         code

#     Methods
#         read_binary

# class Instruction
#     Properties
#         instruction
#         instruction_length
#         raw_opcode
#         instruction_dict
#         opcode
#         modes
#         parameters

# class Memory
#     Properties
#         buffer
#         register

#     Methods
#         flash
#         address

# class CPU
#     Properties
#         instruction
#         name

#     Methods
#         opcode1
#         opcode2
#         opcode3
#         opcode4
#         opcode5
#         opcode6
#         opcode7
#         opcode8
#         opcode99
#         opcode_generic
#         add
#         multiply


class Computer:
    """
    class Computer(library = dictionary of information regarding programs)
        Sub Classes
            class Program
            class Memory
            class Instruction
            class IO
            class CPU
            class OS
                class Instruction
            class Stack

        Properties
            ...

        Methods
            ...
    """

    def __init__(self, library):
        self.name = 'HAL'
        self.programs_available_dictionary = library
        self.program_loaded = None
        self.ip = None

    # def boot1(self, programID='None'):
    #     # program = Program()
    #     program = Program(programID)
    #     memory = Memory()
    #     instruction = Instruction(memory, opcode_dictionary)
    #     cpu = CPU()

    #     return memory, cpu
    #     # return program, memory, instruction, cpu

    def boot(self):
        """
        Initialize sub-classes the computer utilizes.
        """
        memory = Memory()
        cpu = CPU()

        return memory, cpu

    def instruction_next(self, memory, pointer):
        # print(pointer)
        instruction = Instruction(memory, pointer)

        return instruction.instruction

    # def instruction_execute(self):
    #     pass

    def program_install(self, program_keys, program_index):
        program_id = program_keys[program_index]
        program = Program(self.programs_available_dictionary[program_id])
        program.code = program.read_binary()
        self.program_loaded = program_keys[program_index]
        self.ip = 0

        return program

    def program_load(self, computer_name):
        """
        Control the flow to:
            Ask which program to run on this computer
            Load the program
        """

        program_keys = self.programs_available()
        program_index = self.program_menu(program_keys)
        program = self.program_install(program_keys, program_index)

        return program

    def program_menu(self, program_list):
        """
        Create the text to display for the user to make a choice
        of which program to run.  Ask for that choice and return it.

        program_list = the dictionary keys from the
                       programs_available_dictionary
        """

        print_string = "Hello, Dan. "
        print_string += ("My name is " + self.name
                         + ".  I am capable of doing the following:")

        for i in range(len(program_list)):
            if program_list[i] == "None":
                continue

            print_string += "\n  " + f"{i:2d}" + ". " + program_list[i]

        print(f"{print_string}")

        return int(input('What shall we do today?\n(Please enter a number): '))

    def programs_available(self):
        """ Return the programs_available_dictionary's keys """
        return list(self.programs_available_dictionary.keys())

    # def flash_memory():
    #     pass

    def get_input():
        pass

    def print_output():
        pass


# %% Program Class

class Program:
    def __init__(self, programID):
        self.programID = programID
        self.name = self.programID['name']
        self.binary = self.programID['binary']
        self.code = self.read_binary()

    def read_binary(self, program_binary=None):
        """
        Read and parse the text file associated with the named program
        """
        if program_binary is not None:
            self.binary = program_binary

        f = open(self.binary, "r")
        if f.mode == 'r':
            contents = f.read()
            f.close()

        code = []
        raw_program = list(contents.split(","))
        raw_program_length = len(raw_program)
        for i in range(raw_program_length):
            code.append(int(raw_program[i]))

        return code

    # def load_program(self):
    #     pass

    # def initialize_memory(self):
    #     pass

    # def load_program(self, program_info):
    #     code = Program(program_info)
    #     return code

    # def initialize_memory(self):
    #     memory_bank = Memory(self.code)

    #     return memory_bank

    # def get_input(self):
    #     pass

    # def get_instruction(self, ip, memory):
    #     return Instruction(ip, memory)
    #     # raw_opcode = self.memory(self.instruction_pointer)

    # def run_instruction(self, opcode):
    #     if opcode == 1:
    #         # Send to CPU
    #         self.cpu(self.parameters)
    #         self.opcode1(parameters)
    #     elif opcode == 2:
    #         # Send to CPU
    #         self.opcode2(parameters)
    #     elif opcode == 3:
    #         # Send to I/O
    #         self.opcode3(parameters)
    #     elif opcode == 4:
    #         # Send to I/O
    #         self.opcode4(parameters)
    #     elif opcode == 5:
    #         # Send to CPU
    #         self.opcode5(parameters)
    #     elif opcode == 6:
    #         # Send to CPU
    #         self.opcode6(parameters)
    #     elif opcode == 7:
    #         # Send to CPU
    #         self.opcode7(parameters)
    #     elif opcode == 8:
    #         # Send to CPU
    #         self.opcode8(parameters)
    #     elif opcode == 99:
    #         # Terminate Program Execution
    #         self.opcode99()
    #     else:
    #         print(str(100 * memory[ip] + memory[ip + 1]), 'program alarm')
    #         # print(str(100 * self.memory[self.instruction_pointer]
    #         #           + self.memory[self.instruction_pointer + 1]),
    #         #       'program alarm')
    #         self.instruction_pointer += 4


# %% Instruction Class

class Instruction:
    def __init__(self, memory, ip=None, dictionary=aoc.opcode_dictionary):
        self.raw_opcode = memory.address(ip)
        self.opcode = dictionary[self.raw_opcode]['opcode']
        self.modes = dictionary[self.raw_opcode]['modes']
        self.parameters = dictionary[self.raw_opcode]['parameters']
        self.length = dictionary[self.raw_opcode]['length']
        self.instruction = {'opcode': self.opcode,
                            'parameters': self.decode_parameters(
                                memory,
                                self.length,
                                ip),
                            'length': self.length}

    def decode_parameters(self, memory, length, ip):
        if length == 1:
            return {}

        parameters = {}

        for index in range(length - 1):
            if self.modes[index] == 'position':
                adr = memory.address((ip + 1) + index)
            else:
                adr = (ip + 1) + index

            val = memory.address(adr)

            parameters[index] = {'address': adr, 'value': val}

        return parameters


# %% Memory Class

class Memory:
    def __init__(self, code=[]):
        self.register = self.flash(code)

    def flash(self, code):
        mem_dict = {}

        for i in range(len(code)):
            mem_dict[i] = code[i]

        return mem_dict

    def address(self, i):
        if i is None:
            return 'None'

        return self.register[i]


# %% CPU Class

class CPU:
    def __init__(self, instruction=[]):
        self.instruction = instruction
        self.name = 'The Little Train That Could'

# # %%
#     def read_stack(self):
#         executable = stack.pop()

    def instruction_execute(self, memory, ip, inst):
        opcode = inst['opcode']
        par = inst['parameters']
        # print(par)
        # length = inst['length']

        if opcode == 1:
            memory.register[par[2]['address']] = \
                self.add(par[0]['value'], par[1]['value'])
        elif opcode == 2:
            memory.register[par[2]['address']] = \
                self.multiply(par[0]['value'], par[1]['value'])
        elif opcode == 3:
            answer = int(input('Which System ID are we testing? '))
            memory.register[par[0]['address']] = answer
            # memory[par[0]['address']] = \
            #     int(input('Which System ID are we testing? '))
        elif opcode == 4:
            print('Diagnostic Code = {:,d}'.format(par[0]['value']))
        elif opcode == 5:
            if par[0]['value']:
                inst['length'] = par[1]['value'] - ip
        elif opcode == 6:
            if par[0]['value'] == 0:
                inst['length'] = par[1]['value'] - ip
        elif opcode == 7:
            memory.register[par[2]['address']] = \
                1 if par[0]['value'] < par[1]['value'] else 0
        elif opcode == 8:
            memory.register[par[2]['address']] = \
                1 if par[0]['value'] == par[1]['value'] else 0
        elif opcode == 99:
            # Terminate Program Execution
            return inst
        else:
            print(str(100 * memory.address(ip) + memory.address(ip + 1)),
                  'program alarm')
            sys.exit()

        return inst

    def add(self, i, j):
        return i + j

    def multiply(self, i, j):
        return i * j

#         self.opcode = opcode
#         self.decode_opcode(self.instruction_pointer)
# #        self.decode_opcode()
#         if opcode == 3:
#             response = self.get_input(message)
# #        print(instruction[0], instruction[1:], opcode)
#         self.opcode_switch(instruction[0], instruction[1:], opcode)

# # %% OpCode 1 - add two values

#     def opcode1(self, parameters):
#         p1 = self.memory[self.address(0)]
#         p2 = self.memory[self.address(1)]
#         self.memory[parameters[2]] = self.add(p1, p2)
#         self.instruction_pointer += self.instruction_length

# # %% OpCode 2 - multiply two values

#     def opcode2(self, parameters):
#         p1 = self.memory[self.address(0)]
#         p2 = self.memory[self.address(1)]
#         self.memory[parameters[2]] = self.multiply(p1, p2)
#         self.instruction_pointer += self.instruction_length

# # %% OpCode 3 - ask for input

#     def opcode3(self, parameters, input_source):
# #        self.prt0()

# #        self.memory[parameters[0]] = self.get_input(message)
#         if input_source == 'keyboard':
#             self.memory[parameters[0]] = \
#                 int(input('Which System ID are we testing? '))
# #        print(self.instruction_length)
#         self.instruction_pointer += self.get_instruction_length(code=3)
# #        self.instruction_pointer += self.instruction_length


# # %% OpCode 4 - output a result

#     def opcode4(self, parameters):
#         p1 = self.memory[self.address(0)]
#         if p1:
#             print('Diagnostic Code = {:,d}'.format(p1))
#         self.instruction_pointer += self.instruction_length

# # %% OpCode 5 - jump-if-true

#     def opcode5(self, parameters):
#         p1 = self.memory[self.address(0)]
#         p2 = self.memory[self.address(1)]
#         if p1:
#             self.instruction_pointer = p2
#         else:
#             self.instruction_pointer += self.instruction_length

# # %% OpCode 6 - jump-if-false

#     def opcode6(self, parameters):
#         p1 = self.memory[self.address(0)]
#         p2 = self.memory[self.address(1)]
#         if not(p1):
#             self.instruction_pointer = p2
#         else:
#             self.instruction_pointer += self.instruction_length

# # %% OpCode 7 - less than

#     def opcode7(self, parameters):
#         p1 = self.memory[self.address(0)]
#         p2 = self.memory[self.address(1)]
#         self.memory[parameters[2]] = 1 if p1 < p2 else 0
#         self.instruction_pointer += self.instruction_length

# # %% OpCode 8 - equals

#     def opcode8(self, parameters):
#         p1 = self.memory[self.address(0)]
#         p2 = self.memory[self.address(1)]
#         self.memory[parameters[2]] = 1 if p1 == p2 else 0
#         self.instruction_pointer += self.instruction_length

# # %% OpCode 99 - terminate program

#     def opcode99(self):
#         if self.memory[1] == 12 and self.memory[2] == 2:
#             print('Day 2 - Part 1 - Output = {:,d}'.format(self.memory[0]))
#         if self.memory[0] == 19690720:
#             print('Day 2 - Part 2 - 100 * noun + verb = {}'
#                   .format(100 * self.memory[1] + self.memory[2]))
#             print('Day 2 - Part 2 - Check = {}'.format(self.memory[0]))

#         self.instruction_pointer = len(self.memory)

# # %% OpCode general form

#     def opcode_generic(self, i):
#         p = self.memory[self.address(i)]
#         return p


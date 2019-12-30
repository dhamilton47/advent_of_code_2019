# -*- coding: utf-8 -*-
"""
Created on Sun Dec  22 15:49:41 2019

@author: Dan J Hamilton
"""


import sys
# import os

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
#         program_running
#         ip (instruction pointer)

#     Methods
#         boot
#         instruction_next
#         program_load
#         program_menu
#         programs_available

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

    def instruction_next(self, memory, pointer=None):
        if pointer is None:
            pointer = self.ip

        instruction = Instruction(memory, pointer)

        return instruction.instruction

    # def instruction_execute(self):
    #     pass

    def program_load(self):
        """
        Control the flow to:
            Ask which program to run on this computer
            Load the program
        """

        program_keys = self.programs_available()
        program_index = self.program_menu(program_keys)

        self.program_loaded = \
            self.programs_available_dictionary[program_keys[program_index]]
        self.ip = 0

        return Program(self.program_loaded)

    def program_menu(self, program_list):
        """
        Create the text to display for the user to make a choice
        of which program to run.  Ask for that choice and return it.

        program_list = the dictionary keys from the
                       programs_available_dictionary
        """

        print_string = "\n\nHello, Dan.\n\n"
        print_string += ("My name is " + self.name
                         + ".\n\nI am capable of doing the following:")

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
    """
    This class retrieves a program's information from the programs
    available dictionary.
    """

    def __init__(self, program):
        self.program = program
        self.name = self.program['name']
        self.binary = self.program['binary']
        self.code = self.read_binary()
        self.copies = program['copies']
        self.input_sources = self.input_source(program)
        self.messages_in = self.message_in(program)
        self.messages_out = self.message_out(program)
        # self.input_sources = ''
        # self.messages_in = []
        # self.messages_out = []

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

    def input_source(self, program):
        if 'input_source' in program.keys():
            return program['input_source']

        return None

    def message_in(self, program):
        if 'message_in' in program.keys():
            return program['message_in']

        return None

    def message_out(self, program):
        if 'message_out' in program.keys():
            return program['message_out']

        return None


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
    def __init__(self, program=None):
        self.register = self.flash(program)

    def flash(self, program):
        mem_dict = {}

        if program is None:
            return {}

        code = program.code

        for i in range(len(code)):
            mem_dict[i] = code[i]

        return mem_dict

    def address(self, i):
        if i is None:
            return 'None'

        return self.register[i]


# %% CPU Class

class CPU:
    def __init__(self, instruction=None):
        self.instruction = instruction
        self.name = 'The Little Train That Could'

# # %%
#     def read_stack(self):
#         executable = stack.pop()

    def instruction_execute(self, memory, computer, instruction):
        if instruction is None:
            return instruction

        inst = instruction
        opcode = inst['opcode']
        par = inst['parameters']
        ip = computer.ip
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

# %% OpCode 3 - ask for input

    def opcode3(self, io, parameters, input_source):
        answer = int(input('Which System ID are we testing? '))
        memory.register[par[0]['address']] = answer
# #        self.prt0()

# #        self.memory[parameters[0]] = self.get_input(message)
#         if input_source == 'keyboard':
#             self.memory[parameters[0]] = \
#                 int(input('Which System ID are we testing? '))
# #        print(self.instruction_length)
#         self.instruction_pointer += self.get_instruction_length(code=3)
# #        self.instruction_pointer += self.instruction_length
        pass


# %% OpCode 4 - output a result

    def opcode4(self, parameters):
        print('Diagnostic Code = {:,d}'.format(par[0]['value']))
#         p1 = self.memory[self.address(0)]
#         if p1:
#             print('Diagnostic Code = {:,d}'.format(p1))
#         self.instruction_pointer += self.instruction_length

#         self.opcode = opcode
#         self.decode_opcode(self.instruction_pointer)
# #        self.decode_opcode()
#         if opcode == 3:
#             response = self.get_input(message)
# #        print(instruction[0], instruction[1:], opcode)
#         self.opcode_switch(instruction[0], instruction[1:], opcode)
        pass

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

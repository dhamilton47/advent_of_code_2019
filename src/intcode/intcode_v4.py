# -*- coding: utf-8 -*-
"""
Created on Sun Dec  22 15:49:41 2019

@author: Dan J Hamilton
"""

# from memory import Memory
# from program import Program


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
#         get_programs_available
#         load_program
#         initialize_memory
#         get_input
#         print_output
#         get_instruction
#         run_instruction

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
#         code
#         memory

#     Methods
#         create_dict
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
    def __init__(self, library):
        self.name = 'HAL'
        self.programs_available = library
        self.programs_running = []
        self.instruction_pointers = []

    def boot1(self, programID='None'):
        # program = Program()
        program = Program(programID)
        memory = Memory()
        instruction = Instruction(memory, opcode_dictionary)
        cpu = CPU()

        return memory, cpu
        # return program, memory, instruction, cpu

    def boot(self):
        memory = Memory()
        cpu = CPU()

        return memory, cpu
        # return program, memory, instruction, cpu

    def get_programs_available(self):
        return list(self.programs_available.keys())

    # def load_program(self, programID):
    def load_program(self):
        program_list = self.get_programs_available()
        print_string = "These are the programs we have available to execute:\n"

        for i in range(len(program_list)):
            if program_list[i] == "None":
                continue

            # next_line = str(i) + ". " + program_list[i] + "\n"
            print_string += "  " + str(i) + ". " + program_list[i] + "\n"
            # print_string += next_line

        print(f"{print_string}")
        # print(f"These are the programs we have available to execute:\n"
        #       f"1. {test.get_programs_available()[0]}\n")
        which_program = int(input('Which program are we running? '))

        return which_program

    def initialize_memory():
        pass

    def get_input():
        pass

    def print_output():
        pass

    def get_instruction():
        pass

    def run_instruction():
        pass


# %% Program Class

class Program:
    programs = {'Amp': {'name': 'Amplifier Controller',
                        'binary': '../data/adventofcode_2019_day_7_input1.txt'},
                'None': {'name': '',
                         'binary': ''}}

    def __init__(self, programID):
        self.programID = programID
        self.name = self.programs[programID]['name']
        self.binary = self.programs[programID]['binary']
        # self.code = []
        self.code = self.read_binary()
        # self.program = []
        # self.instruction_length_dict = {
        #     1: 4,
        #     2: 4,
        #     3: 2,
        #     4: 2,
        #     5: 3,
        #     6: 3,
        #     7: 4,
        #     8: 4,
        #     99: 1
        #     }
        self.instruction_pointer = 0
        # self.memory = Memory(self.code)
        # self.instruction = []
        # self.cpu = CPU(self.instruction)
        # self.instruction = Instruction(self.instruction_pointer, self.memory)
        # self.memory = self.initialize_memory()
        # self.memory_size = 0
        # self.txtfile = ''

    def read_binary(self, programID='None'):  #, binary=''):
        # print(self.programs.keys())
        # print(programID in self.programs.keys())
        if self.programID == 'None':
            if programID not in self.programs.keys():
                self.name = ''
                self.binary = ''
                return
            else:
                print('are we reaching')
                # print(self.programs[programID]['name'])
                # print(self.programs[programID]['binary'])
                self.name = self.programs[programID]['name']
                self.binary = self.programs[programID]['binary']

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

    def initialize_memory(self):
        memory_bank = Memory(self.code)

        return memory_bank

    def get_input(self):
        pass

    def get_instruction(self, ip, memory):
        return Instruction(ip, memory)
        raw_opcode = self.memory(self.instruction_pointer)

    def run_instruction(self, opcode):
        if opcode == 1:
            # Send to CPU
            self.cpu(self.parameters)
            self.opcode1(parameters)
        elif opcode == 2:
            # Send to CPU
            self.opcode2(parameters)
        elif opcode == 3:
            # Send to I/O
            self.opcode3(parameters)
        elif opcode == 4:
            # Send to I/O
            self.opcode4(parameters)
        elif opcode == 5:
            # Send to CPU
            self.opcode5(parameters)
        elif opcode == 6:
            # Send to CPU
            self.opcode6(parameters)
        elif opcode == 7:
            # Send to CPU
            self.opcode7(parameters)
        elif opcode == 8:
            # Send to CPU
            self.opcode8(parameters)
        elif opcode == 99:
            # Terminate Program Execution
            self.opcode99()
        else:
            print(str(100 * memory[ip] + memory[ip + 1]), 'program alarm')
            # print(str(100 * self.memory[self.instruction_pointer]
            #           + self.memory[self.instruction_pointer + 1]),
            #       'program alarm')
            self.instruction_pointer += 4


# %% Instruction Class


class Instruction:
    def __init__(self, memory, dictionary, ip=None):
        self.instruction = []
        self.instruction_length = 0
        self.raw_opcode = memory.address(ip)
        self.instruction_dict = dictionary
        self.opcode = self.instruction_dict[self.raw_opcode]['opcode']
        self.modes = self.instruction_dict[self.raw_opcode]['modes']
        self.parameters = self.instruction_dict[self.raw_opcode]['parameters']

        # self.instruction_dict = {
        #     1: {'opcode': 1,
        #         'length': 4,
        #         'function': 'add',
        #         'parameters': [0, 0, 0],
        #         'modes': ['position',
        #                   'position',
        #                   'position']},
        #     101: {'opcode': 1,
        #           'length': 4,
        #           'function': 'add',
        #           'parameters': [0, 0, 0],
        #           'modes': ['immediate',
        #                     'position',
        #                     'position']},
        #     1001: {'opcode': 1,
        #            'length': 4,
        #            'function': 'add',
        #            'parameters': [0, 0, 0],
        #            'modes': ['position',
        #                      'immediate',
        #                      'position']},
        #     1101: {'opcode': 1,
        #            'length': 4,
        #            'function': 'add',
        #            'parameters': [0, 0, 0],
        #            'modes': ['immediate',
        #                      'immediate',
        #                      'position']},
        #     10001: {'opcode': 1,
        #             'length': 4,
        #             'function': 'add',
        #             'parameters': [0, 0, 0],
        #             'modes': ['position',
        #                       'position',
        #                       'immediate']},
        #     10101: {'opcode': 1,
        #             'length': 4,
        #             'function': 'add',
        #             'parameters': [0, 0, 0],
        #             'modes': ['immediate',
        #                       'position',
        #                       'immediate']},
        #     11101: {'opcode': 1,
        #             'length': 4,
        #             'function': 'add',
        #             'parameters': [0, 0, 0],
        #             'modes': ['immediate',
        #                       'immediate',
        #                       'immediate']},
        #     2: {'opcode': 2,
        #         'length': 4,
        #         'function': 'multiply',
        #         'parameters': [0, 0, 0],
        #         'modes': ['position',
        #                   'position',
        #                   'position']},
        #     102: {'opcode': 2,
        #           'length': 4,
        #           'function': 'multiply',
        #           'parameters': [0, 0, 0],
        #           'modes': ['immediate',
        #                     'position',
        #                     'position']},
        #     1002: {'opcode': 2,
        #            'length': 4,
        #            'function': 'multiply',
        #            'parameters': [0, 0, 0],
        #            'modes': ['position',
        #                      'immediate',
        #                      'position']},
        #     1102: {'opcode': 2,
        #            'length': 4,
        #            'function': 'multiply',
        #            'parameters': [0, 0, 0],
        #            'modes': ['immediate',
        #                      'immediate',
        #                      'position']},
        #     10002: {'opcode': 2,
        #             'length': 4,
        #             'function': 'multiply',
        #             'parameters': [0, 0, 0],
        #             'modes': ['position',
        #                       'position',
        #                       'immediate']},
        #     10102: {'opcode': 2,
        #             'length': 4,
        #             'function': 'multiply',
        #             'parameters': [0, 0, 0],
        #             'modes': ['immediate',
        #                       'position',
        #                       'immediate']},
        #     11102: {'opcode': 2,
        #             'length': 4,
        #             'function': 'multiply',
        #             'parameters': [0, 0, 0],
        #             'modes': ['immediate',
        #                       'immediate',
        #                       'immediate']},
        #     3: {'opcode': 3,
        #         'length': 2,
        #         'function': 'input',
        #         'parameters': [0],
        #         'modes': ['position']},
        #     103: {'opcode': 3,
        #           'length': 2,
        #           'function': 'input',
        #           'parameters': [0],
        #           'modes': ['immediate']},
        #     4: {'opcode': 4,
        #         'length': 2,
        #         'function': 'output',
        #         'parameters': [0],
        #         'modes': ['position']},
        #     104: {'opcode': 4,
        #           'length': 2,
        #           'function': 'input',
        #           'parameters': [0],
        #           'modes': ['immediate']},
        #     5: {'opcode': 5,
        #         'length': 3,
        #         'function': 'jump-if-true',
        #         'parameters': [0, 0],
        #         'modes': ['position',
        #                   'position']},
        #     105: {'opcode': 5,
        #           'length': 3,
        #           'function': 'jump-if-true',
        #           'parameters': [0, 0],
        #           'modes': ['immediate',
        #                     'position']},
        #     1005: {'opcode': 5,
        #            'length': 3,
        #            'function': 'jump-if-true',
        #            'parameters': [0, 0],
        #            'modes': ['position',
        #                      'immediate']},
        #     1105: {'opcode': 5,
        #            'length': 3,
        #            'function': 'jump-if-true',
        #            'parameters': [0, 0],
        #            'modes': ['immediate',
        #                      'immediate']},
        #     6: {'opcode': 6,
        #         'length': 3,
        #         'function': 'jump-if-false',
        #         'parameters': [0, 0],
        #         'modes': ['position',
        #                   'position']},
        #     106: {'opcode': 6,
        #           'length': 3,
        #           'function': 'jump-if-false',
        #           'parameters': [0, 0],
        #           'modes': ['immediate',
        #                     'position']},
        #     1006: {'opcode': 6,
        #            'length': 3,
        #            'function': 'jump-if-false',
        #            'parameters': [0, 0],
        #            'modes': ['position',
        #                      'immediate']},
        #     1106: {'opcode': 6,
        #            'length': 3,
        #            'function': 'jump-if-false',
        #            'parameters': [0, 0],
        #            'modes': ['immediate',
        #                      'immediate']},
        #     7: {'opcode': 7,
        #         'length': 4,
        #         'function': 'less than',
        #         'parameters': [0, 0, 0],
        #         'modes': ['position',
        #                   'position',
        #                   'position']},
        #     107: {'opcode': 7,
        #           'length': 4,
        #           'function': 'less than',
        #           'parameters': [0, 0, 0],
        #           'modes': ['immediate',
        #                     'position',
        #                     'position']},
        #     1007: {'opcode': 7,
        #            'length': 4,
        #            'function': 'less than',
        #            'parameters': [0, 0, 0],
        #            'modes': ['position',
        #                      'immediate',
        #                      'position']},
        #     1107: {'opcode': 7,
        #            'length': 4,
        #            'function': 'less than',
        #            'parameters': [0, 0, 0],
        #            'modes': ['immediate',
        #                      'immediate',
        #                      'position']},
        #     10007: {'opcode': 7,
        #             'length': 4,
        #             'function': 'less than',
        #             'parameters': [0, 0, 0],
        #             'modes': ['position',
        #                       'position',
        #                       'immediate']},
        #     10107: {'opcode': 7,
        #             'length': 4,
        #             'function': 'less than',
        #             'parameters': [0, 0, 0],
        #             'modes': ['immediate',
        #                       'position',
        #                       'immediate']},
        #     11107: {'opcode': 7,
        #             'length': 4,
        #             'function': 'less than',
        #             'parameters': [0, 0, 0],
        #             'modes': ['immediate',
        #                       'immediate',
        #                       'immediate']},
        #     8: {'opcode': 8,
        #         'length': 4,
        #         'function': 'equals',
        #         'parameters': [0, 0, 0],
        #         'modes': ['position',
        #                   'position',
        #                   'position']},
        #     108: {'opcode': 8,
        #           'length': 4,
        #           'function': 'equals',
        #           'parameters': [0, 0, 0],
        #           'modes': ['immediate',
        #                     'position',
        #                     'position']},
        #     1008: {'opcode': 8,
        #            'length': 4,
        #            'function': 'equals',
        #            'parameters': [0, 0, 0],
        #            'modes': ['position',
        #                      'immediate',
        #                      'position']},
        #     1108: {'opcode': 8,
        #            'length': 4,
        #            'function': 'equals',
        #            'parameters': [0, 0, 0],
        #            'modes': ['immediate',
        #                      'immediate',
        #                      'position']},
        #     10008: {'opcode': 8,
        #             'length': 4,
        #             'function': 'equals',
        #             'parameters': [0, 0, 0],
        #             'modes': ['position',
        #                       'position',
        #                       'immediate']},
        #     10108: {'opcode': 8,
        #             'length': 4,
        #             'function': 'equals',
        #             'parameters': [0, 0, 0],
        #             'modes': ['immediate',
        #                       'position',
        #                       'immediate']},
        #     11108: {'opcode': 8,
        #             'length': 4,
        #             'function': 'equals',
        #             'parameters': [0, 0, 0],
        #             'modes': ['immediate',
        #                       'immediate',
        #                       'immediate']},
        #     99: {'opcode': 99,
        #          'length': 1,
        #          'function': 'exit',
        #          'parameters': [],
        #          'modes': []},
        #     'None': {'opcode': 'None',
        #              'length': 0,
        #              'function': 'none',
        #              'parameters': 'None',
        #              'modes': 'None'},
        #     }


# %% Memory Class

class Memory:
    def __init__(self, code=[]):
        # self.code = code
        self.memory = self.flash(code)

    # def create_dict(self):
    #     mem_dict = {}

    #     for i in range(len(self.code)):
    #         mem_dict[i] = self.code[i]

    #     return mem_dict

    def flash(self, code):
        mem_dict = {}

        for i in range(len(code)):
            mem_dict[i] = code[i]

        return mem_dict

    def address(self, i):
        if i is None:
            return 'None'
        return self.memory[i]
        # if self.parameter_modes[i] == 'position':
        #     return self.parameters[i]
        # else:
        #     return self.instruction_pointer + 1 + i


# %% CPU Class

class CPU:
    def __init__(self, instruction=[]):
        self.instruction = instruction
        self.name = 'The Little Train That Could'

# # %%
#     def read_stack(self):
#         executable = stack.pop()

#     def execute_instruction(self, instruction, message=''):
#         opcode = self.get_opcode(instruction[0])
#         self.opcode = opcode
#         self.decode_opcode(self.instruction_pointer)
# #        self.decode_opcode()
#         if opcode == 3:
#             response = self.get_input(message)
# #        print(instruction[0], instruction[1:], opcode)
#         self.opcode_switch(instruction[0], instruction[1:], opcode)

# %% OpCode 1 - add two values

    def opcode1(self, parameters):
        p1 = self.memory[self.address(0)]
        p2 = self.memory[self.address(1)]
        self.memory[parameters[2]] = self.add(p1, p2)
        self.instruction_pointer += self.instruction_length

# %% OpCode 2 - multiply two values

    def opcode2(self, parameters):
        p1 = self.memory[self.address(0)]
        p2 = self.memory[self.address(1)]
        self.memory[parameters[2]] = self.multiply(p1, p2)
        self.instruction_pointer += self.instruction_length

# %% OpCode 3 - ask for input

    def opcode3(self, parameters, input_source):
#        self.prt0()

#        self.memory[parameters[0]] = self.get_input(message)
        if input_source == 'keyboard':
            self.memory[parameters[0]] = \
                int(input('Which System ID are we testing? '))
#        print(self.instruction_length)
        self.instruction_pointer += self.get_instruction_length(code=3)
#        self.instruction_pointer += self.instruction_length


# %% OpCode 4 - output a result

    def opcode4(self, parameters):
        p1 = self.memory[self.address(0)]
        if p1:
            print('Diagnostic Code = {:,d}'.format(p1))
        self.instruction_pointer += self.instruction_length

# %% OpCode 5 - jump-if-true

    def opcode5(self, parameters):
        p1 = self.memory[self.address(0)]
        p2 = self.memory[self.address(1)]
        if p1:
            self.instruction_pointer = p2
        else:
            self.instruction_pointer += self.instruction_length

# %% OpCode 6 - jump-if-false

    def opcode6(self, parameters):
        p1 = self.memory[self.address(0)]
        p2 = self.memory[self.address(1)]
        if not(p1):
            self.instruction_pointer = p2
        else:
            self.instruction_pointer += self.instruction_length

# %% OpCode 7 - less than

    def opcode7(self, parameters):
        p1 = self.memory[self.address(0)]
        p2 = self.memory[self.address(1)]
        self.memory[parameters[2]] = 1 if p1 < p2 else 0
        self.instruction_pointer += self.instruction_length

# %% OpCode 8 - equals

    def opcode8(self, parameters):
        p1 = self.memory[self.address(0)]
        p2 = self.memory[self.address(1)]
        self.memory[parameters[2]] = 1 if p1 == p2 else 0
        self.instruction_pointer += self.instruction_length

# %% OpCode 99 - terminate program

    def opcode99(self):
        if self.memory[1] == 12 and self.memory[2] == 2:
            print('Day 2 - Part 1 - Output = {:,d}'.format(self.memory[0]))
        if self.memory[0] == 19690720:
            print('Day 2 - Part 2 - 100 * noun + verb = {}'
                  .format(100 * self.memory[1] + self.memory[2]))
            print('Day 2 - Part 2 - Check = {}'.format(self.memory[0]))

        self.instruction_pointer = len(self.memory)

# %% OpCode general form

    def opcode_generic(self, i):
        p = self.memory[self.address(i)]
        return p

    def add(i, j):
        return i + j

    def multiply(i, j):
        return i * j


# # %% Programs Dictionary

# programs_available_dictionary = {
#     'Amp': {'name': 'Amplifier Controller',
#             'binary': '../data/adventofcode_2019_day_7_input1.txt'},
#     'None': {'name': '',
#              'binary': ''}, }

# %% OpCode Dictionary

opcode_dictionary = {
            1: {'opcode': 1,
                'length': 4,
                'function': 'add',
                'parameters': [0, 0, 0],
                'modes': ['position',
                          'position',
                          'position']},
            101: {'opcode': 1,
                  'length': 4,
                  'function': 'add',
                  'parameters': [0, 0, 0],
                  'modes': ['immediate',
                            'position',
                            'position']},
            1001: {'opcode': 1,
                   'length': 4,
                   'function': 'add',
                   'parameters': [0, 0, 0],
                   'modes': ['position',
                             'immediate',
                             'position']},
            1101: {'opcode': 1,
                   'length': 4,
                   'function': 'add',
                   'parameters': [0, 0, 0],
                   'modes': ['immediate',
                             'immediate',
                             'position']},
            10001: {'opcode': 1,
                    'length': 4,
                    'function': 'add',
                    'parameters': [0, 0, 0],
                    'modes': ['position',
                              'position',
                              'immediate']},
            10101: {'opcode': 1,
                    'length': 4,
                    'function': 'add',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'position',
                              'immediate']},
            11101: {'opcode': 1,
                    'length': 4,
                    'function': 'add',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'immediate',
                              'immediate']},
            2: {'opcode': 2,
                'length': 4,
                'function': 'multiply',
                'parameters': [0, 0, 0],
                'modes': ['position',
                          'position',
                          'position']},
            102: {'opcode': 2,
                  'length': 4,
                  'function': 'multiply',
                  'parameters': [0, 0, 0],
                  'modes': ['immediate',
                            'position',
                            'position']},
            1002: {'opcode': 2,
                   'length': 4,
                   'function': 'multiply',
                   'parameters': [0, 0, 0],
                   'modes': ['position',
                             'immediate',
                             'position']},
            1102: {'opcode': 2,
                   'length': 4,
                   'function': 'multiply',
                   'parameters': [0, 0, 0],
                   'modes': ['immediate',
                             'immediate',
                             'position']},
            10002: {'opcode': 2,
                    'length': 4,
                    'function': 'multiply',
                    'parameters': [0, 0, 0],
                    'modes': ['position',
                              'position',
                              'immediate']},
            10102: {'opcode': 2,
                    'length': 4,
                    'function': 'multiply',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'position',
                              'immediate']},
            11102: {'opcode': 2,
                    'length': 4,
                    'function': 'multiply',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'immediate',
                              'immediate']},
            3: {'opcode': 3,
                'length': 2,
                'function': 'input',
                'parameters': [0],
                'modes': ['position']},
            103: {'opcode': 3,
                  'length': 2,
                  'function': 'input',
                  'parameters': [0],
                  'modes': ['immediate']},
            4: {'opcode': 4,
                'length': 2,
                'function': 'output',
                'parameters': [0],
                'modes': ['position']},
            104: {'opcode': 4,
                  'length': 2,
                  'function': 'input',
                  'parameters': [0],
                  'modes': ['immediate']},
            5: {'opcode': 5,
                'length': 3,
                'function': 'jump-if-true',
                'parameters': [0, 0],
                'modes': ['position',
                          'position']},
            105: {'opcode': 5,
                  'length': 3,
                  'function': 'jump-if-true',
                  'parameters': [0, 0],
                  'modes': ['immediate',
                            'position']},
            1005: {'opcode': 5,
                   'length': 3,
                   'function': 'jump-if-true',
                   'parameters': [0, 0],
                   'modes': ['position',
                             'immediate']},
            1105: {'opcode': 5,
                   'length': 3,
                   'function': 'jump-if-true',
                   'parameters': [0, 0],
                   'modes': ['immediate',
                             'immediate']},
            6: {'opcode': 6,
                'length': 3,
                'function': 'jump-if-false',
                'parameters': [0, 0],
                'modes': ['position',
                          'position']},
            106: {'opcode': 6,
                  'length': 3,
                  'function': 'jump-if-false',
                  'parameters': [0, 0],
                  'modes': ['immediate',
                            'position']},
            1006: {'opcode': 6,
                   'length': 3,
                   'function': 'jump-if-false',
                   'parameters': [0, 0],
                   'modes': ['position',
                             'immediate']},
            1106: {'opcode': 6,
                   'length': 3,
                   'function': 'jump-if-false',
                   'parameters': [0, 0],
                   'modes': ['immediate',
                             'immediate']},
            7: {'opcode': 7,
                'length': 4,
                'function': 'less than',
                'parameters': [0, 0, 0],
                'modes': ['position',
                          'position',
                          'position']},
            107: {'opcode': 7,
                  'length': 4,
                  'function': 'less than',
                  'parameters': [0, 0, 0],
                  'modes': ['immediate',
                            'position',
                            'position']},
            1007: {'opcode': 7,
                   'length': 4,
                   'function': 'less than',
                   'parameters': [0, 0, 0],
                   'modes': ['position',
                             'immediate',
                             'position']},
            1107: {'opcode': 7,
                   'length': 4,
                   'function': 'less than',
                   'parameters': [0, 0, 0],
                   'modes': ['immediate',
                             'immediate',
                             'position']},
            10007: {'opcode': 7,
                    'length': 4,
                    'function': 'less than',
                    'parameters': [0, 0, 0],
                    'modes': ['position',
                              'position',
                              'immediate']},
            10107: {'opcode': 7,
                    'length': 4,
                    'function': 'less than',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'position',
                              'immediate']},
            11107: {'opcode': 7,
                    'length': 4,
                    'function': 'less than',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'immediate',
                              'immediate']},
            8: {'opcode': 8,
                'length': 4,
                'function': 'equals',
                'parameters': [0, 0, 0],
                'modes': ['position',
                          'position',
                          'position']},
            108: {'opcode': 8,
                  'length': 4,
                  'function': 'equals',
                  'parameters': [0, 0, 0],
                  'modes': ['immediate',
                            'position',
                            'position']},
            1008: {'opcode': 8,
                   'length': 4,
                   'function': 'equals',
                   'parameters': [0, 0, 0],
                   'modes': ['position',
                             'immediate',
                             'position']},
            1108: {'opcode': 8,
                   'length': 4,
                   'function': 'equals',
                   'parameters': [0, 0, 0],
                   'modes': ['immediate',
                             'immediate',
                             'position']},
            10008: {'opcode': 8,
                    'length': 4,
                    'function': 'equals',
                    'parameters': [0, 0, 0],
                    'modes': ['position',
                              'position',
                              'immediate']},
            10108: {'opcode': 8,
                    'length': 4,
                    'function': 'equals',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'position',
                              'immediate']},
            11108: {'opcode': 8,
                    'length': 4,
                    'function': 'equals',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'immediate',
                              'immediate']},
            99: {'opcode': 99,
                 'length': 1,
                 'function': 'exit',
                 'parameters': [],
                 'modes': []},
            'None': {'opcode': 'None',
                     'length': 0,
                     'function': 'none',
                     'parameters': 'None',
                     'modes': 'None'},
            }
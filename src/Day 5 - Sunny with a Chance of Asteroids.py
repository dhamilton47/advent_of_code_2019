# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:32:44 2019

@author: Dan J Hamilton
"""

# import pandas as pd


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


# %% Define the IntCode class
class IntCode:

    def __init__(self, program):
        self.instruction = []
        self.instruction_length = 0
        self.instruction_length_dict = {1: 4,
                                        2: 4,
                                        3: 2,
                                        4: 2,
                                        99: 1}
        self.instruction_pointer = 0
        self.memory = program
        self.memory_length = 0
        self.noun = self.memory[1]
        self.opcode = 0
        self.parameters = []
        self.parameter_modes = []
        self.txtfile = txtfile
        self.verb = self.memory[2]

# %%
    def set_instruction(self):
        self.instruction = []
        self.instruction.append(self.memory[self.instruction_pointer])
        for i in range(1, self.instruction_length):
            self.instruction.append(self.memory[self.instruction_pointer + i])

# %%
    def set_instruction_length(self):
        self.instruction_length = self.instruction_length_dict[self.opcode] \
            if self.instruction_length_dict[self.opcode] else 0

# %%
    def set_opcode(self):
        return self.memory[self.instruction_pointer] % 100

# %%
    def set_parameter(self, i):
        return self.memory[(self.instruction_pointer + 1) + i]

# %%
    def set_parameters(self):
        self.parameters = []
        for i in range(self.instruction_length - 1):
            self.parameters.append(self.set_parameter(i))

# %%
    def set_parameter_mode(self, i):
        parameter_mode_matrix = {0: 'position', 1: 'immediate'}
        index = self.memory[self.instruction_pointer] // (10 * 10 ** i) % 10

        return parameter_mode_matrix[index]

# %%
    def set_parameter_modes(self):
        self.parameter_modes = []
        if self.opcode in set([3]):
            return
        elif self.opcode == 4:
            self.parameter_modes.append(self.set_parameter_mode(1))
        else:
            self.parameter_modes.append(self.set_parameter_mode(1))
            self.parameter_modes.append(self.set_parameter_mode(2))

# %%
    def address(self, i):
        if self.parameter_modes[i] == 'position':
            return self.parameters[i]
        else:
            return self.instruction_pointer + 1 + i

# %% Print Functions
    def prt0(self):
        print('IP = {}, Instruction = {}, OpCode = {}'
              .format(self.instruction_pointer, self.instruction, self.opcode))
        # print('OpCode = {}, Instruction length = {}, Parameters = {}'
        #       .format(self.opcode, self.instruction_length, self.parameters))

    def prt(self, i, pm, adr, val):
        print('\tV{}: Mode = {}, Address = {}, Value = {}'
              .format(i, pm, adr, val))
        # print('\tV{} mode = {}, V{} value = {}'
        #       .format(i + 1, self.parameter_modes[i],
        #               i + 1, self.parameters[i]))
        # print('\tIPCode: {}, OpCode: {}, vm{}: {}, v{}: {}'
        #       .format(self.memory[self.instruction_pointer],
        #               self.opcode, i + 1, self.parameter_modes[i],
        #               i + 1, self.parameters[i]))

    def prt1(self, x1, x2, x3):
        print('\t\tp1 = {}, p2 = {}, p3 = {} '.format(x1, x2, x3))

# %%
    def opcode1(self, parameters):
        mem = self.memory
#        ip = self.instruction_pointer
        pm1, pm2 = self.parameter_modes
#        v1, v2 = self.parameters[:2]

        adr1 = self.address(0)
        adr2 = self.address(1)
#        self.prt1(adr1, adr2, adr1 + adr2)
#        print('\t\tp1 = {}, p2 = {}'.format())
#        adr1 = mem[ip + 1] if pm1 == 'position' else mem[parameters[0]]
#        adr2 = mem[ip + 2] if pm2 == 'position' else mem[parameters[1]]

        p1 = mem[adr1]
        p2 = mem[adr2]
        # p1 = mem[parameters[0]] if pm1 == 'position' else mem[ip + 1]
        # p2 = mem[parameters[1]] if pm2 == 'position' else mem[ip + 2]

        # self.prt0()
        # self.prt(1, pm1, adr1, p1)
        # self.prt(2, pm2, adr2, p2)
        # self.prt(3, 'position', parameters[2], p1 + p2)
#        self.prt1(p1, p2, p1 + p2)
#        print('\t\tp1 = {}, p2 = {}'.format())

        self.memory[parameters[2]] = p1 + p2
        self.instruction_pointer += self.instruction_length
#        print('Value at Memory Location 224 =', self.memory[224])

# %%
    def opcode2(self, parameters):

        mem = self.memory
#        ip = self.instruction_pointer
        pm1, pm2 = self.parameter_modes
#        v1, v2 = self.parameters[:2]

        adr1 = self.address(0)
        adr2 = self.address(1)
#        self.prt1(adr1, adr2, adr1 * adr2)
#        print('\t\tp1 = {}, p2 = {}'.format(adr1, adr2))
#        adr1 = mem[ip + 1] if pm1 == 'position' else mem[parameters[0]]
#        adr2 = mem[ip + 2] if pm2 == 'position' else mem[parameters[1]]

        p1 = mem[adr1]
        p2 = mem[adr2]
        # p1 = mem[parameters[0]] if pm1 == 'position' else mem[ip + 1]
        # p2 = mem[parameters[1]] if pm2 == 'position' else mem[ip + 2]

        # self.prt0()
        # self.prt(1, pm1, adr1, p1)
        # self.prt(2, pm2, adr2, p2)
        # self.prt(3, 'position', parameters[2], p1 * p2)
        # self.prt(0)
        # self.prt(1)
#        self.prt1(p1, p2, p1 * p2)
#        print('\t\tp1 = {}, p2 = {}'.format(p1, p2))

        self.memory[parameters[2]] = p1 * p2
        self.instruction_pointer += self.instruction_length
#        print('Value at Memory Location 224 =', self.memory[224])

# %%
    def opcode3(self, parameters):
        self.prt0()
        # print('Value at Memory Location 224 =', self.memory[224])

        self.memory[parameters[0]] = \
            int(input('Which System ID are we testing? '))
        self.instruction_pointer += self.instruction_length

# %%
    def opcode4(self, parameters):

        mem = self.memory
        pm1 = self.parameter_modes[0]
#        v1 = self.parameters[0]

        adr1 = self.address(0)
        p1 = mem[adr1]

        # self.prt0()
        # self.prt(1, pm1, adr1, p1)
#        print('p1 = {}'.format(p1))

        if p1:
            print('Day 5 - Part 1 - Diagnostic Code = {:,d}'.format(p1))
        self.instruction_pointer += self.instruction_length
#        print('Value at Memory Location 224 =', self.memory[224])

# %%
    def opcode99(self):
        if self.memory[1] == 12 and self.memory[2] == 2:
            print('Day 2 - Part 1 - Output = {:,d}'.format(self.memory[0]))
        elif self.memory[0] == 19690720:
            print('Day 2 - Part 2 - 100 * noun + verb = {}'
                  .format(100 * self.memory[1] + self.memory[2]))
            print('Day 2 - Part 2 - Check = {}'.format(self.memory[0]))
        else:
            return
        self.instruction_pointer = len(self.memory)

# %%
    def decode_opcode(self):
        # Determine OpCode
        self.opcode = self.set_opcode()
        # op = self.opcode = m[ip] % 100

        # Determine instruction length
        self.set_instruction_length()
        # il = self.instruction_length

        # Set parameter modes
        self.set_parameter_modes()
        # pm = self.parameter_modes

        # Set parameters
        self.set_parameters()
        # p = self.parameters

        self.set_instruction()
        # self.instruction.append(self.memory[self.instruction_pointer])

        # self.prt0()
        # print('OpCode =', self.opcode, ' Instruction length =',
        # self.instruction_length, ' Parameters =', self.parameters)


        return self.opcode, self.parameters

# %%
    def run_program(self):
        memory_length = len(self.memory)
        while self.instruction_pointer < memory_length:
            opcode, parameters = self.decode_opcode()
            if opcode == 1:
                self.opcode1(parameters)
            elif opcode == 2:
                self.opcode2(parameters)
            elif opcode == 3:
                self.opcode3(parameters)
            elif opcode == 4:
                self.opcode4(parameters)
            elif opcode == 99:
                self.opcode99()
            else:
                print(str(100 * self.memory[self.instruction_pointer]
                          + self.memory[self.instruction_pointer + 1]),
                      'program alarm')
                self.instruction_pointer += 4


def preprocess_program():
    return


def TEST(self_initialize=True, noun=0, verb=0):

    txtfile = "../data/adventofcode_2019_day_5_input.txt" \
        if self_initialize else "../data/adventofcode_2019_day_2_input.txt"

    # Preprocess "program"
    program = read_program(txtfile)
    readable_program = transform_program(program)

    if not(self_initialize):
        readable_program[1] = noun
        readable_program[2] = verb

#    noun=225
#    verb=1
    intcode = IntCode(readable_program)
#    intcode = IntCode(txtfile, noun, verb, unit)
    intcode.run_program()


# %%

# temp = IntCode(txtfile="../data/adventofcode_2019_day_5_input.txt", noun=12, verb=2)
# temp.run_program()
# temp = IntCode(txtfile="../data/adventofcode_2019_day_5_input.txt", noun=95, verb=7)
# temp.run_program()

txtfile = "../data/adventofcode_2019_day_5_input.txt"
program = read_program(txtfile)
readable_program = transform_program(program)
temp = IntCode(readable_program)
temp.run_program()

# temp = IntCode(txtfile="../data/adventofcode_2019_day_5_input.txt", noun=225, verb=1)
# temp.read_program()
# temp.initialize_memory()

# TEST()
# TEST(self_initialize=False, noun=12, verb=2)
# TEST(self_initialize=False, noun=95, verb=7)

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:32:44 2019

@author: Dan J Hamilton
"""


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
                                        5: 3,
                                        6: 3,
                                        7: 4,
                                        8: 4,
                                        99: 1}
        self.instruction_pointer = 0
        self.memory = program
        self.memory_length = 0
        self.noun = self.memory[1]
        self.opcode = 0
        self.parameters = []
        self.parameter_modes = []
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

    def prt(self, i, pm, adr, val):
        print('\tV{}: Mode = {}, Address = {}, Value = {}'
              .format(i, pm, adr, val))

    def prt1(self, x1, x2, x3):
        print('\t\tp1 = {}, p2 = {}, p3 = {} '.format(x1, x2, x3))

# %% OpCode 1 - add two values
    def opcode1(self, parameters):
        mem = self.memory
        pm1, pm2 = self.parameter_modes

        adr1 = self.address(0)
        adr2 = self.address(1)

        p1 = mem[adr1]
        p2 = mem[adr2]

        self.memory[parameters[2]] = p1 + p2
        self.instruction_pointer += self.instruction_length

# %% OpCode 2 - multiply two values
    def opcode2(self, parameters):
        mem = self.memory
        pm1, pm2 = self.parameter_modes

        adr1 = self.address(0)
        adr2 = self.address(1)

        p1 = mem[adr1]
        p2 = mem[adr2]

        self.memory[parameters[2]] = p1 * p2
        self.instruction_pointer += self.instruction_length

# %% OpCode 3 - ask for input
    def opcode3(self, parameters):
        self.prt0()

        self.memory[parameters[0]] = \
            int(input('Which System ID are we testing? '))
        self.instruction_pointer += self.instruction_length

# %% OpCode 4 - output a result
    def opcode4(self, parameters):

        mem = self.memory

        adr1 = self.address(0)
        p1 = mem[adr1]

        if p1:
            print('Diagnostic Code = {:,d}'.format(p1))
        self.instruction_pointer += self.instruction_length
#        print('Value at Memory Location 224 =', self.memory[224])

# %% OpCode 5 - jump-if-true
    def opcode5(self, parameters):

        mem = self.memory
        pm1, pm2 = self.parameter_modes

        adr1 = self.address(0)
        adr2 = self.address(1)

        p1 = mem[adr1]
        p2 = mem[adr2]

        if p1:
            self.instruction_pointer = p2
        else:
            self.instruction_pointer += self.instruction_length

# %% OpCode 6 - jump-if-false
    def opcode6(self, parameters):
        mem = self.memory
        pm1, pm2 = self.parameter_modes

        adr1 = self.address(0)
        adr2 = self.address(1)

        p1 = mem[adr1]
        p2 = mem[adr2]

        if not(p1):
            self.instruction_pointer = p2
        else:
            self.instruction_pointer += self.instruction_length

# %% OpCode 7 - less than
    def opcode7(self, parameters):
        mem = self.memory
        pm1, pm2 = self.parameter_modes

        adr1 = self.address(0)
        adr2 = self.address(1)

        p1 = mem[adr1]
        p2 = mem[adr2]

        self.memory[parameters[2]] = 1 if p1 < p2 else 0
        self.instruction_pointer += self.instruction_length

# %% OpCode 8 - equals
    def opcode8(self, parameters):
        mem = self.memory
        pm1, pm2 = self.parameter_modes

        adr1 = self.address(0)
        adr2 = self.address(1)

        p1 = mem[adr1]
        p2 = mem[adr2]

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
            elif opcode == 5:
                self.opcode5(parameters)
            elif opcode == 6:
                self.opcode6(parameters)
            elif opcode == 7:
                self.opcode7(parameters)
            elif opcode == 8:
                self.opcode8(parameters)
            elif opcode == 99:
                self.opcode99()
            else:
                print(str(100 * self.memory[self.instruction_pointer]
                          + self.memory[self.instruction_pointer + 1]),
                      'program alarm')
                self.instruction_pointer += 4


def TEST(self_initialize=True, noun=0, verb=0):

    txtfile = "../data/adventofcode_2019_day_5_input.txt" \
        if self_initialize else "../data/adventofcode_2019_day_2_input.txt"

    # Preprocess "program"
    program = read_program(txtfile)
    readable_program = transform_program(program)

    if not(self_initialize):
        readable_program[1] = noun
        readable_program[2] = verb

    # Create IntCode instance
    intcode = IntCode(readable_program)

    # Run code
    intcode.run_program()


# %% Development Environment

# temp = IntCode(txtfile="../data/adventofcode_2019_day_5_input.txt",
# noun=12, verb=2)
# temp.run_program()
# temp = IntCode(txtfile="../data/adventofcode_2019_day_5_input.txt",
# noun=95, verb=7)
# temp.run_program()

# txtfile = "../data/adventofcode_2019_day_5_input.txt"
# program = read_program(txtfile)
# readable_program = transform_program(program)
# temp = IntCode(readable_program)
# temp.run_program()

# temp = IntCode(txtfile="../data/adventofcode_2019_day_5_input.txt",
# noun=225, verb=1)
# temp.read_program()
# temp.initialize_memory()


# %% Production Environment (LOL)

TEST()
# TEST(self_initialize=False, noun=12, verb=2)
# TEST(self_initialize=False, noun=95, verb=7)

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:32:44 2019

@author: Dan J Hamilton
"""


# from memory import Memory


# %% Define the IntCode class

class IntCode:

    def __init__(self):
        # def __init__(self, program):
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
        self.memory = []
        # self.memory = program
        self.memory_size = 0
#        self.noun = 0
        self.opcode = 0
        self.parameters = []
        self.parameter_modes = []
        self.txtfile = ''
#        self.verb = 0

    # def load_program(self, txtfile):
    #     memory1 = Memory()
    #     mem, memory_size = memory1.read_program(txtfile)
    #     self.memory = mem
    #     self.memory_size = memory_size
    #     # self.memory, self.memory_size = memory.read_program(txtfile)

# %%

    def read_program(self, txtfile):
        self.txtfile = txtfile

        f = open(txtfile, "r")
        if f.mode == 'r':
            contents = f.read()
            f.close()

        memory = list(contents.split(","))
        memory_size = len(memory)
        for i in range(memory_size):
            memory[i] = int(memory[i])

        self.memory = memory
        self.memory_size = memory_size
        
        return memory

# %%

    def get_input(self, message):
        return int(input(message))

# %%

    def set_instruction(self):
        self.instruction = []
        self.instruction.append(self.memory[self.instruction_pointer])
        for i in range(1, self.instruction_length):
            self.instruction.append(self.memory[self.instruction_pointer + i])

# %%

    def get_instruction(self, ip):
        opcode = self.set_opcode()
        instruction_length = self.get_instruction_length(opcode)
        self.instruction = self.memory[ip:ip + instruction_length]
        return self.instruction

# %%

    def set_instruction_length(self):
        dictionary = self.instruction_length_dict
        self.instruction_length = dictionary[self.opcode] \
            if dictionary[self.opcode] else 0

# %%

    def get_instruction_length(self, code):
        dictionary = self.instruction_length_dict
        return dictionary[code] if dictionary[code] else 0

# %%

    def set_opcode(self):
        return self.memory[self.instruction_pointer] % 100

# %%

    def get_opcode(self, ip):
        return ip % 100
#        return self.memory[ip] % 100

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
        p1 = self.memory[self.address(0)]
        p2 = self.memory[self.address(1)]
        self.memory[parameters[2]] = p1 + p2
        self.instruction_pointer += self.instruction_length

# %% OpCode 2 - multiply two values

    def opcode2(self, parameters):
        p1 = self.memory[self.address(0)]
        p2 = self.memory[self.address(1)]
        self.memory[parameters[2]] = p1 * p2
        self.instruction_pointer += self.instruction_length

# %% OpCode 3 - ask for input

    def opcode3(self, parameters):
#        self.prt0()

#        self.memory[parameters[0]] = self.get_input(message)
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

# %%
    def opcode_switch(self, ip, parameters, code):
        memory = self.memory

        if code == 1:
            self.opcode1(parameters)
        elif code == 2:
            self.opcode2(parameters)
        elif code == 3:
            self.opcode3(parameters)
        elif code == 4:
            self.opcode4(parameters)
        elif code == 5:
            self.opcode5(parameters)
        elif code == 6:
            self.opcode6(parameters)
        elif code == 7:
            self.opcode7(parameters)
        elif code == 8:
            self.opcode8(parameters)
        elif code == 99:
            self.opcode99()
        else:
            print(str(100 * memory[ip] + memory[ip + 1]), 'program alarm')
            # print(str(100 * self.memory[self.instruction_pointer]
            #           + self.memory[self.instruction_pointer + 1]),
            #       'program alarm')
            self.instruction_pointer += 4



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

#        self.set_instruction()

#        return self.opcode, self.parameters

# %%

    def execute_instruction(self, instruction, message=''):
        opcode = self.get_opcode(instruction[0])
        if opcode == 3:
            self.get_input(message)
        self.opcode = opcode
        self.decode_opcode()
#        print(instruction[0], instruction[1:], opcode)
        self.opcode_switch(instruction[0], instruction[1:], opcode)

# %%
    def run_program(self):
        memory = self.memory
        memory_size = self.memory_size
        ip = self.instruction_pointer
#        print(ip, memory_size)
#        memory_size = len(self.memory)
        while self.instruction_pointer < memory_size:
#        while self.instruction_pointer < memory_size:
            opcode, parameters = self.decode_opcode()
            self.opcode_switch(self.instruction_pointer, parameters, opcode)
            # if opcode == 1:
            #     self.opcode1(parameters)
            # elif opcode == 2:
            #     self.opcode2(parameters)
            # elif opcode == 3:
            #     self.opcode3(parameters)
            # elif opcode == 4:
            #     self.opcode4(parameters)
            # elif opcode == 5:
            #     self.opcode5(parameters)
            # elif opcode == 6:
            #     self.opcode6(parameters)
            # elif opcode == 7:
            #     self.opcode7(parameters)
            # elif opcode == 8:
            #     self.opcode8(parameters)
            # elif opcode == 99:
            #     self.opcode99()
            # else:
            #     print(str(100 * memory[ip] + memory[ip + 1]), 'program alarm')
            #     # print(str(100 * self.memory[self.instruction_pointer]
            #     #           + self.memory[self.instruction_pointer + 1]),
            #     #       'program alarm')
            #     self.instruction_pointer += 4

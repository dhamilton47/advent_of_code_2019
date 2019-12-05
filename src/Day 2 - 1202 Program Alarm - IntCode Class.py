# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:32:44 2019

@author: Dan J Hamilton
"""


class IntCode:

# %%
    def __init__(self, txtfile, noun, verb):
        self.address = 0
        self.contents = ''
        self.instruction = []
        self.instruction_pointer = 0
        self.memory = []
        self.memory_length = 0
        self.noun = noun
        self.opcode = self.address
        self.parameters = []
        self.txtfile = txtfile
        self.verb = verb

# %%
    def read_program(self):
        f = open(self.txtfile, "r")
        if f.mode == 'r':
            self.contents = f.read()
        f.close()

        return

# %%
    def initialize_memory(self, a, b):
        self.memory = list(self.contents.split(","))
        self.memory_length = len(self.memory)
        for i in range(self.memory_length):
            self.memory[i] = int(self.memory[i])
        self.memory[1] = a
        self.memory[2] = b

# %%
    def determine_opcode(self):
        return

# %%
    def determine_parameter_types(self):
        return 0

# %%
    def assign_paramters(self):
        if self.opcode in [1, 2]:
            return [self.memory[self.index_pointer] + 1,
                    self.memory[self.index_pointer] + 2,
                    self.memory[self.index_pointer] + 3]
        elif self.opcode in [3, 4]:
            return [self.memory[self.index_pointer] + 1]
        else:
            return []

# %%
    def set_address(self, index, value):
        self.address = value

# %%
    def get_address(self, index):
        return self.address

# %%
    def opcode1(self, var1, var2, var3):
        self.memory[var3] = self.memory[var1] + self.memory[var2]
        self.instruction_pointer += 4

# %%
    def opcode2(self, var1, var2, var3):
        self.memory[var3] = self.memory[var1] * self.memory[var2]
        self.instruction_pointer += 4

# %%
    def opcode3(self, var):
        self.memory[var] = input()

# %%
    def opcode4(self, var):
        print(self.memory[var])

# %%
    def opcode99(self):
        if self.memory[1] == 12 and self.memory[2] == 2:
            print('Day 2 - Part 1 - Output = {:,d}'.format(self.memory[0]))
        if self.memory[0] == 19690720:
            print('Day 2 - Part 2 - 100 * noun + verb = {}'
                  .format(100 * self.memory[1] + self.memory[2]))
            print('Day 2 - Part 2 - Check = {}'.format(self.memory[0]))
        self.instruction_pointer = len(self.memory)
        return

# %%
    def run_program(self):
        self.read_program()
        self.initialize_memory(self.noun, self.verb)
        while self.instruction_pointer < self.memory_length:
            m = self.memory
            ip = self.instruction_pointer
            opcode = m[ip]
            p1 = m[ip + 1]
            p2 = m[ip + 2]
            p3 = m[ip + 3]
            if opcode == 1:
                self.opcode1(p1, p2, p3)
            elif opcode == 2:
                self.opcode2(p1, p2, p3)
            elif opcode == 99:
                self.opcode99()
            else:
                print(str(100 * m[ip]
                      + m[ip + 1]), 'program alarm')
                self.instruction_pointer += 4


# %%

temp = IntCode(txtfile="../data/adventofcode_2019_day_2_input.txt", noun=12, verb=2)
temp.run_program()
temp = IntCode(txtfile="../data/adventofcode_2019_day_2_input.txt", noun=95, verb=7)
temp.run_program()

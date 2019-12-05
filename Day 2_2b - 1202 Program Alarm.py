# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:32:44 2019

@author: danha
"""


class IntCode:
    def __init__(self, instruction_length):
        self._contents = ''
        self._memory = []
        self._memory_length = 0
        self._instruction_length = instruction_length | 4
        self._number_of_instructions = 0
        self._instructions = []

    def read_intcode(self, txtfile):
        f = open(txtfile, "r")
        if f.mode == 'r':
            self._contents = f.read()

    def get_instruction_length(self):
        return self._instruction_length

    def set_memory(self):
        self._memory = list(self._contents.split(","))
        self._memory_length = len(self._memory)
        for i in range(self._memory_length):
            self._memory[i] = int(self._memory[i])

    def get_memory(self):
        return self._memory

    def get_memory_length(self):
        return self._memory_length

    def get_number_of_instructions(self):
        return self._number_of_instructions

    def set_number_of_instructions(self):
        x = self._memory_length
        n = self._instruction_length
        self._number_of_instructions = x // n

    def set_address(self, index, value):
        self._memory[index] = value

    def get_address(self, index):
        return self._memory[index]

    def initialize_instructions(self):
        """
        This function initializes a m x n dimensional array
        """
        m = self._number_of_instructions
        n = self._instruction_length
        self._instructions = [[0] * n for i in range(m)]
#        for i in range(m):
#            print(self._instructions[i])

    def set_instructions(self):
        """
        This function rearranges the program input into an array
        of instructions
        """
        m = self._number_of_instructions
        n = self._instruction_length
#        print('m = ', m, 'n = ', n)

        for i in range(m):
            for j in range(n):
                self._instructions[i][j] = self._memory[(i * 4) + j]
#            print(self._instructions[i])

    def print_instructions(self):
        m = self._number_of_instructions
        z = self._instructions
        for i in range(m):
            print(z[i])


temp = IntCode(instruction_length=4)
temp.read_intcode(txtfile="./data/adventofcode_2019_day_2_input.txt")
# print(temp.get_instruction_length())
temp.set_memory()
# print(temp.get_memory())
# print(temp.get_address(116))
temp.set_number_of_instructions()
temp.initialize_instructions()
# temp.print_instructions()
temp.set_instructions()
temp.print_instructions()
# print(temp._instructions)


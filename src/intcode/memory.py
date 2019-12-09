# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:32:44 2019

@author: Dan J Hamilton
"""


class Memory:
    def __init__(self):
        self.instruction_pointer = 0
        self.memory = []
        # self.memory = program
        self.memory_size = 0
#        self.noun = 0
        self.txtfile = ''
#        self.verb = 0

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
#        print([memory, memory_size])
#        print(list([memory, memory_size]))
        return [memory, memory_size]
#        return list([memory, memory_size])

    def read_address(self, address):
        return self.memory[address]

    def write_address(self, address, value):
        self.memory[address] = value

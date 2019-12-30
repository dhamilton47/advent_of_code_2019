# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:50 2019

@author: Dan J Hamilton
"""


import aoc


# class Instruction
#     Properties
#         instruction
#         instruction_length
#         raw_opcode
#         instruction_dict
#         opcode
#         modes
#         parameters


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

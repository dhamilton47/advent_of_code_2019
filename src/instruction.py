# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:50 2019

@author: Dan J Hamilton

"""


import aoc


# %% Instruction Class

class Instruction:
    """
    An Instruction is the smallest element of code derived from a Program
    which the CPU is able to execute.

    class Instruction
        Properties
            raw_opcode
            opcode
            length
            parameters
            modes
            instruction

        Methods
            decode_parameters
    """

    def __init__(self, computer, op_dictionary=aoc.OPCODE_DICTIONARY,
                 mode_dictionary=aoc.MODE_DICTIONARY):
        self.raw_opcode = computer.memory.value(
            computer.ip)
        self.opcode = op_dictionary[self.raw_opcode % 100]['opcode']
        self.length = op_dictionary[self.raw_opcode % 100]['length']
        self.function = op_dictionary[self.raw_opcode % 100]['func']
        self.parameters = op_dictionary[self.raw_opcode % 100]['params']
        self.modes = mode_dictionary[self.raw_opcode // 100]['modes']
        self.instruction = {'opcode': self.opcode,
                            'parameters': self.decode_parameters(
                                computer.memory,
                                self.length,
                                computer.ip),
                            'length': self.length}

    def decode_parameters(self, memory, length, ip):
        """
        The OpCode of each instruction contains information which
        mutates the meaning of each parameter.  This information needs
        to be evaluated so that the parameters provide consistent
        structure for exectution.

        mode value 0 = position
        mode value 1 = immediate
        mode value 2 = relative
        """

        if length == 1:
            return {}

        parameters = {}

        for index in range(length - 1):
            if self.modes[index] == 0:
                address = memory.value((ip + 1) + index)
            elif self.modes[index] == 1:
                address = (ip + 1) + index
            elif self.modes[index] == 2:
                address = memory.value((ip + 1) + index) \
                    + memory.base_offset
            else:
                raise ValueError("Parameter mode is undefined.")

            value = memory.value(address)

            parameters[index] = {'address': address, 'value': value}

        return parameters

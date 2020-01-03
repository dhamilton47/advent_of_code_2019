# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:50 2019

@author: Dan J Hamilton
"""


import aoc


# class Instruction
#     Properties
#         raw_opcode
#         opcode
#         modes
#         parameters
#         length
#         instruction
#
#     Methods
#         decode_parameters


# %% Instruction Class

class Instruction:
    """
    An Instruction is the smallest element of code derived from a Program
    which the CPU is able to execute.
    """

    def __init__(self, computer, dictionary=aoc.OPCODE_DICTIONARY):
        self.raw_opcode = computer.memory.value(
            computer.process_active, computer.ips[computer.process_active])
        self.opcode = dictionary[self.raw_opcode]['opcode']
        self.modes = dictionary[self.raw_opcode]['modes']
        self.parameters = dictionary[self.raw_opcode]['parameters']
        self.length = dictionary[self.raw_opcode]['length']
        self.instruction = {'opcode': self.opcode,
                            'parameters': self.decode_parameters(
                                computer.process_active,
                                computer.memory,
                                self.length,
                                computer.ips[computer.process_active]),
                            'length': self.length}

    def decode_parameters(self, program_name, memory, length, ip):
        """
        The OpCode of each instruction contains information which
        mutates the meaning of each parameter.  This information needs
        to be evaluated so that the parameters provide consistent
        structure for exectution.
        """

        if length == 1:
            return {}

        parameters = {}

        for index in range(length - 1):
            if self.modes[index] == 'position':
                address = memory.value(program_name, (ip + 1) + index)
            else:
                address = (ip + 1) + index

            value = memory.value(program_name, address)

            parameters[index] = {'address': address, 'value': value}

        return parameters

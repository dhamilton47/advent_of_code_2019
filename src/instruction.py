# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:50 2019

@author: Dan J Hamilton

"""


# %% Instruction Class

class Instruction:
    """
    An Instruction is the smallest element of code derived from a Program
    which the CPU is able to execute.

    class Instruction
        Properties
            opcode
            instruction

        Methods
            construct_instruction
            decode_parameters
            ip_next
    """


# %% Dictionary Globals

    opcode_dictionary = {
        1: {
            'opcode': 1,
            'instruction length': 4,
            'func': 'ADD',
            'params': {
                0: {'address': 0, 'value': 0},
                1: {'address': 0, 'value': 0},
                2: {'address': 0, 'value': 0},
                },
            },
        2: {
            'opcode': 2,
            'instruction length': 4,
            'func': 'MUL',
            'params': {
                0: {'address': 0, 'value': 0},
                1: {'address': 0, 'value': 0},
                2: {'address': 0, 'value': 0},
                },
            },
        3: {
            'opcode': 3,
            'instruction length': 2,
            'func': 'INPUT',
            'params': {
                0: {'address': 0, 'value': 0},
                },
            },
        4: {
            'opcode': 4,
            'instruction length': 2,
            'func': 'OUTPUT',
            'params': {
                0: {'address': 0, 'value': 0},
                },
            },
        5: {
            'opcode': 5,
            'instruction length': 3,
            'func': 'JIT',
            'params': {
                0: {'address': 0, 'value': 0},
                1: {'address': 0, 'value': 0},
                },
            },
        6: {
            'opcode': 6,
            'instruction length': 3,
            'func': 'JIF',
            'params': {
                0: {'address': 0, 'value': 0},
                1: {'address': 0, 'value': 0},
                },
            },
        7: {
            'opcode': 7,
            'instruction length': 4,
            'func': 'LT',
            'params': {
                0: {'address': 0, 'value': 0},
                1: {'address': 0, 'value': 0},
                2: {'address': 0, 'value': 0},
                },
            },
        8: {
            'opcode': 8,
            'instruction length': 4,
            'func': 'EQ',
            'params': {
                0: {'address': 0, 'value': 0},
                1: {'address': 0, 'value': 0},
                2: {'address': 0, 'value': 0},
                },
            },
        9: {
            'opcode': 9,
            'instruction length': 2,
            'func': 'REBASE',
            'params': {
                0: {'address': 0, 'value': 0},
                 },
            },
        99: {
            'opcode': 99,
            'instruction length': 1,
            'func': 'EXIT',
            'params': {}
            },
    }

    mode_dictionary = {
        0: {'modes': [0, 0, 0]},
        1: {'modes': [1, 0, 0]},
        2: {'modes': [2, 0, 0]},
        10: {'modes': [0, 1, 0]},
        11: {'modes': [1, 1, 0]},
        12: {'modes': [2, 1, 0]},
        20: {'modes': [0, 2, 0]},
        21: {'modes': [1, 2, 0]},
        22: {'modes': [2, 2, 0]},
        100: {'modes': [0, 0, 1]},
        101: {'modes': [1, 0, 1]},
        102: {'modes': [2, 0, 1]},
        110: {'modes': [0, 1, 1]},
        111: {'modes': [1, 1, 1]},
        112: {'modes': [2, 1, 1]},
        120: {'modes': [0, 2, 1]},
        121: {'modes': [1, 2, 1]},
        122: {'modes': [2, 2, 1]},
        200: {'modes': [0, 0, 2]},
        201: {'modes': [1, 0, 2]},
        202: {'modes': [2, 0, 2]},
        210: {'modes': [0, 1, 2]},
        211: {'modes': [1, 1, 2]},
        212: {'modes': [2, 1, 2]},
        220: {'modes': [0, 2, 2]},
        221: {'modes': [1, 2, 2]},
        222: {'modes': [2, 2, 2]},
    }

    def __init__(self, computer):
        self.opcode = computer.memory.value(computer.ip) % 100
        self.instruction = {
            'opcode': self.opcode,
            'parameters': self.construct_instruction(
                self.opcode,
                computer.ip,
                computer.memory),
            'next_ip': self.ip_next(computer.ip)
            }

    def construct_instruction(self, opcode, ip, memory):
        opcode = self.opcode_dictionary[opcode]['opcode']
        parameters = self.opcode_dictionary[opcode]['params']
        modes = self.mode_dictionary[memory.value(ip) // 100]['modes']

        parameters = self.decode_parameters(
            memory,
            parameters,
            modes,
            ip)

        return parameters

    def decode_parameters(self, memory, parameters, modes, ip):
        """
        The OpCode of each instruction contains information which
        mutates the meaning of each parameter.  This information needs
        to be evaluated so that the parameters provide consistent
        structure for execution.

        mode value 0 = position
        mode value 1 = immediate
        mode value 2 = relative
        """

        if len(parameters) == 0:
            return {}

        for index in parameters:
            address = [
                memory.value((ip + 1) + index),
                (ip + 1) + index,
                memory.value((ip + 1) + index)
                + memory.base_offset][modes[index]]

            value = memory.value(address)

            parameters[index] = {'address': address, 'value': value}

        return parameters

    def ip_next(self, ip):
        length = self.opcode_dictionary[self.opcode]['instruction length']

        return ip + length

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:21 2019

@author: Dan J Hamilton
"""


import sys


# class CPU
#     Properties
#         instruction
#         name
#
#     Methods
#         instruction_execute
#         add
#         multiply


# %% CPU Class

class CPU:
    """
    The CPU is where the Instructions are executed.
    """

    def __init__(self, instruction=None):
        self.instruction = instruction
        self.name = 'The Little Train That Could'
        self.print_flag = False

    def instruction_execute(self, computer, instruction):
        """ Execute the Instruction """

        self.instruction = instruction

        print_flag = self.print_flag

        if instruction is None:
            return instruction

        inst = instruction
        opcode = inst['opcode']
        par = inst['parameters']
        memory = computer.memory
        io = computer.io
        ip = computer.ip
        # print(f"Instruction is {inst}")
        # print(f"Parameters are {par}")
        if 0 in par.keys():
            adr0 = par[0]['address']
            # print(adr0)
            val0 = par[0]['value']
            # print(f"Address = {adr0}, value = {val0}")

        if 1 in par.keys():
            adr1 = par[1]['address']
            val1 = par[1]['value']

        if 2 in par.keys():
            adr2 = par[2]['address']
            val2 = par[2]['value']

        # print(f"\nInstruction (in CPU Module): {inst}")

        if opcode == 1:
            memory.bank[adr2] = self.add(val0, val1)

            if print_flag:
                print(f"ADD({val0}, {val1}) = {memory.bank[adr2]}")

            # memory.bank[par[2]['address']] = \
            #     self.add(par[0]['value'], par[1]['value'])

            # if print_flag:
            #     print(f"ADD({par[0]['value']}, {par[1]['value']}) = "
            #           f"{memory.bank[par[2]['address']]}")

        elif opcode == 2:
            memory.bank[adr2] = \
                self.multiply(val0, val1)

            if print_flag:
                print(f"MUL({val0}, {val1}) = {memory.bank[adr2]}")

            # memory.bank[par[2]['address']] = \
            #     self.multiply(par[0]['value'], par[1]['value'])

            # if print_flag:
            #     print(f"MUL({par[0]['value']}, {par[1]['value']}) = "
            #           f"{memory.bank[par[2]['address']]}")

        elif opcode == 3:
            # answer = io.get_input(computer)
            memory.bank[adr0] = io.get_input(computer)

            # answer = io.get_input(computer)
            # memory.bank[par[0]['address']] = answer

            if print_flag:
                print(f"INPUT")

        elif opcode == 4:
            io.return_output(computer, instruction)

            if print_flag:
                print(f"OUTPUT")

        elif opcode == 5:
            if val0:
                inst['length'] = val1 - ip

            if print_flag:
                print(f"JIT = {['False', 'True'][val0 != 0]}")

            # if par[0]['value']:
            #     inst['length'] = par[1]['value'] - ip

            # if print_flag:
            #     print(f"JUMP = {['True', 'False'][par[0]['value'] != 0]}")

        elif opcode == 6:
            if val0 == 0:
                inst['length'] = val1 - ip

            if print_flag:
                print(f"JIF = {['True', 'False'][val0 == 0]}")

            # if par[0]['value'] == 0:
            #     inst['length'] = par[1]['value'] - ip

            # if print_flag:
            #     print(f"JUMP = {['True', 'False'][par[0]['value'] == 0]}")

        elif opcode == 7:
            # print(val0, val1)
            memory.bank[adr2] = \
                1 if val0 < val1 else 0

            if print_flag:
                print(f"LT({val0}, {val1}) = {memory.bank[adr2]}")

            # memory.bank[par[2]['address']] = \
            #     1 if par[0]['value'] < par[1]['value'] else 0

            # if print_flag:
            #     print(f"LT({par[0]['value']}, {par[1]['value']}) = "
            #           f"{memory.bank[par[2]['address']]}")

        elif opcode == 8:
            memory.bank[adr2] = \
                1 if val0 == val1 else 0

            if print_flag:
                print(f"EQ({val0}, {val1}) = {memory.bank[adr2]}")

            # memory.bank[par[2]['address']] = \
            #     1 if par[0]['value'] == par[1]['value'] else 0

            # if print_flag:
            #     print(f"EQ({par[0]['value']}, {par[1]['value']}) = "
            #           f"{memory.bank[par[2]['address']]}")

        elif opcode == 9:
            computer.memory.base_offset += val0

            if print_flag:
                print(f"REBASE = {val0}")

            # computer.memory.base_offset += par[0]['value']

            # if print_flag:
            #     print(f"REBASE = {par[0]['value']}")

        elif opcode == 99:
            if print_flag:
                print(f"EXIT")

            # Terminate Program Execution
            return inst

        else:
            print(str(100 * memory.bank(ip) + memory.bank(ip + 1)),
                  'program alarm')
            sys.exit()

        return inst

    def add(self, i, j):
        """ Add two operands """

        return i + j

    def multiply(self, i, j):
        """ Multiply two operands """

        return i * j

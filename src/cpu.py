# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:21 2019

@author: Dan J Hamilton
"""


import sys


# %% CPU Class

class CPU:
    """
    The CPU is where the Instructions are executed.

    class CPU
        Properties
            instruction
            name
            print_flag

        Methods
            instruction_execute(computer, instruction)
    """

    def __init__(self):
        self.instruction = None
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
            # adr1 = par[1]['address']
            val1 = par[1]['value']

        if 2 in par.keys():
            adr2 = par[2]['address']
            # val2 = par[2]['value']

        # print(f"\nInstruction (in CPU Module): {inst}")

        if opcode == 1:
            memory.bank[adr2] = val0 + val1

            if print_flag:
                print(f"ADD({val0}, {val1}) = {memory.bank[adr2]}"
                      f" stored at address {adr2}")

        elif opcode == 2:
            memory.bank[adr2] = val0 * val1

            if print_flag:
                print(f"MUL({val0}, {val1}) = {memory.bank[adr2]}"
                      f" stored at address {adr2}")

        elif opcode == 3:
            memory.bank[adr0] = io.get_input()

            if print_flag:
                print(f"INPUT: value = {memory.bank[adr0]}"
                      f" stored at address {adr0}")

        elif opcode == 4:
            io.return_output(instruction)

            if print_flag:
                print(f"OUTPUT")

        elif opcode == 5:
            if val0 != 0:
                inst['next_ip'] = val1

            if print_flag:
                print(f"JIT = {['False', 'True'][val0 != 0]}"
                      f", next IP = {inst['next_ip']}")

        elif opcode == 6:
            if val0 == 0:
                inst['next_ip'] = val1

            if print_flag:
                print(f"JIF = {['True', 'False'][val0 == 0]}"
                      f", next IP = {inst['next_ip']}")

        elif opcode == 7:
            memory.bank[adr2] = 1 if val0 < val1 else 0

            if print_flag:
                print(f"LT({val0}, {val1}) = {memory.bank[adr2]}"
                      f" stored at address {adr2}")

        elif opcode == 8:
            memory.bank[adr2] = 1 if val0 == val1 else 0

            if print_flag:
                print(f"EQ({val0}, {val1}) = {memory.bank[adr2]}"
                      f" stored at address {adr2}")

        elif opcode == 9:
            computer.memory.base_offset += val0

            if print_flag:
                print(f"REBASE now = {computer.memory.base_offset}")

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

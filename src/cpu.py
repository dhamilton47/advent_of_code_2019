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

# Need to change such that cpu interfaces with stack only.
# Need to see how this will work with IO

class CPU:
    """
    The CPU is where the Instructions are executed.
    """

    def __init__(self, instruction=None):
        self.instruction = instruction
        self.name = 'The Little Train That Could'

# # %%
#     def read_stack(self):
#         executable = stack.pop()

    def instruction_execute(self, computer, program, memory, io, instruction):
        if instruction is None:
            return instruction

        inst = instruction
        opcode = inst['opcode']
        par = inst['parameters']
        ip = computer.ip

        if opcode == 1:
            memory.bank[par[2]['address']] = \
                self.add(par[0]['value'], par[1]['value'])

        elif opcode == 2:
            memory.bank[par[2]['address']] = \
                self.multiply(par[0]['value'], par[1]['value'])

        elif opcode == 3:
            answer = io.get_input(program)
            memory.bank[par[0]['address']] = answer

        elif opcode == 4:
            io.return_output(program, instruction)

        elif opcode == 5:
            if par[0]['value']:
                inst['length'] = par[1]['value'] - ip

        elif opcode == 6:
            if par[0]['value'] == 0:
                inst['length'] = par[1]['value'] - ip

        elif opcode == 7:
            memory.bank[par[2]['address']] = \
                1 if par[0]['value'] < par[1]['value'] else 0

        elif opcode == 8:
            memory.bank[par[2]['address']] = \
                1 if par[0]['value'] == par[1]['value'] else 0

        elif opcode == 9:
            pass


        elif opcode == 99:
            # Terminate Program Execution
            return inst

        else:
            print(str(100 * memory.bank(ip) + memory.bank(ip + 1)),
                  'program alarm')
            sys.exit()

        return inst

    def instruction_execute1(self, computer, instruction):
        if instruction is None:
            return instruction

        inst = instruction
        opcode = inst['opcode']
        par = inst['parameters']
        process_active = computer.process_active
        memory = computer.memory
        io = computer.io
        ip = computer.ips[process_active]
        print(f"Instruction (in CPU Module): {inst}")

        # print(f"instruction = {instruction}")
        if opcode == 1:
            memory.bank[process_active][par[2]['address']] = \
                self.add(par[0]['value'], par[1]['value'])

        elif opcode == 2:
            print(F"value = {par[0]['value']}, value2 = {par[1]['value']}")
            memory.bank[process_active][par[2]['address']] = \
                self.multiply(par[0]['value'], par[1]['value'])

        elif opcode == 3:
            answer = io.get_input(computer)
            # print(par[0]['address'], answer)
            memory.bank[process_active][par[0]['address']] = answer

        elif opcode == 4:
            io.return_output(computer, instruction)

        elif opcode == 5:
            if par[0]['value']:
                inst['length'] = par[1]['value'] - ip

        elif opcode == 6:
            if par[0]['value'] == 0:
                inst['length'] = par[1]['value'] - ip

        elif opcode == 7:
            memory.bank[process_active][par[2]['address']] = \
                1 if par[0]['value'] < par[1]['value'] else 0

        elif opcode == 8:
            memory.bank[process_active][par[2]['address']] = \
                1 if par[0]['value'] == par[1]['value'] else 0

        elif opcode == 9:
            return inst

        elif opcode == 99:
            # Terminate Program Execution
            return inst

        else:
            print(str(100 * memory.bank(ip) + memory.bank(ip + 1)),
                  'program alarm')
            sys.exit()

        return inst

    def add(self, i, j):
        return i + j

    def multiply(self, i, j):
        return i * j


# %% CPU Class

# Need to change such that cpu interfaces with stack only.
# Need to see how this will work with IO

class CPU1:
    def __init__(self, instruction=None):
        self.instruction = instruction
        self.name = 'The Little Train That Could'

# # %%
#     def read_stack(self):
#         executable = stack.pop()

    def instruction_execute1(self, computer, program, memory, io, instruction):
        if instruction is None:
            return instruction

        inst = instruction
        opcode = inst['opcode']
        par = inst['parameters']
        process_active = computer.process_active
        memory = computer.memory
        io = computer.io
        ip = computer.ips[process_active]

        if opcode == 1:
            memory.register[process_active][par[2]['address']] = \
                self.add(par[0]['value'], par[1]['value'])
        elif opcode == 2:
            memory.register[process_active][par[2]['address']] = \
                self.multiply(par[0]['value'], par[1]['value'])
        elif opcode == 3:
            answer = io.get_input(program)
            memory.register[process_active][par[0]['address']] = answer
        elif opcode == 4:
            io.return_output(program, instruction)
        elif opcode == 5:
            if par[0]['value']:
                inst['length'] = par[1]['value'] - ip
        elif opcode == 6:
            if par[0]['value'] == 0:
                inst['length'] = par[1]['value'] - ip
        elif opcode == 7:
            memory.register[process_active][par[2]['address']] = \
                1 if par[0]['value'] < par[1]['value'] else 0
        elif opcode == 8:
            memory.register[process_active][par[2]['address']] = \
                1 if par[0]['value'] == par[1]['value'] else 0
        elif opcode == 99:
            # Terminate Program Execution
            return inst
        else:
            print(str(100 * memory.address(ip) + memory.address(ip + 1)),
                  'program alarm')
            sys.exit()

        return inst

    def add(self, i, j):
        return i + j

    def multiply(self, i, j):
        return i * j

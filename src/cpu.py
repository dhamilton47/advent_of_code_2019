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

#     Methods
#         opcode1
#         opcode2
#         opcode3
#         opcode4
#         opcode5
#         opcode6
#         opcode7
#         opcode8
#         opcode99
#         opcode_generic
#         add
#         multiply


# %% CPU Class

class CPU:
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
        # print(par)
        # length = inst['length']

        if opcode == 1:
            memory.register[par[2]['address']] = \
                self.add(par[0]['value'], par[1]['value'])
        elif opcode == 2:
            memory.register[par[2]['address']] = \
                self.multiply(par[0]['value'], par[1]['value'])
        elif opcode == 3:
            answer = io.get_input(program)
            # print(answer)
            # answer = int(input('Which System ID are we testing? '))
            memory.register[par[0]['address']] = answer
            # memory[par[0]['address']] = \
            #     int(input('Which System ID are we testing? '))
        elif opcode == 4:
            print('Diagnostic Code = {:,d}'.format(par[0]['value']))
        elif opcode == 5:
            if par[0]['value']:
                inst['length'] = par[1]['value'] - ip
        elif opcode == 6:
            if par[0]['value'] == 0:
                inst['length'] = par[1]['value'] - ip
        elif opcode == 7:
            memory.register[par[2]['address']] = \
                1 if par[0]['value'] < par[1]['value'] else 0
        elif opcode == 8:
            memory.register[par[2]['address']] = \
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

# %% OpCode 3 - ask for input

    def opcode3(self, io, parameters, input_source):
        answer = int(input('Which System ID are we testing? '))
        memory.register[par[0]['address']] = answer
# #        self.prt0()

# #        self.memory[parameters[0]] = self.get_input(message)
#         if input_source == 'keyboard':
#             self.memory[parameters[0]] = \
#                 int(input('Which System ID are we testing? '))
# #        print(self.instruction_length)
#         self.instruction_pointer += self.get_instruction_length(code=3)
# #        self.instruction_pointer += self.instruction_length
        pass


# %% OpCode 4 - output a result

    def opcode4(self, parameters):
        print('Diagnostic Code = {:,d}'.format(par[0]['value']))
#         p1 = self.memory[self.address(0)]
#         if p1:
#             print('Diagnostic Code = {:,d}'.format(p1))
#         self.instruction_pointer += self.instruction_length


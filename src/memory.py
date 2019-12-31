# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:46 2019

@author: Dan J Hamilton
"""

# class Memory
#     Properties
#         buffer
#         register
#
#     Methods
#         flash
#         address


# %% Memory Class

class Memory:
    def __init__(self, program=None):
        self.register = self.flash(program)

    def flash(self, program):
        mem_dict = {}

        if program is None:
            return {}

        # print(f"Program at Memory: {program}")
        for item in program:
            # print(f"item = {item}\n")
            # print(f"item.code = {program[item].code}\n")
            code = program[item].code

            for i in range(len(code)):
                mem_dict[i] = code[i]

            self.register[item] = mem_dict

        return self.register

    def address(self, program, ip):
        if ip is None:
            return 'None'

        # TODO:  form is self.register[program][index]
        return self.register[program][ip]

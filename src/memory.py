# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:46 2019

@author: Dan J Hamilton
"""

# class Memory
#     Properties
#         buffer
#         bank
#
#     Methods
#         flash
#         address


# %% Memory Class

class Memory:
    def __init__(self, program={}):
        self.bank = self.flash(program)

    def flash(self, program):
        mem_dict = {}

        if program == {}:
            return {}

        for item in program:
            code = program[item].code

            for i in range(len(code)):
                mem_dict[i] = code[i]

            self.bank[item] = mem_dict

        return self.bank

    def address(self, program_name, ip):
        if ip is None:
            return 'None'

        return self.bank[program_name][ip]

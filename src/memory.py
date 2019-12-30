# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:46 2019

@author: Dan J Hamilton
"""

# class Memory
#     Properties
#         buffer
#         register

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

        code = program.code

        for i in range(len(code)):
            mem_dict[i] = code[i]

        return mem_dict

    def address(self, i):
        if i is None:
            return 'None'

        return self.register[i]




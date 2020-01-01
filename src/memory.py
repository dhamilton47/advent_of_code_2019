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
    """
    Memory is equivalent to RAM.  It stores a copy of each loaded Program.
    These copies are then used to create the Instructions for a Program.

    A bank is the memory associated with a specific Program's code.
    """

    def __init__(self, program={}):
        self.bank = self.flash(program)

    def flash(self, program):
        """
        A Program's coded is added to Memory when the Porgram is loaded.
        """
        mem_dict = {}

        if program == {}:
            return {}

        for item in program:
            code = program[item].code

            for address in range(len(code)):
                mem_dict[address] = code[address]

            self.bank[item] = mem_dict

        return self.bank

    def value(self, program_name, address):
        """ Return the value stored at a particular memory address. """
        if address is None:
            return 'None'

        return self.bank[program_name][address]

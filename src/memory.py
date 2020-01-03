# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:46 2019

@author: Dan J Hamilton
"""

# class Memory
#     Properties
#         bank
#         base_offset
#
#     Methods
#         flash
#         address
#         extend_memory


# %% Memory Class

class Memory:
    """
    Memory is equivalent to RAM.  It stores a copy of each loaded Program.
    These copies are then used to create the Instructions for a Program.

    A bank is the memory associated with a specific Program's code.
    """

    def __init__(self, program={}):
        self.bank = self.flash(program)
        self.base_offset = 0

    def flash(self, program):
        """
        A Program's coded is added to Memory when the Porgram is loaded.
        """

        mem_dict = {}

        if program == {}:
            return {}

        for item in program:
            code = program[item].code

            for address, value in enumerate(code):
                mem_dict[address] = value

            self.bank[item] = mem_dict

        return self.bank

    def value(self, program_name, address):
        """ Return the value stored at a particular memory address. """

        if address is None:
            return 'None'

        self.bank[program_name] = \
            self.extend_memory(self.bank[program_name], address)
        # print(f"program name = {program_name}, address = {address}, "
        #       f"length bank = {len(self.bank[program_name])}")
        return self.bank[program_name][address]

    def extend_memory(self, bank, address):
        """ Extend the memory bank if it is too short for a desired address """
        if address >= len(bank):
            # print(len(bank))
            for index in range(len(bank), address + 1):
                bank[index] = 0
            # bank.extend(0 * (address - len(bank)))

        return bank

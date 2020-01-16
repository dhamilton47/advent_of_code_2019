# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:46 2019

@author: Dan J Hamilton
"""


# %% Memory Class

class Memory:
    """
    Memory is equivalent to RAM.  Initially, it stores a copy of the Program.
    The memory is then used to create the Instruction(s) for execution
    and modified as per the execution of those instructions.

    A bank is the memory allocated to a Program.

    class Memory
        Properties
            bank
            base_offset

        Methods
            extend_memory
            flash
            value
    """

    def __init__(self, program={}):
        self.bank = self.flash(program)
        self.base_offset = 0

    def extend_memory(self, bank, address):
        """ Extend the memory bank if it is too short for a desired address """
        if address >= len(bank):
            for index in range(len(bank), address + 1):
                bank[index] = 0

        return bank

    def flash(self, program):
        """
        A Program's code is added to its bank when the Program is loaded.
        """

        mem_dict = {}

        if program == {}:
            return {}

        code = program.code

        for address, value in enumerate(code):
            mem_dict[address] = value

        self.bank = mem_dict

        return self.bank

    def value(self, address):
        """ Return the value stored at a particular memory address. """

        if address is None:
            return 'None'

        self.bank = self.extend_memory(self.bank, address)

        return self.bank[address]

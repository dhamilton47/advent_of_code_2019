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
            flash
            value
    """

    def __init__(self, program={}):
        self.bank = self.flash(program)
        self.base_offset = 0

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

        return mem_dict

    def value(self, address):
        """ Return the value stored at a particular memory address. """

        if address is None:
            return 'None'

        if address not in self.bank:
            self.bank[address] = 0

        return self.bank[address]

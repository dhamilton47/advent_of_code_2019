# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 23:59:09 2019

@author: Dan J Hamilton
"""


import aoc


# %% Program Class

class Program:
    """
    This class retrieves a program's information from the available
    programs dictionary.

    class Program
        Properties
            code
            description
            name

        Methods
            read_binary
    """

    def __init__(self, program):
        self.code = self.read_binary(program['binary'])
        self.description = program['description']
        self.name = program['name']

    def read_binary(self, program_binary):
        """
        Read and parse the text file associated with the named program
        """

        return aoc.read_intcode_program(program_binary)

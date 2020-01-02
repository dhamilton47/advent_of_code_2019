# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 23:59:09 2019

@author: Dan J Hamilton
"""


# class Program
#     Properties
#         binary
#         code
#         copies
#         description
#         io_in
#         io_out
#         io_in_count
#         io_out_sount
#         messages_in
#         messages_out
#         name
#         process_order
#
#     Methods
#         read_binary
#         verify


# %% Program Class

class Program:
    """
    This class retrieves a program's information from the available
    programs dictionary.
    """

    def __init__(self, program):
        self.binary = program['binary']
        self.code = self.read_binary()
        self.description = program['description']
        self.io_in = (self.verify(program, 'io_in'),
                      self.verify(program, 'messages_in'))
        self.io_out = (self.verify(program, 'io_out'),
                       self.verify(program, 'messages_out'))
        self.io_in_count = 0
        self.io_out_count = 0
        self.name = program['name']
        self.process_order = self.verify(program, 'process_order')

    def read_binary(self, program_binary=None):
        """
        Read and parse the text file associated with the named program
        """

        if program_binary is not None:
            self.binary = program_binary

        file = open(self.binary, "r")
        if file.mode == 'r':
            contents = file.read()
            file.close()

        code = []
        raw_program = list(contents.split(","))
        raw_program_length = len(raw_program)
        for i in range(raw_program_length):
            code.append(int(raw_program[i]))

        return code

    def verify(self, program, attribute):
        """
        Verify that the property is part of the program info, return
        None if not.
        """

        if attribute in program.keys():
            return program[attribute]

        return None

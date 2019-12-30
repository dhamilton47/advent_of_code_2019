# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 23:59:09 2019

@author: Dan J Hamilton
"""


# %% Program Class

class Program:
    """
    This class retrieves a program's information from the available
    programs dictionary.
    """

    def __init__(self, program):
        # self.program = program
        self.name = program['name']
        self.description = program['description']
        self.binary = program['binary']
        self.code = self.read_binary()
        self.copies = program['copies']
        self.input_sources = self.input_source(program)
        self.messages_in = self.message_in(program)
        self.messages_out = self.message_out(program)
        self.messages_in_calls = 0
        self.messages_out_calls = 0
        # self.input_sources = ''
        # self.messages_in = []
        # self.messages_out = []

    def read_binary(self, program_binary=None):
        """
        Read and parse the text file associated with the named program
        """

        if program_binary is not None:
            self.binary = program_binary

        f = open(self.binary, "r")
        if f.mode == 'r':
            contents = f.read()
            f.close()

        code = []
        raw_program = list(contents.split(","))
        raw_program_length = len(raw_program)
        for i in range(raw_program_length):
            code.append(int(raw_program[i]))

        return code

    def input_source(self, program):
        if 'input_source' in program.keys():
            return program['input_source']

        return None

    def message_in(self, program):
        if 'message_in' in program.keys():
            return program['message_in']

        return None

    def message_out(self, program):
        if 'message_out' in program.keys():
            return program['message_out']

        return None

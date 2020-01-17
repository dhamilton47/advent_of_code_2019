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

        with open(program_binary, 'r', encoding='utf-8') as file:
            contents = file.read().split(',')

        contents = [int(_) for i, _ in enumerate(contents)]

        return contents

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  22 15:49:41 2019

@author: Dan J Hamilton
"""


# import sys
# import os

# import aoc
from program import Program
from cpu import CPU
from io_aoc import IO
from memory import Memory
from instruction import Instruction
from stack import Stack


# %% Define the IntCode class

class Computer:
    """
    class Computer(library = dictionary of information regarding programs)
        Sub Classes
            class Program - code loaded to memory for execution
            class Memory - refers to CPU cache/memory (RAM), not ROM
            class Instruction - retrieved by the computer from each program and
                    placed on the stack for execution
            class IO - get data from user (keyboard) or from registers.
                    Place on stack.  Return data to user or place into
                    a register.
            class CPU - executes opreations from the stack
            class OS
                class Instruction
            class Stack
            class Register - ?

        Properties
            name
            cpu
            io
            memory
            programs_available_dictionary
            program_loaded
            ip (instruction pointer)
            programs_loaded
            ips (instruction pointer)

        Methods
            boot
            instruction_next
            program_load
            program_menu
            programs_available

            input
            output
    # """

    def __init__(self, library):
        self.name = 'HAL'
        self.cpu = None
        self.io = None
        self.memory = None
        self.programs_available_dictionary = library
        # self.program_loaded = None
        # self.ip = None
        self.programs_loaded = {}
        self.ips = {}
        self.ips_last = {}
        self.instructions = {}
        self.registers = {}
        self.stack = {}
        self.instruction_bits = {}
        self.idle_bits = {}

    def boot(self):
        """
        Initialize sub-classes the computer utilizes.
        """

        self.cpu = CPU()
        self.io = IO()
        self.memory = Memory()
        self.stack = Stack()

        # return self.cpu, self.io, self.memory, self.stack

    def instruction_next(self):
        if self.programs_loaded == {}:
            return {}

        for item in self.ips.items():
            if item[1] == self.ips_last[item[0]]:
                self.instructions[item[0]] = \
                    Instruction(item[0],
                                self.memory,
                                self.ips[item[0]])

    def program_load(self):
        """
        Control the flow to:
            Ask which program to run on this computer
            Load the program
        """

        program_keys = self.programs_available()
        program_index = self.program_menu(program_keys)
        program_to_load = \
            self.programs_available_dictionary[program_keys[program_index]]

        for item in program_to_load['copies']:
            program_loaded = Program(program_to_load)

            self.programs_loaded[item] = program_loaded
            self.ips[item] = 0
            self.ips_last[item] = 0

        # return self.programs_loaded

    def program_menu(self, program_list):
        """
        Create the text to display for the user to make a choice
        of which program to run.  Ask for that choice and return it.

        program_list = the dictionary keys from the
                       programs_available_dictionary
        """

        print_string = "\n\nHello, Dan.\n\n"
        print_string += ("My name is " + self.name
                         + ".\n\nI am capable of doing the following:")

        for i in range(len(program_list)):
            if program_list[i] == "None":
                continue

            print_string += "\n  " + f"{i:2d}" + ". " + program_list[i]

        print(f"{print_string}")

        return int(input('What shall we do today?\n(Please enter a number): '))

    def programs_available(self):
        """ Return the programs_available_dictionary's keys """

        return list(self.programs_available_dictionary.keys())

    def flash_memory(self):
        self.memory.bank = self.memory.flash(self.programs_loaded)

    # def get_input():
    #     pass

    # def print_output():
    #     pass

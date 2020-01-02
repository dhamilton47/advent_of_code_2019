# -*- coding: utf-8 -*-
"""
Created on Sun Dec  22 15:49:41 2019

@author: Dan J Hamilton
"""


# import sys
# import os

# import aoc
from cpu import CPU
from io_aoc import IO
from instruction import Instruction
from memory import Memory
from program import Program
from register import Register


# %% Define the IntCode class

class Computer:
    """
    class Computer(library = dictionary of information regarding programs)
        Inner Classes
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
            programs_loaded_keys
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

        self.buffers = {}
        self.cpu = None
        self.instructions = {}
        self.io = None
        self.ips = {}
        self.ips_last = {}
        self.memory = None
        self.process_active = None
        self.process_order = None
        self.programs_available_dictionary = library
        self.programs_available_keys = list(library.keys())
        self.programs_loaded = {}
        self.programs_loaded_keys = []
        self.stack = []

    def boot(self):
        """
        Initialize sub-classes the computer utilizes.
        """

        self.cpu = CPU()
        self.io = IO()
        self.memory = Memory()

    def instruction_next(self):
        """
        Grab the next Instruction to execute
        """
        program_name = self.process_active

        if program_name == []:
            return {}

        instruction = Instruction(self)
        # print(f"Instruction = {instruction}")
        return instruction.instruction

    def process_run(self):
        """
        the instance of a computer program that is being executed
        """
        while self.stack != []:
            self.process_active = self.stack.pop(0)
            if self.buffers[self.process_active].register[0]:

                # Execute program
                opcode = 0
                # print(f"\nRunning process {self.process_active}")
                while opcode != 99:
                    instruction = self.instruction_next()
                    # print(f"\nInstruction (in Computer Module): {instruction}")
                    instruction = self.cpu.instruction_execute(self, instruction)
                    self.ips_last[self.process_active] = \
                        self.ips[self.process_active]
                    self.ips[self.process_active] += instruction['length']
                    opcode = instruction['opcode']

            if not self.buffers[self.process_active].register[0]:
                value = self.buffers[self.process_active].register[3]
                # print(f"Buffer [{self.process_active}] = "
                #       f"{list(self.buffers[self.process_active].register.values())}")
                # self.process_active = self.stack.pop(0)
                if self.stack != []:
                    self.buffers[self.stack[0]].register[0] = True
                    self.buffers[self.stack[0]].register[2] = value
        if self.process_active == 'ampE':
            print(f"Max thruster signal = "
                  f"{self.buffers[self.process_active].register[3]}")

    def process_scheduler(self):
        """
        the activity of the process manager that handles the removal
        of the running process from the CPU and the selection of
        another process on the basis of a particular strategy
        """
        progs = self.programs_loaded
        # print(progs)
        num = self.programs_loaded_keys[0]
        # print(num)
        if len(progs) == 0:
            return {}

        if len(progs) == 1:
            self.process_order = 'sequential'
            self.stack.append(num)
        else:
            # print(progs[num].process_order)
            if progs[num].process_order == 'sequential':
                self.process_order = 'sequential'
                for item in self.programs_loaded_keys:
                    self.stack.append(item)
            elif progs[num].process_order == 'parallel':
                self.process_order = 'parallel'
            else:
                raise ValueError('No processing order specified.')

    def program_load(self):
        """
        Control the flow to:
            Ask which program to run on this computer
            Load the program
        """

        program_keys = self.programs_available_keys
        # program_keys = self.programs_available()
        program_index = self.program_menu(program_keys)
        program_to_load = \
            self.programs_available_dictionary[program_keys[program_index]]

        # print(program_to_load)
        for item in program_to_load['copies']:
            program_loaded = Program(program_to_load)

            self.buffers[item] = Register()

            self.programs_loaded[item] = program_loaded
            self.programs_loaded_keys.append(item)
            self.ips[item] = 0
            self.ips_last[item] = 0

    def program_reload(self, program_to_load):
        """
        When running multiple times, parts of the Program load process
        need to be re-initialized.
        """

        for item in self.programs_loaded_keys:
            program_loaded = Program(program_to_load)
            self.buffers[item] = Register()

            self.programs_loaded[item] = program_loaded
            # self.programs_loaded_keys.append(item)
            self.ips[item] = 0
            self.ips_last[item] = 0

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

    # def programs_available(self):
    #     """ Return the programs_available_dictionary's keys """

    #     return list(self.programs_available_dictionary.keys())

    def flash_memory(self):
        """ Load the Program(s) code into a Memory bank for execution """
        self.memory.bank = self.memory.flash(self.programs_loaded)

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
            class Stack - ?
            class Register - ?

        Properties
            buffers
            computer_name
            cpu
            io
            ips (instruction pointer)
            # ips_last (instruction pointer)
            library
            memory
            process_active
            process_order
            program_copies_loaded
            programs_loaded
            stack

        Methods
            boot
            flash_memory
            instruction_next
            process_run
            process_scheduler
            program_load
            program_menu
            program_reload
            # programs_available
    # """

    def __init__(self, library):
        self.computer_name = 'HAL'

        self.buffers = {}
        self.cpu = None
        self.io = None
        self.ips = {}
        self.library = library
        self.memory = None
        self.process_active = None
        self.process_order = None
        self.program_name = {}
        self.programs_loaded = {}
        self.program_copies_loaded = []
        self.stack = []

    def boot(self):
        """
        Initialize sub-classes the computer utilizes.
        """

        self.cpu = CPU()
        self.io = IO()
        self.memory = Memory()

    def flash_memory(self):
        """ Load the Program(s) code into a Memory bank for execution """
        self.memory.bank = self.memory.flash(self.programs_loaded)

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

        thruster_max = 0

        while self.stack != []:
            self.process_active = self.stack.pop(0)
            # print(f"Stack = {self.stack}")
            # print(f"Program copies loaded = {self.program_copies_loaded}")
            if self.buffers[self.process_active].register[0]:

                # Execute program
                opcode = 0
                print(f"\nRunning process {self.process_active}")
                while opcode != 99:
                    instruction = self.instruction_next()
                    # print(f"\nInstruction (in Computer Module): "
                    #       f"{instruction}")
                    instruction = \
                        self.cpu.instruction_execute(self, instruction)
                    self.ips[self.process_active] += instruction['length']
                    opcode = instruction['opcode']

            if not self.buffers[self.process_active].register[0]:
                value = self.buffers[self.process_active].register[3]
                # print(f"Buffer [{self.process_active}] = "
                #       f"{list(self.buffers[self.process_active].register.values())}")
                if self.stack != []:
                    self.buffers[self.stack[0]].register[0] = True
                    self.buffers[self.stack[0]].register[2] = value
        # if self.program_name == "Amp":
        #     thruster_max = thruster_max if thruster_max > \
        #         self.buffers[self.process_active].register[3] \
        #         else self.buffers[self.process_active].register[3]

        # if self.program_name == 'Amp':
        #     print(f"Max thruster signal = "
        #           # f"{thruster_max}")
        #           f"{self.buffers[self.process_active].register[3]}")

    def process_scheduler(self):
        """
        the activity of the process manager that handles the removal
        of the running process from the CPU and the selection of
        another process on the basis of a particular strategy
        """
        if len(self.program_copies_loaded) == 0:
            self.stack = {}

        self.stack = self.program_copies_loaded.copy()

    def program_load(self):
        """
        Control the flow to:
            Ask which program to run on this computer
            Load the program
        """

        program_keys = list(self.library.keys())
        program_index = self.program_menu(program_keys)
        program_to_load = self.library[program_keys[program_index]]

        self.program_name = program_to_load['name']

        # print(program_to_load)
        for item in program_to_load['copies']:
            program_loaded = Program(program_to_load)

            self.buffers[item] = Register()

            self.programs_loaded[item] = program_loaded
            self.program_copies_loaded.append(item)
            self.ips[item] = 0

    def program_menu(self, program_list):
        """
        Create the text to display for the user to make a choice
        of which program to run.  Ask for that choice and return it.

        program_list = the dictionary keys from the
                       programs_available_dictionary
        """

        print_string = "\n\nHello, Dan.\n\n"
        print_string += ("My name is " + self.computer_name
                         + ".\n\nI am capable of doing the following:")

        for index, value in enumerate(program_list):
            if value == "None":
                continue

            print_string += "\n  " + f"{index:2d}" + ". " + value

        print(f"{print_string}")

        return int(input('What shall we do today?\n(Please enter a number): '))

    # def programs_available(self):
    #     """ Return the programs_available_dictionary's keys """

    #     return list(self.programs_available_dictionary.keys())

    def program_reload(self, program_to_load):
        """
        When running multiple times, parts of the Program load process
        need to be re-initialized.
        """
        # print(f"Program copies loaded = {self.program_copies_loaded}")
        self.stack = self.program_copies_loaded.copy()

        for item in self.program_copies_loaded:
            program_loaded = Program(program_to_load)

            self.buffers[item] = Register()
            self.programs_loaded[item] = program_loaded
            self.ips[item] = 0

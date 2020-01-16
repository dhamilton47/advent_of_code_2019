# -*- coding: utf-8 -*-
"""
Created on Sun Dec  22 15:49:41 2019

@author: Dan J Hamilton
"""


from cpu import CPU
from io_aoc import IO
from instruction import Instruction
from memory import Memory
from program import Program


# %% Define the IntCode class

class Computer:
    """
    class Computer(library = dictionary of information regarding programs)
        Inner Classes
            class Program - code loaded to memory for execution
            class Memory - refers to CPU cache/memory (RAM), not ROM
            class Instruction - calculated by the computer.
            class IO - get data from user (keyboard) or from registers.
                    Return data to user or place into a register.
            class CPU - executes Instruction(s)
            class OS - ?

        Properties
            computer_name
            cpu
            halt_condition
            io
            ip (instruction pointer)
            library
            memory
            program_name
            program_loaded
            program_to_load

        Methods
            boot
            flash_memory
            instruction_next
            process_run
            program_load
    """

    def __init__(self, library, program_to_load):
        self.computer_name = 'HAL'

        self.cpu = None
        self.halt_condition = False
        self.io = None
        self.ip = 0
        self.library = library
        self.memory = None
        self.program_name = None
        self.program_loaded = None
        self.program_to_load = program_to_load

    def boot(self):
        """
        Initialize sub-classes the computer utilizes.
        """

        self.cpu = CPU()
        self.io = IO()
        self.memory = Memory()

    def flash_memory(self):
        """ Load the Program code into Memory bank for execution """

        self.memory.bank = self.memory.flash(self.program_loaded)

    def instruction_next(self):
        """
        Grab the next Instruction to execute
        """

        instruction = Instruction(self)

        return instruction.instruction

    def process_run(self):
        """
        Execute the Program
        """

        opcode = 0
        # print(f"\nRunning process {self.process_active}")

        while opcode != 99:
            instruction = self.instruction_next()
            # print(f"\nInstruction (in Computer Module): "
            #       f"{instruction}")
            instruction = \
                self.cpu.instruction_execute(self, instruction)
            self.ip += instruction['length']
            # print(self.ip)
            opcode = instruction['opcode']

            # print(f"Halt: {self.halt_condition}, "
            #       f"OpCode = {opcode}, "
            #       f"Output Value = {self.output_value}")

            if self.halt_condition and opcode == 4:
                break

        return opcode

    def program_load(self):
        """ Load the Program """

        program_to_load = self.library[self.program_to_load]
        self.program_name = program_to_load['name']
        self.program_loaded = Program(program_to_load)

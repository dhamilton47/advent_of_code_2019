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
            class CPU - executes Instruction(s)
            class IO - get data from user (keyboard) or from registers.
                    Return data to user or place into a register.
            class Memory - refers to CPU cache/memory (RAM), not ROM
            class Program - code loaded to memory for execution
            class Instruction - calculated by the computer.

        Properties
            computer_name

            cpu
            io
            memory
            program

            halt_condition
            ip (instruction pointer)

        Methods
            flash_memory
            instruction_next
            process_run
    """

    def __init__(self, library, program_name):
        self.computer_name = 'HAL'

        self.cpu = CPU()
        self.io = IO()
        self.memory = Memory()
        self.program = Program(library[program_name])

        self.halt_condition = False
        self.ip = 0

    def flash_memory(self):
        """ Load the Program code into Memory bank for execution """

        self.memory.bank = self.memory.flash(self.program)

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
            self.ip = instruction['next_ip']

            opcode = instruction['opcode']

            # print(f"Halt: {self.halt_condition}, "
            #       f"OpCode = {opcode}, "
            #       f"Output Value = {self.output_value}")

            if self.halt_condition and opcode == 4:
                break

        return opcode

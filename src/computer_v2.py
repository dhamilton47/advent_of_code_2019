# -*- coding: utf-8 -*-
"""
Created on Sun Dec  22 15:49:41 2019

@author: Dan J Hamilton
"""


from cpu1 import CPU
from io_aoc1 import IO
from instruction1 import Instruction
from memory1 import Memory
from program1 import Program
from register1 import Register


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
            class Register - ?

        Properties
            buffer
            computer_name
            cpu
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
            # program_reload
    """

    def __init__(self, library, program_to_load):
        self.computer_name = 'HAL'

        self.buffer = None
        self.cpu = None
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

        # thruster_max = 0

        opcode = 0
        # print(f"\nRunning process {self.process_active}")

        while opcode != 99:
            instruction = self.instruction_next()
            # print(f"\nInstruction (in Computer Module): "
            #       f"{instruction}")
            instruction = \
                self.cpu.instruction_execute(self, instruction)
            self.ip += instruction['length']
            opcode = instruction['opcode']

    def program_load(self):
        """ Load the Program """

        program_to_load = self.library[self.program_to_load]

        self.program_name = program_to_load['name']

        program_loaded = Program(program_to_load)

        self.buffer = Register()

        self.program_loaded = program_loaded

    # def program_reload(self, program_to_load):
    #     """
    #     When running multiple times, parts of the Program load process
    #     need to be re-initialized.
    #     """
    #     # print(f"Program copies loaded = {self.program_copies_loaded}")
    #     self.stack = self.program_copies_loaded.copy()

    #     for item in self.program_copies_loaded:
    #         program_loaded = Program(program_to_load)

    #         self.buffers[item] = Register()
    #         self.programs_loaded[item] = program_loaded
    #         self.ips[item] = 0

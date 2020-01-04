# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from computer import Computer


import aoc
import phases

# Day 7, Part 1 needs:
#     Multiple programs running on the computer
#     Buffer(s) or stack to add instruction command control
#     Inputs coming from the stack
#     Outputs placed on the stack
#     Inputs:
#         Phase setting
#         Signal


# %%
def intcode(library, program, input1, input2):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.boot()
    computer.program_load()
    computer.flash_memory()
    computer.emulated_input = [input1, input2]
    computer.process_run()

    return computer


def thruster(program, library=aoc.PROGRAMS_AVAILABLE_DICTIONARY):
    """ main() program """
    computer = Computer(library, program)
    computer.boot()

    # Select a program to run & flash memory
    computer.program_load()

    phase_input = phases.phase_generator()
    print(f"Number of phase combinations to run = {len(phase_input)}")

    thruster_max = 0

    for index in range(len(phase_input)):
        # index = 29
        computer.program_reload(computer.library['Amp'])
        computer.flash_memory()

        # if 'ampA' in computer.programs_loaded_keys:
        phases.phase_load(computer, phase_input, index)
        print(phase_input[index])
        # if 'ampA' in computer.programs_loaded_keys:
        computer.buffers['ampA'].register[0] = True
        computer.buffers['ampA'].register[2] = 0

        computer.process_scheduler()
        computer.process_run()
        thruster_max = thruster_max if thruster_max > \
            computer.buffers[computer.process_active].register[3] \
            else computer.buffers[computer.process_active].register[3]
        print(computer.buffers[computer.process_active].register[3])
        print('we got here')
    print(f"Maximum thruster signal = {thruster_max}")


def process_scheduler(library, program):
    """
    the activity of the process manager that handles the removal
    of the running process from the CPU and the selection of
    another process on the basis of a particular strategy
    """

    return library[program]['copies']


# %% Development Environment

# phase_input = phases.phase_generator()
phase_input = phases.phase_generator1()
print(f"Number of phase combinations to run = {len(phase_input)}")

program_stack = process_scheduler(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
thruster_max = 0

# index = 119
# index = 112
# value = phase_input[index]

for index, value in enumerate(phase_input):
    # print(index, value)

    phase_register = value
    print(phase_input[index])

    signal_register = [0, None, None, None, None]
    # print(signal_register)
    # signal_register[0] = 0

    ampA = Computer(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
    ampA.boot()
    ampA.program_load()
    ampA.flash_memory()
    ampA.halt_condition = True

    ampB = Computer(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
    ampB.boot()
    ampB.program_load()
    ampB.flash_memory()
    ampB.halt_condition = True

    ampC = Computer(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
    ampC.boot()
    ampC.program_load()
    ampC.flash_memory()
    ampC.halt_condition = True

    ampD = Computer(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
    ampD.boot()
    ampD.program_load()
    ampD.flash_memory()
    ampD.halt_condition = True

    ampE = Computer(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
    ampE.boot()
    ampE.program_load()
    ampE.flash_memory()
    ampE.halt_condition = True

    for i in range(11):
    # for i in range(1):
        # print(f"\nBefore Amp A, Signal Register = {signal_register}")
        ampA.emulated_input = [phase_register[0], signal_register[0]]
        # print(ampA.emulated_input)
        if signal_register[0] is not None:
            ampA.process_run()
            signal_register[0] = None

        signal_register[1] = ampA.output_value
        # print(f"AFter Amp A, Signal Register = {signal_register}")

        # print(f"\nBefore Amp B, Signal Register = {signal_register}")
        ampB.emulated_input = [phase_register[1], signal_register[1]]
        if signal_register[1] is not None:
            ampB.process_run()
            signal_register[1] = None

        signal_register[2] = ampB.output_value
        # print(f"AFter Amp B, Signal Register = {signal_register}")

        # print(f"\nBefore Amp C, Signal Register = {signal_register}")
        ampC.emulated_input = [phase_register[2], signal_register[2]]
        if signal_register[2] is not None:
            ampC.process_run()
            signal_register[2] = None

        signal_register[3] = ampC.output_value
        # print(f"AFter Amp C, Signal Register = {signal_register}")

        # print(f"\nBefore Amp D, Signal Register = {signal_register}")
        ampD.emulated_input = [phase_register[3], signal_register[3]]
        if signal_register[3] is not None:
            ampD.process_run()
            signal_register[3] = None

        signal_register[4] = ampD.output_value
        # print(f"AFter Amp D, Signal Register = {signal_register}")

        # print(f"\nBefore Amp E, Signal Register = {signal_register}")
        ampE.emulated_input = [phase_register[4], signal_register[4]]
        if signal_register[4] is not None:
            ampE.process_run()
            signal_register[4] = None

        signal_register[0] = ampE.output_value
        # print(f"AFter Amp E, Signal Register = {signal_register}")


    thruster_test = ampE.output_value

    thruster_max = thruster_max if thruster_max > \
        thruster_test \
        else thruster_test

print(f"Maximum thruster signal = {thruster_max}")


# test.instruction_next()

# Determine next instruction to process and execute it.


# %% Production Environment (LOL)

# if __name__ == "__main__":
    # thruster('Amp', aoc.PROGRAMS_AVAILABLE_DICTIONARY)

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""

from computer import Computer

import aoc
import phases


"""
Day 7, Part 1 needs:
    Multiple programs running on the computer
    Buffer(s) or stack to add instruction command control
    Inputs coming from the stack
    Outputs placed on the stack
    Inputs:
        Phase setting
        Signal
"""


# %%
def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.boot()
    computer.program_load()
    computer.flash_memory()
    computer.halt_condition = True

    return computer


def program_run_halt(computer, halt_check):
    if halt_check is not None:
        computer.process_run()

    return None


def thruster(program,
             part,
             library=aoc.PROGRAMS_AVAILABLE_DICTIONARY,
             print_flag=False):
    """ main() program """

    if part == 1:
        phase_input = phases.phase_generator()
    else:
        phase_input = phases.phase_generator1()

    if print_flag:
        print(f"Number of phase combinations to run = {len(phase_input)}")

    thruster_max = 0

    for index, value in enumerate(phase_input):
        # print(index, value)

        phase_register = value
        # print(phase_input[index])

        signal_register = [0, None, None, None, None]
        # print(signal_register)

        ampA = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
        ampB = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
        ampC = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
        ampD = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
        ampE = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')

        if part == 1:
            runs = 1
        else:
            runs = 11

        for i in range(runs):
            if print_flag:
                print(f"\nBefore Amp A, Signal Register = {signal_register}")
            ampA.emulated_input = [phase_register[0], signal_register[0]]
            signal_register[0] = program_run_halt(ampA, signal_register[0])

            signal_register[1] = ampA.output_value
            if print_flag:
                print(f"AFter Amp A, Signal Register = {signal_register}")

            if print_flag:
                print(f"\nBefore Amp B, Signal Register = {signal_register}")
            ampB.emulated_input = [phase_register[1], signal_register[1]]
            signal_register[1] = program_run_halt(ampB, signal_register[1])

            signal_register[2] = ampB.output_value
            if print_flag:
                print(f"AFter Amp B, Signal Register = {signal_register}")

            if print_flag:
                print(f"\nBefore Amp C, Signal Register = {signal_register}")
            ampC.emulated_input = [phase_register[2], signal_register[2]]
            signal_register[2] = program_run_halt(ampC, signal_register[2])

            signal_register[3] = ampC.output_value
            if print_flag:
                print(f"AFter Amp C, Signal Register = {signal_register}")

            if print_flag:
                print(f"\nBefore Amp D, Signal Register = {signal_register}")
            ampD.emulated_input = [phase_register[3], signal_register[3]]
            signal_register[3] = program_run_halt(ampD, signal_register[3])

            signal_register[4] = ampD.output_value
            if print_flag:
                print(f"AFter Amp D, Signal Register = {signal_register}")

            if print_flag:
                print(f"\nBefore Amp E, Signal Register = {signal_register}")
            ampE.emulated_input = [phase_register[4], signal_register[4]]
            signal_register[4] = program_run_halt(ampE, signal_register[4])

            signal_register[0] = ampE.output_value
            if print_flag:
                print(f"AFter Amp E, Signal Register = {signal_register}")

        thruster_test = ampE.output_value

        thruster_max = thruster_max if thruster_max > \
            thruster_test \
            else thruster_test

    print(f"Maximum thruster signal = {thruster_max}")


# def process_scheduler(library, program):
#     """
#     the activity of the process manager that handles the removal
#     of the running process from the CPU and the selection of
#     another process on the basis of a particular strategy
#     """

#     return library[program]['copies']


# %% Development Environment

# phase_input = phases.phase_generator()
# # phase_input = phases.phase_generator1()
# print(f"Number of phase combinations to run = {len(phase_input)}")

# # program_stack = process_scheduler(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
# thruster_max = 0

# # index = 119
# # index = 112
# # value = phase_input[index]

# for index, value in enumerate(phase_input):
#     # print(index, value)

#     phase_register = value
#     # print(phase_input[index])

#     signal_register = [0, None, None, None, None]
#     # print(signal_register)

#     ampA = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
#     ampB = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
#     ampC = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
#     ampD = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')
#     ampE = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Amp')

#     # for i in range(11):
#     for i in range(1):
#         # print(f"\nBefore Amp A, Signal Register = {signal_register}")
#         ampA.emulated_input = [phase_register[0], signal_register[0]]
#         signal_register[0] = program_run_halt(ampA, signal_register[0])

#         signal_register[1] = ampA.output_value
#         # print(f"AFter Amp A, Signal Register = {signal_register}")

#         # print(f"\nBefore Amp B, Signal Register = {signal_register}")
#         ampB.emulated_input = [phase_register[1], signal_register[1]]
#         signal_register[1] = program_run_halt(ampB, signal_register[1])

#         signal_register[2] = ampB.output_value
#         # print(f"AFter Amp B, Signal Register = {signal_register}")

#         # print(f"\nBefore Amp C, Signal Register = {signal_register}")
#         ampC.emulated_input = [phase_register[2], signal_register[2]]
#         signal_register[2] = program_run_halt(ampC, signal_register[2])

#         signal_register[3] = ampC.output_value
#         # print(f"AFter Amp C, Signal Register = {signal_register}")

#         # print(f"\nBefore Amp D, Signal Register = {signal_register}")
#         ampD.emulated_input = [phase_register[3], signal_register[3]]
#         signal_register[3] = program_run_halt(ampD, signal_register[3])

#         signal_register[4] = ampD.output_value
#         # print(f"AFter Amp D, Signal Register = {signal_register}")

#         # print(f"\nBefore Amp E, Signal Register = {signal_register}")
#         ampE.emulated_input = [phase_register[4], signal_register[4]]
#         signal_register[4] = program_run_halt(ampE, signal_register[4])

#         signal_register[0] = ampE.output_value
#         # print(f"AFter Amp E, Signal Register = {signal_register}")

#     thruster_test = ampE.output_value

#     thruster_max = thruster_max if thruster_max > \
#         thruster_test \
#         else thruster_test

# print(f"Maximum thruster signal = {thruster_max}")


# %% Production Environment (LOL)

if __name__ == "__main__":
    thruster(program='Amp',
             part=1,
             library=aoc.PROGRAMS_AVAILABLE_DICTIONARY)

    # thruster(program='Amp',
    #          part=2,
    #          library=aoc.PROGRAMS_AVAILABLE_DICTIONARY)

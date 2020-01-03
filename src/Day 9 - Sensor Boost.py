# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 00:11:17 2020

@author: Dan J Hamilton
"""

from computer_v1 import Computer

import aoc
import phases


# %%

def test(library=aoc.PROGRAMS_AVAILABLE_DICTIONARY):
    """ main() program """
    computer = Computer(library)
    computer.boot()

    computer.program_load()

    if computer.program_name != 'Amp':
        computer.buffers[computer.program_name].register[0] = True
        computer.flash_memory()

        computer.process_scheduler()
        computer.process_run()

    if computer.program_name == 'Amp':
        phase_input = phases.phase_generator()
        print(f"Number of phase combinations to run = {len(phase_input)}")

        thruster_max = 0

        for index in range(len(phase_input)):
            computer.program_reload(computer.library['Amp'])
            computer.flash_memory()

            phases.phase_load(computer, phase_input, index)

            computer.buffers['ampA'].register[0] = True
            computer.buffers['ampA'].register[2] = 0

            computer.process_scheduler()
            computer.process_run()
            thruster_max = thruster_max if thruster_max > \
                computer.buffers[computer.process_active].register[3] \
                else computer.buffers[computer.process_active].register[3]
        print(f"Maximum thruster signal = {thruster_max}")


# %% Production Environment (LOL)

if __name__ == "__main__":
    test()

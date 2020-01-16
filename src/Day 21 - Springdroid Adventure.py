# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 01:37:31 2020

@author: Dan J Hamilton
"""


import numpy as np

import aoc
from computer import Computer


"""
While a springdroid is certainly capable of navigating the artificial
gravity and giant holes, it has one downside: it can only remember
at most 15 springscript instructions.

Two registers are available:
    T, the temporary value register, and
    J, the jump register.

If the jump register is true at the end of the springscript program,
the springdroid will try to jump. Both of these registers start
with the value false.

Your springdroid can detect ground at four distances: one tile away (A),
two tiles away (B), three tiles away (C), and four tiles away (D).

If there is ground at the given distance, the register will be true;
if there is a hole, the register will be false.

There are only three instructions available in springscript:

- AND X Y sets Y to true if both X and Y are true; otherwise,
    it sets Y to false.
- OR X Y sets Y to true if at least one of X or Y is true; otherwise,
    it sets Y to false.
- NOT X Y sets Y to true if X is false; otherwise, it sets Y to false.

In all three instructions, the second argument (Y) needs to be a
writable register (either T or J). The first argument (X) can be
any register (including A, B, C, or D).

If the springdroid falls into space, an ASCII rendering of the last moments
of its life will be produced. In these, @ is the springdroid, # is hull,
and . is empty space.

When you have finished entering your program, provide the command WALK
followed by a newline to instruct the springdroid to begin
surveying the hull.
"""


# %%
def AND(x, y):
    return x & y


def OR(x, y):
    return x | y


def NOT(x, y):
    return not x


def ascii_interpreter(val):
    val1 = [ord(val[i]) for i in range(len(val))]
    # val1.append(10)

    return val1


def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.boot()
    computer.program_load()
    computer.flash_memory()
    computer.halt_condition = True

    return computer


# %% Development Environment

# walk = 'NOT A J\nNOT B T\nAND T J\nNOT C T\nAND T J\nAND D J\nWALK\n'
combos = [
    '0000',  # Not possible to navigate
    '0001',  # inst #1 doesn't work
    '0010',
    '0011',  # inst #1 doesn't work
    '0100',
    '0101',  # inst #1 doesn't work
    '0110',
    '0111',  # inst #1 doesn't work
    '1000',
    '1001',  # inst #1 doesn't work
    '1010',
    '1011',  # inst #1 doesn't work
    '1100',
    '1101',  # inst #1 doesn't work
    '1110',
    '1111',
    ]

reg = {
   'A': 0,
   'B': 0,
   'C': 0,
   'D': 0,
   'J': 0,
   'T': int(0),
   }


def playlist():
    reg['J'] = int(NOT(reg['D'], reg['J']))  # Looking for a 1 in 4th
    reg['T'] = int(NOT(reg['J'], reg['T']))  # Flip that answer to T
    reg['J'] = int(NOT(reg['C'], reg['J']))  # Looking for a 0 in 3rd
    reg['T'] = int(AND(reg['J'], reg['T']))  # Flipping that combo to T; Gives us 11 if ab01
    reg['J'] = int(AND(reg['C'], reg['J']))  # Looking for a 1 in 3rd
    reg['J'] = int(AND(reg['T'], reg['J']))  # Gives us jump if


for i in range(1, 16):
    reg['A'] = int(combos[i][0])
    reg['B'] = int(combos[i][1])
    reg['C'] = int(combos[i][2])
    reg['D'] = int(combos[i][3])
    playlist()
    print(reg)


answer = [
    'NOT D J\n'
    'NOT J T\n'
    'NOT C J\n'
    'AND T J\n'
    'WALK\n'
    ]

# any_combo_fourth_is_hull = [
#     'NOT A J\n'
#     'NOT B T\n'
#     'AND T J\n'
#     'NOT C T\n'
#     'AND T J\n'
#     'OR A J\n'
#     'OR B J\n'
#     'OR C J\n'
#     'AND D J\n'
#     'WALK\n'
#     ]

# three_space_hole = [
#     'NOT A J\n'
#     'NOT B T\n'
#     'AND T J\n'
#     'NOT C T\n'
#     'AND T J\n'
#     'AND D J\n'
#     'WALK\n'
#     ]

# jump_into_any_hole = [
#     'NOT D J\n'
#     'WALK\n'
#     ]

# fourth_spot_hull = [
#     'OR A J\n'
#     'OR B J\n'
#     'OR C J\n'
#     'AND D J\n'
#     'WALK\n'
#     ]

opcode = 0

machine = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Springdroid')
machine.io.input_value = ascii_interpreter(answer[0])
string = ''
while opcode != 99:
    machine.process_run()
    if machine.io.output_value < 128:
        # print(machine.output_value)
        string += chr(machine.io.output_value)
    else:
        print(machine.io.output_value)
        break

# print(chr(machine.output_value))


# %% Production Environment (LOL)

# if __name__ == "__main__":
#     test()

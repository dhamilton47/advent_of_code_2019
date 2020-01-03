# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


import aoc


# While a springdroid is certainly capable of navigating the artificial
# gravity and giant holes, it has one downside: it can only remember
# at most 15 springscript instructions.

# Two registers are available:
    # T, the temporary value register, and
    # J, the jump register.

# If the jump register is true at the end of the springscript program,
# the springdroid will try to jump. Both of these registers start
# with the value false.

# Your springdroid can detect ground at four distances: one tile away (A),
# two tiles away (B), three tiles away (C), and four tiles away (D).

# If there is ground at the given distance, the register will be true;
# if there is a hole, the register will be false.

# There are only three instructions available in springscript:

# - AND X Y sets Y to true if both X and Y are true; otherwise,
    # it sets Y to false.
# - OR X Y sets Y to true if at least one of X or Y is true; otherwise,
    # it sets Y to false.
# - NOT X Y sets Y to true if X is false; otherwise, it sets Y to false.

# In all three instructions, the second argument (Y) needs to be a
# writable register (either T or J). The first argument (X) can be
# any register (including A, B, C, or D).

# If the springdroid falls into space, an ASCII rendering of the last moments
# of its life will be produced. In these, @ is the springdroid, # is hull,
# and . is empty space.

# When you have finished entering your program, provide the command WALK
# followed by a newline to instruct the springdroid to begin
# surveying the hull.





# %% Transform the "XXXX" from a string to a list
def transform_program(contents):
    memory = list(contents.split(","))
#    memory_length = len(memory)
#    for i in range(memory_length):
#        memory[i] = int(memory[i])

    return memory


txtfile = "../data/AoC2019_day_21_input.txt"
contents = aoc.read_program(txtfile)
transformed_contents = transform_program(contents)

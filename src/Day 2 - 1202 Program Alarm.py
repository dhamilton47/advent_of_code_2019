# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:34:08 2019

@author: Dan J Hamilton
"""

import aoc


# %%
def main(txtfile):
    for i in range(100):
        for j in range(100):
            memory = initiate_code_sequence(txtfile, i, j)
            intcode(memory)


def initiate_code_sequence(txtfile, x, y):
    memory = aoc.read_intcode_program(txtfile)
    memory[1] = x
    memory[2] = y

    return memory


def opcode1(memory, var1, var2, var3):
    memory[var3] = memory[var1] + memory[var2]

    return 4


def opcode2(memory, var1, var2, var3):
    memory[var3] = memory[var1] * memory[var2]

    return 4


def opcode99(memory):
    if memory[1] == 12 and memory[2] == 2:
        print(f"Day 2 - Part 1 - Output = {memory[0]:d}")
    if memory[0] == 19690720:
        print(f"Day 2 - Part 2 - 100 * noun + verb = "
              f"{100 * memory[1] + memory[2]:d}\n"
              f"Day 2 - Part 2 - Check = {memory[0]:d}")

    return len(memory)


def intcode(x):
    index = 0

    while index < len(x):
        opcode = x[index]
        var1 = x[index + 1]
        var2 = x[index + 2]
        var3 = x[index + 3]

        if opcode == 1:
            index += opcode1(x, var1, var2, var3)
        elif opcode == 2:
            index += opcode2(x, var1, var2, var3)
        elif opcode == 99:
            index = opcode99(x)
        else:
            print(str(100 * x[index] + x[index + 1]), 'program alarm')
            index += 4


# %%
main("../data/AoC2019_day_2_input.txt")

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:34:08 2019

@author: Dan J Hamilton
"""


# %%
def main(txtfile, instruction_length=4):
    code = read_intcode(txtfile)

    for i in range(100):
        for j in range(100):
            memory = initiate_code_sequence(code, i, j)
            IntCode(memory)


# %%
def read_intcode(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    return contents


# %%
def set_memory(x):
    memory = list(x.split(","))
    return memory


# %%
def initiate_code_sequence(code, x, y):
    memory = set_memory(code)
    memory[1] = x
    memory[2] = y
    return memory


# %%
def opcode1(memory, var1, var2, var3):
    memory[var3] = memory[var1] + memory[var2]
    return 4


# %%
def opcode2(memory, var1, var2, var3):
    memory[var3] = memory[var1] * memory[var2]
    return 4


# %%
def opcode99(memory):
    if memory[1] == 12 and memory[2] == 2:
        print('Day 2 - Part 1 - Output = {:,d}'.format(memory[0]))
    if memory[0] == 19690720:
        print('Day 2 - Part 2 - 100 * noun + verb = {}'
              .format(100 * memory[1] + memory[2]))
        print('Day 2 - Part 2 - Check = {}'.format(memory[0]))
    return len(memory)


# %%
def IntCode(x):
    index = 0

    for i in range(len(x)):
        x[i] = int(x[i])

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
main("./data/adventofcode_2019_day_2_input.txt")

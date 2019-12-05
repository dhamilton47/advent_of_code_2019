# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:34:08 2019

@author: danha
"""


import pandas as pd


def main(txtfile, instruction_length=4):
    for i in range(100):
        for j in range(100):
            contents = read_intcode(txtfile)
            memory = set_memory(contents)
            memory[1] = j
            memory[2] = i
            IntCode(memory)


def read_intcode(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()
    
    return contents


def get_address(mem, x):
    return mem[x]


def set_address(value, mem, x):
    mem[x] = value


def set_memory(x):
    memory = list(x.split(","))
    return memory


def set_instructions(x, instruction_length):
    for i in range(len(x)):
        x[i] = int(x[i])

    y = (len(x) // 4)
    z = [[0] * instruction_length for i in range(y)]

    for i in range(y):
        for j in range(instruction_length):
            z[i][j] = x[(i * 4) + j]

    return z

def IntCode(x):
    index = 0

    for i in range(len(x)):
        x[i] = int(x[i])

    noun = x[index + 1]
    verb = x[index + 2]

    while index < len(x):
        if x[index] == 1:
            x[x[index + 3]] = x[x[index + 1]] + x[x[index + 2]]
            index += 4
        elif +x[index] == 2:
            x[x[index + 3]] = x[x[index + 1]] * x[x[index + 2]]
            index += 4
        elif x[index] == 99:
            if x[0] == 19690720:
                print('100 * noun + verb =', str(100 * noun + verb))
                print(x[0])
            index = len(x)
        else:
            print('Final array =', str(x[index]) + str(x[index + 1]) +
                  str(x[index + 2]) + str(x[index + 3]), 'program alarm')
            index += 4


main("./data/adventofcode_2019_day_2_input.txt")

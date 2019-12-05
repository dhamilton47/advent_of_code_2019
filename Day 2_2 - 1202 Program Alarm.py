# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:34:08 2019

@author: danha
"""


import pandas as pd


# input = pd.read_csv("./data/adventofcode_2019_day_2_input.txt", sep=",",
#                    names=["data"], header=None, index_col=False)
# f = open("./data/adventofcode_2019_day_2_input.txt", "r")
# if f.mode == 'r':
#     contents = f.read()
#    print(contents)

# memory = list(contents.split(","))

# input_data = pd.DataFrame(memory, columns=['Column_Name'])

# input1 = pd.DataFrame([1, 0, 0, 0, 99], columns=['Column_Name'])
input2 = list([1, 0, 0, 0, 99])
input3 = list([2, 3, 0, 3, 99])
input4 = list([2, 4, 4, 5, 99, 0])
input5 = list([1, 1, 1, 4, 99, 5, 6, 0, 99])


def main(txtfile, instruction_length=4):
    
    contents = read_intcode(txtfile)
    memory = set_memory(contents)
    instructions = set_instructions(memory, instruction_length)

    for i in range(len(instructions)):
        print(instructions[i])


def read_intcode(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()

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
#            print(i, j, (i * 4) + j, x[(i * 4) + j])
            z[i][j] = x[(i * 4) + j]
#    for i in range(y):
#        print(z[i])
    return z

def execute_instructions(x, instruction_length):
    for instruction in x:
        opcode = instruction[0]
        parameters = []
        for i in range(1, instruction_length - 1):
            parameters.append(get_address(mem, instruction[i]))

        for i in parameters:
            if opcode == 1:
                x[x[index + 3]] = x[x[index + 1]] + x[x[index + 2]]

            elif opcode == 2:
                x[x[index + 3]] = x[x[index + 1]] * x[x[index + 2]]

            elif opcode == 99:

            else:
#            print('Final array =', str(x[index]) + str(x[index + 1]) +
#                  str(x[index + 2]) + str(x[index + 3]), 'program alarm')

def IntCode(x):
    index = 0
#    command = command_string[command_index - 1:4]
#    print('Original array =', x)
    for i in range(len(x)):
        x[i] = int(x[i])

#    print('length of array =', len(x))
    while index < len(x):
#        print('index = ', index)
        if x[index] == 1:
            x[x[index + 3]] = x[x[index + 1]] + x[x[index + 2]]
            index += 4
        elif +x[index] == 2:
            x[x[index + 3]] = x[x[index + 1]] * x[x[index + 2]]
            index += 4
        elif x[index] == 99:
#            print('Final array =', x)
            index = len(x)
        else:
#            print('Final array =', str(x[index]) + str(x[index + 1]) +
#                  str(x[index + 2]) + str(x[index + 3]), 'program alarm')
            index += 4


for i in range(99):
    for j in range(99):
        memory = arr
        memory[1] = str(j)
        memory[2] = str(i)
#        print(memory)
        IntCode(memory)

main("./data/adventofcode_2019_day_2_input.txt")

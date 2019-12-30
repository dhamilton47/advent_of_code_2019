# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 02:57:25 2019

@author: Dan J Hamilton
"""


import aoc


# %% Transform the "orbit" from a string to a list
def transform_program(contents):
    memory2 = []
    memory = contents.split("\n")
    for i in range(len(memory)):
        memory2.append(memory[i].split(")"))

    return memory2


# %%
def printpath(counter, child, parent_locator=[], parent=[], flag=False):
    if flag:
        print('counter = {}, {} -> {}'.format(counter, child, parent))


# %%
def find_parent(lst, counter, child, flag=False):
    parent_locator = child[0]
    for index, item in enumerate(lst):
        if child[0] == item[1]:
            parent = lst[index]
            counter += 1
            printpath(counter, child[0], parent_locator, parent[0], flag)
            return find_parent(lst, counter, parent) if parent[0] != 'COM' \
                else counter
    if child[0] != 'COM':
        parent = ['COM', parent_locator]
        printpath(counter, child[0], parent_locator, parent[0], flag)
    return counter


# %%
def find_child(lst, child):
    for index, item in enumerate(lst):
        if lst[index][1] == child:
            return lst[index],  index


# %%
def day6_part1(lst, print_path=False):
    total = 0
    for i in lst:
        printpath(counter=1, child=i[1], flag=print_path,
                  parent_locator=i[0], parent=i[0])
        a = find_parent(lst, 1, i, print_path)
        total += a

    return total


# %% Set up

txtfile = "../data/AoC2019_day_6_input.txt"
# txtfile1 = "../data/adventofcode_2019_day_6_test.txt"

contents = aoc.read_program(txtfile)
orbits = transform_program(contents)

total = day6_part1(orbits)
print('Day 6 - Part 1 - Total number of orbits: {:,d}'.format(total))

print(find_child(orbits, 'YOU'))
print(find_child(orbits, 'SAN'))
print(find_child(orbits, 'C4R'))

you = find_parent(orbits, 1, orbits[805])
print('Number of orbits from you to COM:', you)

santa = find_parent(orbits, 1, orbits[763])
print('Number of orbits from Santa to COM:', santa)

turn = find_parent(orbits, 1, orbits[518])
print('Number of orbits from intersection of paths to COM:', turn)

print('Day 6 - Part 2 - Number of orbits from you to Santa\n \
       (not including last mile ot each):',
      santa + you - 2 - 2 * turn)

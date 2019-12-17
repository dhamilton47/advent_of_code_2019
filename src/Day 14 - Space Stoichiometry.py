# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


from itertools import groupby


def read_input(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    return contents


def transform_input(data):
    memory = data.split("\n")
    memory1 = []
    for item in memory:
        item1 = item.replace(',', '')
        memory1.append(item1.split(' '))

    return memory1


def repeater(d, previous_item, item, level):

    previous_batch = d[previous_item]['batch']
    batch = d[previous_item]['requires'][item]
    print(('   ' * level + 'A batch of {} {} requires {} {}')
          .format(previous_batch, previous_item, batch, item))
    if item == 'ORE':
        return [], 0

    next_requires = d[item]['requires']
    # print('Next requries {}'.format(next_requires))
    # print('Ingredient = '.format(item))
    return next_requires, level + 1
    # next_requires = d[item]['requires']

    # return next_requires, level + 1
    # return item, next_requires
# batch = dict2[item8]['batch']
# batch1 = dict2[item8]['requires'][item9]
# print('\t\t\t\tA batch of {} {} requires {} {}'.format(batch, item8, batch1, item9))
# if item9 == 'ORE':
#     continue

# requires9 = dict2[item9]['requires']


def repeater1(previous_item, requires):
    for item in requires:
        previous_batch = dict2[previous_item]['batch']
        batch = dict2[previous_item]['requires'][item]
        print('\t\t\t\tA batch of {} {} requires {} {}'.
              format(previous_batch, previous_item, batch, item))
        if item == 'ORE':
            continue

    next_requires = dict2[item]['requires']

    return next_requires
    # return item, next_requires


# %% Development Environment

txtfile = "../data/adventofcode_2019_day_14_input.txt"
start = read_input(txtfile)
start_vector = transform_input(start)

dict2 = {}

for outer_item in start_vector:
    quantities = []
    ingredients = []
    for inner_item in outer_item:
        if inner_item.isnumeric():
            quantities.append(int(inner_item))
        elif inner_item == '=>':
            row_dict = {}
        else:
            ingredients.append(inner_item)
    # print()
    for index in range(len(ingredients) - 1):
        row_dict[ingredients[index]] = quantities[index]

    dict1 = {}
    dict1[ingredients[len(ingredients) - 1]] = \
        {'batch': quantities[len(ingredients) - 1],
         'requires': row_dict}
    dict2 = {**dict2, **dict1}


item = 'FUEL'
requires = dict2[item]['requires']
level = 0

for item1 in requires:
    requires1, level1 = repeater(dict2, item, item1, level)

    for item2 in requires1:
        requires2, level2 = repeater(dict2, item1, item2, level1)

        for item3 in requires2:
            requires3, level3 = repeater(dict2, item2, item3, level2)

            for item4 in requires3:
                requires4, level4 = repeater(dict2, item3, item4, level3)

                for item5 in requires4:
                    requires5, level5 = repeater(dict2, item4, item5, level4)

                    for item6 in requires5:
                        requires6, level6 = repeater(dict2, item5, item6, level5)

                        for item7 in requires6:
                            requires7, level7 = repeater(dict2, item6, item7, level6)

                            for item8 in requires7:
                                requires8, level8 = repeater(dict2, item7, item8, level7)

                                for item9 in requires8:
                                    requires9, level9 = repeater(dict2, item8, item9, level8)

                                    for item10 in requires9:
                                        requires10, level10 = repeater(dict2, item9, item10, level9)
    
                                        for item11 in requires10:
                                            requires11, level11 = repeater(dict2, item10, item11, level10)


# %% Production Environment

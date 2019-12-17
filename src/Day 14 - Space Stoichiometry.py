# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


# from itertools import groupby
import math


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
        item1 = item1.split(' ')
        item1.reverse()
        memory1.append(item1)

    return memory1


def repeater(d, previous_item, item, level):

    previous_batch = d[previous_item]['batch']
    batch = d[previous_item]['requires'][item]
    print(('   ' * level + 'A batch of {} {} requires {} {}')
          .format(previous_batch, previous_item, batch, item))
    if item == 'ORE':
        return [], 0

    next_requires = d[item]['requires']
    previous_item = item
    # return next_requires, level + 1
    for item in next_requires:
        repeater(d, previous_item, item, level + 1)


def create_ingredient_dictionary(data):
    d = {i: {'name': data[i][0], 'batch_size': int(data[i][1])}
         for i in range(len(data))}

    return d


def create_recipe_dictionary(data):
    d = {i: {'recipe':
             {data[i][3 + k * 2]: int(data[i][4 + k * 2])
              for k in range((len(data[i]) - 3) // 2)}}
         for i in range(len(data))}

    return d


def create_ingredient_dictionary_1(data):
    d = {data[i][0]: {'batch_size': int(data[i][1]),
                      'recipe':
                          {data[i][3 + k * 2]: int(data[i][4 + k * 2])
                           for k in range((len(data[i]) - 3) // 2)}}
         for i in range(len(data))}

    return d


def create_cookbook_dictionary(data):
    d = {i: {'recipe':
             {data[i][3 + k * 2]: int(data[i][4 + k * 2])
              for k in range((len(data[i]) - 3) // 2)}}
         for i in range(len(data))}

    return d


def drop3(data):
    return [data[i][:len(data[i]) - 3] for i in range(len(data))]


def create_dict2(data):
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
        for index in range(1, len(ingredients)):
        # for index in range(len(ingredients) - 1):
            row_dict[ingredients[index]] = quantities[index]

        dict1 = {}
        dict1[ingredients[0]] = \
            {'batch': quantities[0],
             'requires': row_dict}
        # dict1[ingredients[len(ingredients) - 1]] = \
        #     {'batch': quantities[len(ingredients) - 1],
        #      'requires': row_dict}
        dict2 = {**dict2, **dict1}

    return dict2


# %% Development Environment

txtfile = "../data/adventofcode_2019_day_14_input.txt"
start = read_input(txtfile)
start_vector = transform_input(start)

# make ingredient dictionary
# ingredients1 = create_ingredient_dictionary(start_vector)
ingredients = create_ingredient_dictionary_1(start_vector)

# make recipe dictionary
# recipes = create_recipe_dictionary(start_vector)
# start_vector1 = drop3(start_vector.copy())

# Create recursion dictionary
recursion = {}

# Seed reaction chain
ingredient = 'FUEL'
next_ingredient = {ingredient: {
    'batch_size': ingredients[ingredient]['batch_size'],
    'needed': 1,
    'batches_to_make': 0,
    'recipe': dict(ingredients[ingredient]['recipe']),
    'reaction_chain_level': 0}}
recursion = {**recursion,
             **next_ingredient}
             # **{ingredient: {
             #     'batch_size': ingredients1[ingredient]['batch_size'],
             #     'needed': 1,
             #     'batches_to_make': 0,
             #     'recipe': dict(ingredients1[ingredient]['recipe']),
             #     'reaction_chain_level': 0}}}
# Aggragate next level of requirments
# ingredient = recursion[ingredient]['recipe'][0][0]

d = {ingredient: {
    'batch_size': ingredients[ingredient]['batch_size'],
    'needed': 1,
    'batches_to_make': 0,
    'recipe': dict(ingredients[ingredient]['recipe']),
    'reaction_chain_level': 0}}




# recursion = {**recursion,
#              **{item[0]: for item[0] in recursion.items: \
#                     for item1[0] in recursion.items['recipe'].items:
#                         item['needed'] * item1[1]}}










# dict2 = create_dict2(start_vector)








# item = 'FUEL'
# requires = dict2[item]['requires']
# level = 0

# # for item1 in requires:
# #     repeater(dict2, item, item1, level)

# item = 'FUEL'
# needed = 1
# ingredients = dict2[item]['requires']
# ingredients_index = list(ingredients.keys())

# print('To make {} {}, we:'.format(needed, item))
# for item1 in ingredients:
#     # item1 = ingredients_index[i]
#     needed = dict2[item]['requires'][item1]

#     batch = dict2[item1]['batch']
#     batches = needed // batch + 1 if needed % batch else 0
#     make = batches * batch

#     print('  Need {} {}. Making {} batch(s) for a total of {}'.format(needed, item1, batches, make))




# %% Production Environment

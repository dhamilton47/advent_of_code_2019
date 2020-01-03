# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


# from itertools import groupby
import math

import aoc


def transform_input(data):
    memory = data.split("\n")
    memory1 = []
    for item in memory:
        item1 = item.replace(',', '')
        item1 = item1.split(' ')
        item1.reverse()
        memory1.append(item1)

    return memory1


def create_dictionary(data):
    d = {data[i][0]: []
         for i in range(len(data))}

    return d


def create_chemicals_dictionary(data):
    d = {data[i][0]: {'batch_size': int(data[i][1]),
                      'recipe':
                          {data[i][3 + k * 2]: int(data[i][4 + k * 2])
                           for k in range((len(data[i]) - 3) // 2)}}
         for i in range(len(data))}

    return d


def printa(chem, qty, need):
    print(f"  chemical = {chem}, quantity = {qty}, needed = {need}")


def print_repeat(chem, dc):
    need = dc[chem]['needed']
    lvl = dc[chem]['chain_reaction_level']
    print('  ' * lvl + f"Repeat: Need {need} more {chem}, lvl {lvl}")


def print_new(chem, nc):
    need = nc[chem]['needed']
    lvl = nc[chem]['chain_reaction_level']
    print('  ' * lvl + f"New: Need {need} {chem}, lvl {lvl}")


def order_record(chem, chem_name, lvl, qty=1, need=1):
    need = qty * need
    flag = False
    if chem == 'ORE':
        flag = True
        qty = 1
    order = {chem_name: {
        'batch_size': 1 if flag else chem['batch_size'],
        'needed': qty * need,
        'batches_to_make': qty * need if flag else 0,
        'recipe': [] if flag else dict(chem['recipe']),
        'making': 0,
        'extra_available': 0,
        'chain_reaction_level': lvl}}
    return order


def create_order(ledger,
                 inventory,
                 orders,
                 chemicals,
                 order_key_index,
                 chem_name,
                 lvl=0,
                 qty=1,
                 need=1):
    chem = chemicals[chem_name]
    order = order_record(chem, chem_name, lvl, qty, need)
    key, order_key_index = get_order_key_index(order_key_index)
    orders[key] = order

    return order_key_index


def needs_analysis(orders, chemicals, lvl):
    lvl += 1
    for ord_no, order in orders.items():
        print('Order number:', ord_no)
        for item_number, item in order.items():
            print('Item name:', item_number)
            if item['chain_reaction_level'] == lvl - 1:
                n = item['needed']

    return orders, chemicals


def requirements(dc, di):
    for item in list(dc.keys()):
        chem = dc[item]
        chem['batches_to_make'] = math.ceil(chem['needed']
                                            / chem['batch_size'])
        chem['making'] = chem['batches_to_make'] * chem['batch_size']
        chem['extra_available'] = chem['making'] - chem['needed']
    return dc, di


def add_chemicals(orders, chemicals, chem='FUEL', need=1, qty=1, lvl=0):
    """
    dc = Recursive dictionary for tracing chemical reaction needs
    de = Information dictionary for the chemicals
    lvl = Indicator to avoid double counting of needed chemicals as new
            reactions are added to the Recursive dictionary
    need = Amount of a chemical needed by this reaction
    qty = Cumulative amount of a particular chemical needed prior to
    """

    new_need = qty * need

    new_order = create_order(orders, chemicals,
                             order_key_index, chem, lvl, qty, need)

    if chem in orders.keys():
        # Repeat chemical need; don't want to overwrite previous entries.
        print_repeat(chem, orders)
        orders[chem]['needed'] = orders[chem]['needed'] + new_need
    else:
        # First entry for a chem
        new_chem = {chem: {
            'batch_size': 1 if chem == 'ORE'
            else chemicals[chem]['batch_size'],
            'needed': qty * need,
            'batches_to_make': qty * need if chem == 'ORE' else 0,
            'recipe': [] if chem == 'ORE' else dict(chemicals[chem]['recipe']),
            'making': 0,
            'extra_available': 0,
            'chain_reaction_level': lvl}}

        new_chem1 = {
            'batch_size': 1 if chem == 'ORE'
            else chemicals[chem]['batch_size'],
            'needed': qty * need,
            'batches_to_make': qty * need if chem == 'ORE' else 0,
            'recipe': [] if chem == 'ORE' else dict(chemicals[chem]['recipe']),
            'chain_reaction_level': lvl}

        orders[chem] = new_chem1
        print_new(chem, new_chem)
    return orders, chem


def get_order_key_index(order_key_index):
    index = order_key_index
    order_key_index += 1
    return index, order_key_index


def get_reaction_level_index(reaction_level_index):
    index = reaction_level_index
    reaction_level_index += 1
    return index


def pull_previous_order(ledger,
                        inventory,
                        orders,
                        chemicals,
                        order_key_index,
                        reaction_level_index):
    # get_reaction_level_index(reaction_level_index)
    for ldg_item, ldg_hist in ledger.items():
        if len(ldg_hist):
            print('Ledger item:', ldg_item)
        for order in ldg_hist:
            print(f"  Ledger entry: {order}")
            print(reaction_level_index)
            # print('Item details:', item)

            if order['chain_reaction_level'] == reaction_level_index - 1:
                print('yes')
                print(order['recipe'].items())
                for chem_name, amount in order['recipe'].items():
                    print(f"{chem_name} {amount}")
                    order_key_index = create_order(ledger,
                                                   inventory,
                                                   orders,
                                                   chemicals,
                                                   order_key_index,
                                                   chem_name,
                                                   reaction_level_index)


# %% Development Environment

txtfile = "../data/AoC2019_day_14_input.txt"

raw_data = aoc.read_program(txtfile)
data = transform_input(raw_data)

chemicals = create_chemicals_dictionary(data)
ledger = create_dictionary(data)
inventory = create_dictionary(data)

order_key_index = 0
reaction_level_index = 0
orders = {}

chem_name = 'FUEL'

order_key_index = create_order(ledger,
                               inventory,
                               orders,
                               chemicals,
                               order_key_index,
                               chem_name,
                               reaction_level_index)

for order_number, order in orders.items():
    for chem, chem_details in order.items():
        ledger[chem].append(chem_details)


# Create next level of orders
reaction_level_index += 1
orders = {}
pull_previous_order(ledger,
                    inventory,
                    orders,
                    chemicals,
                    order_key_index,
                    reaction_level_index)

for order_number, order in orders.items():
    for chem, chem_details in order.items():
        ledger[chem].append(chem_details)


# Create next level of orders
reaction_level_index += 1
orders = {}
pull_previous_order(ledger,
                    inventory,
                    orders,
                    chemicals,
                    order_key_index,
                    reaction_level_index)

# needs_analysis(orders, chemicals, reaction_level_index)

# %% Production Environment

# txtfile = "../data/adventofcode_2019_day_14_input.txt"
# raw_data = read_input(txtfile)
# data = transform_input(raw_data)

# chemicals = create_chemicals_dictionary(data)
# ledger = create_dictionary(data)
# inventory = create_dictionary(data)
# orders = {}
# cookbook = day_14_part_1(txtfile)


# %%


def day_14_part_1(chemicals, ledger, inventory, orders,
                  initial_chemical='FUEL', need=1):
    # Seed reaction chain
    reaction_level_index = 0
    create_order(orders, chemicals, order_key_index,
                 initial_chemical, reaction_level_index)

    # Add order to Ledger
    for order_number, order in orders.items():
        for chem, chem_details in order.items():

            # print(chem, chem_details, ledger[chem])
            ledger[chem].append(chem_details)
    orders = {}

    # Create next level of orders
    reaction_level_index += 1
    pull_previous_order(ledger, orders, reaction_level_index)
    # needs_analysis(orders, chemicals, reaction_level_index)



# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:41:25 2019

@author: Dan J. Hamilton
"""


# %% Import the program data (as a string)

def read_intcode_program(file_path):
    """ Read the context of a .txt file """

    with open(file_path, 'r') as file:
        contents = file.read().split(',')

    contents = [int(_) for i, _ in enumerate(contents)]

    return contents


def read_program(file_path):
    """ Read the context of a .txt file """

    with open(file_path, 'r') as file:
        contents = file.read()

    return contents


# %% Program Dictionary

PROGRAMS_AVAILABLE_DICTIONARY = {
    'Gravity Assist':
        {
            'binary': '../data/AoC2019_day_2_input.txt',
            'copies': ['GravAsst'],
            'description': 'Gravity Assist Program',
            'name': 'GravAsst',
        },

    'System Diagnostics':
        {
            'binary': '../data/AoC2019_day_5_input.txt',
            'copies': ['Diagnostics'],
            'description': 'Spacecraft System Diagnostic Program',
            'name': 'Diagnostics',
        },

    'Amp':
        {
            'binary': '../data/AoC2019_day_7_input.txt',
            'copies': ['ampA', 'ampB', 'ampC', 'ampD', 'ampE'],
            'description': 'Amplifier Controller Software',
            'name': 'Amp',
        },

    'BOOST':
        {
            'binary': '../data/AoC2019_day_9_input.txt',
            'copies': ['BOOST'],
            'description': 'Basic Operation Of System Test Program',
            'name': 'BOOST',
        },

    'Registration Identifier':
        {
            'binary': '../data/AoC2019_day_11_input.txt',
            'copies': ['Registration'],
            'description': 'Emergency Hull Painting Robot Software',
            'name': 'Registration',
        },

    'Arcade Cabinet':
        {
            'binary': '../data/AoC2019_day_13_input.txt',
            'copies': ['Breakout'],
            'description': 'Arcade Cabinet Video Game Software',
            'name': 'Game',
        },

    'Oxygen System':
        {
            'binary': '../data/AoC2019_day_15_input.txt',
            'copies': ['Oxygen'],
            'description': 'Repair Droid Remote Control Program',
            'name': 'Repair Droid',
        },

    'ASCII':
        {
            'binary': '../data/AoC2019_day_17_input.txt',
            'copies': ['ASCII'],
            'description': 'Aft Scaffolding Control and Information Interface',
            'name': 'ascii_enabled',
        },

    'Tractor Beam':
        {
            'binary': '../data/AoC2019_day_19_input.txt',
            'copies': ['TractorBeam'],
            'description': 'Drone Control Program',
            'name': 'TractorBeam',
        },

    'Springdroid':
        {
            'binary': '../data/AoC2019_day_21_input.txt',
            'copies': ['Springdroid'],
            'description': 'ASCII-capable Springscript Translation Program',
            'name': 'springscript',
        },

    'NIC':
        {
            'binary': '../data/AoC2019_day_23_input.txt',
            'copies': ['NIC'],
            'description': 'Network Interface Controller (NIC) Software',
            'name': 'NIC',
        },

    'Search Droid':
        {
            'binary': '../data/AoC2019_day_25_input.txt',
            'copies': ['Search'],
            'description': 'ASCII-capable Droid Communications Program',
            'name': 'Droid Communications',
        },

    'None':
        {
            'name': '',
            'copies': [],
            'binary': ''
        },
}

# %% OpCode Dictionary

OPCODE_DICTIONARY = {
    1: {'opcode': 1, 'length': 4, 'func': 'add', 'params': [0, 0, 0]},
    2: {'opcode': 2, 'length': 4, 'func': 'multiply', 'params': [0, 0, 0]},
    3: {'opcode': 3, 'length': 2, 'func': 'input', 'params': [0]},
    4: {'opcode': 4, 'length': 2, 'func': 'output', 'params': [0]},
    5: {'opcode': 5, 'length': 3, 'func': 'jump-if-true', 'params': [0, 0]},
    6: {'opcode': 6, 'length': 3, 'func': 'jump-if-false', 'params': [0, 0]},
    7: {'opcode': 7, 'length': 4, 'func': 'lt', 'params': [0, 0, 0]},
    8: {'opcode': 8, 'length': 4, 'func': 'eq', 'params': [0, 0, 0]},
    9: {'opcode': 9, 'length': 2, 'func': 'rebase', 'params': [0]},
    99: {'opcode': 99, 'length': 1, 'func': 'exit', 'params': []},
}

MODE_DICTIONARY = {
    0: {'modes': [0, 0, 0]},
    1: {'modes': [1, 0, 0]},
    2: {'modes': [2, 0, 0]},
    10: {'modes': [0, 1, 0]},
    11: {'modes': [1, 1, 0]},
    12: {'modes': [2, 1, 0]},
    20: {'modes': [0, 2, 0]},
    21: {'modes': [1, 2, 0]},
    22: {'modes': [2, 2, 0]},
    100: {'modes': [0, 0, 1]},
    101: {'modes': [1, 0, 1]},
    102: {'modes': [2, 0, 1]},
    110: {'modes': [0, 1, 1]},
    111: {'modes': [1, 1, 1]},
    112: {'modes': [2, 1, 1]},
    120: {'modes': [0, 2, 1]},
    121: {'modes': [1, 2, 1]},
    122: {'modes': [2, 2, 1]},
    200: {'modes': [0, 0, 2]},
    201: {'modes': [1, 0, 2]},
    202: {'modes': [2, 0, 2]},
    210: {'modes': [0, 1, 2]},
    211: {'modes': [1, 1, 2]},
    212: {'modes': [2, 1, 2]},
    220: {'modes': [0, 2, 2]},
    221: {'modes': [1, 2, 2]},
    222: {'modes': [2, 2, 2]},
}

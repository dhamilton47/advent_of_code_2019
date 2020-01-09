# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:41:25 2019

@author: Dan J. Hamilton
"""


# %% Import the "XXXX" data (as a string)
def read_program(txtfile):
    """ Read the context of a .txt file """
    file = open(txtfile, "r")
    if file.mode == 'r':
        contents = file.read()
    file.close()

    return contents


# %% Program Dictionary

PROGRAMS_AVAILABLE_DICTIONARY = {
    'Gravity Assist':
        {
            'binary': '../data/AoC2019_day_2_input.txt',
            'copies': ['GravAsst'],
            'description': 'Gravity Assist Program',
            'io_in': ['keyboard', 'keyboard'],
            'io_out': ['monitor'],
            'messages_in': ['Noun = ', 'Verb = '],
            'messages_out': ['Day 2, Part 1 - Value at position 0 =',
                             'Day 2, Part 2 - 100 * noun + verb ='],
            'name': 'GravAsst',
        },

    'System Diagnostics':
        {
            'binary': '../data/AoC2019_day_5_input.txt',
            'copies': ['Diagnostics'],
            'description': 'Spacecraft System Diagnostic Program',
            'io_in': ['keyboard'],
            'io_out': ['monitor',
                       'monitor',
                       'monitor',
                       'monitor',
                       'monitor',
                       'monitor',
                       'monitor',
                       'monitor',
                       'monitor',
                       'monitor', ],
            'messages_in': ['Which System ID are we testing? '],
            'messages_out': ['Diagnostic test =',
                             'Diagnostic test =',
                             'Diagnostic test =',
                             'Diagnostic test =',
                             'Diagnostic test =',
                             'Diagnostic test =',
                             'Diagnostic test =',
                             'Diagnostic test =',
                             'Diagnostic test =',
                             'Day 5, Part 1 - Diagnostic code =',
                             'Day 5, Part 2 - Diagnostic code ='],
            'name': 'Diagnostics',
            # 'process_order': 'sequential',
        },

    'Amp':
        {
            # 'binary': '../data/adventofcode_2019_day_7_input5.txt',
            'binary': '../data/AoC2019_day_7_input.txt',
            'copies': ['ampA', 'ampB', 'ampC', 'ampD', 'ampE'],
            'description': 'Amplifier Controller Software',
            'io_in': ['emulated', 'emulated'],
            'io_out': ['monitor'],
            'messages_in': ['Enter phase: ',
                            'Enter input signal: '],
            'messages_out': ['Output signal: '],
            'name': 'Amp',
            # 'process_order': 'sequential',
        },

    'BOOST':
        {
            'binary': '../data/AoC2019_day_9_input.txt',
            'copies': ['BOOST'],
            'description': 'Basic Operation Of System Test Program',
            'io_in': ['keyboard'],
            'io_out': ['monitor'],
            'messages_in': ['Enter test number: '],
            'messages_out': ['BOOST keycode ='],
            'name': 'BOOST',
        },

    'Registration Identifier':
        {
            'binary': '../data/AoC2019_day_11_input.txt',
            'copies': ['Registration'],
            'description': 'Emergency Hull Painting Robot Software',
            'io_in': ['emulated'],
            'io_out': ['monitor', 'monitor'],
            'messages_in': ['Enter color code (0 = black, 1 = white): '],
            'messages_out': ['Paint panel (0 = black, 1 = white): ',
                             'Turn (0 = left, 1 = right): '],
            'name': 'Registration',
        },

    'Arcade Cabinet':
        {
            'binary': '../data/AoC2019_day_13_input.txt',
            'copies': ['Breakout'],
            'description': 'Arcade Cabinet Video Game Software',
            'io_in': ['emulated'],
            'io_out': ['monitor', 'monitor', 'monitor'],
            'messages_in': ['start'],
            'messages_out': ['x coordinate = ',
                             'y coordinate = ',
                             'Object = '],
            'name': 'Game',
        },

    'Oxygen System':
        {
            'binary': '../data/AoC2019_day_15_input.txt',
            'copies': ['Oxygen'],
            'description': 'Repair Droid Remote Control Program',
            'io_in': ['emulated'],
            'io_out': ['monitor', 'monitor', 'monitor'],
            'messages_in': ['start'],
            'messages_out': ['x coordinate = ',
                             'y coordinate = ',
                             'Object = '],
            'name': 'Repair Droid',
        },

    'ASCII':
        {
            'binary': '../data/AoC2019_day_17_input.txt',
            'copies': ['ASCII'],
            'description': 'Aft Scaffolding Control and Information Interface',
            'io_in': ['emulated'],
            'io_out': ['monitor', 'monitor', 'monitor'],
            'messages_in': ['start'],
            'messages_out': ['x coordinate = ',
                             'y coordinate = ',
                             'Object = '],
            'name': 'ASCII',
        },

    'Tractor Beam':
        {
            'binary': '../data/AoC2019_day_19_input.txt',
            'copies': ['TractorBeam'],
            'description': 'Drone Control Program',
            'io_in': ['emulated'],
            'io_out': ['monitor', 'monitor', 'monitor'],
            'messages_in': ['start'],
            'messages_out': ['x coordinate = ',
                             'y coordinate = ',
                             'Object = '],
            'name': 'TractorBeam',
        },

    'Springdroid':
        {
            'binary': '../data/AoC2019_day_21_input.txt',
            'copies': ['Springdroid'],
            'description': 'ASCII-capable Springscript Translation Program',
            'io_in': ['emulated'],
            'io_out': ['monitor', 'monitor', 'monitor'],
            'messages_in': ['start'],
            'messages_out': ['x coordinate = ',
                             'y coordinate = ',
                             'Object = '],
            'name': 'springscript',
        },

    'Ship Network':
        {
            'binary': '../data/AoC2019_day_23_input.txt',
            'copies': ['NIC'],
            'description': 'Network Interface Controller (NIC) Software',
            'io_in': ['emulated'],
            'io_out': ['monitor', 'monitor', 'monitor'],
            'messages_in': ['start'],
            'messages_out': ['x coordinate = ',
                             'y coordinate = ',
                             'Object = '],
            'name': 'NIC',
        },

    'Search Droid':
        {
            'binary': '../data/AoC2019_day_25_input.txt',
            'copies': ['Search'],
            'description': 'ASCII-capable Droid Communications Program',
            'io_in': ['emulated'],
            'io_out': ['monitor', 'monitor', 'monitor'],
            'messages_in': ['start'],
            'messages_out': ['x coordinate = ',
                             'y coordinate = ',
                             'Object = '],
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

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
                       'monitor',],
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
            'binary': '../data/AoC2019_day_7_input.txt',
            'copies': ['ampA', 'ampB', 'ampC', 'ampD', 'ampE'],
            'description': 'Amplifier Controller Software',
            'io_in': ['buffer', 'buffer'],
            'io_out': ['buffer', 'buffer'],
            'messages_in': ['Enter phase: ',
                            'Enter input signal: '],
            'messages_out': ['Output signal: ',
                             'Max thruster signal ='],
            'name': 'Amps',
            'process_order': 'sequential',
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
            'name': 'Repair Program',
        },

    'ASCII':
        {
            'binary': '../data/AoC2019_day_17_input.txt',
            'copies': ['ASCII'],
            'description': 'Aft Scaffolding Control and Information Interface',
            'name': 'ASCII',
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

    'Ship Network':
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
    1: {
        'opcode': 1,
        'length': 4,
        'function': 'add',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'position',
                  'position']
        },

    101: {
        'opcode': 1,
        'length': 4,
        'function': 'add',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'position',
                  'position']
        },

    1001: {
        'opcode': 1,
        'length': 4,
        'function': 'add',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'immediate',
                  'position']
        },

    1101: {
        'opcode': 1,
        'length': 4,
        'function': 'add',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'immediate',
                  'position']
        },


    10001: {
        'opcode': 1,
        'length': 4,
        'function': 'add',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'position',
                  'immediate']
        },

    10101: {
        'opcode': 1,
        'length': 4,
        'function': 'add',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'position',
                  'immediate']
        },

    11101: {
        'opcode': 1,
        'length': 4,
        'function': 'add',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'immediate',
                  'immediate']
        },

    2: {
        'opcode': 2,
        'length': 4,
        'function': 'multiply',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'position',
                  'position']
        },

    102: {
        'opcode': 2,
        'length': 4,
        'function': 'multiply',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'position',
                  'position']
        },

    1002: {
        'opcode': 2,
        'length': 4,
        'function': 'multiply',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'immediate',
                  'position']
        },

    1102: {
        'opcode': 2,
        'length': 4,
        'function': 'multiply',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'immediate',
                  'position']
        },

    10002: {
        'opcode': 2,
        'length': 4,
        'function': 'multiply',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'position',
                  'immediate']
        },

    10102: {
        'opcode': 2,
        'length': 4,
        'function': 'multiply',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'position',
                  'immediate']
        },

    11102: {
        'opcode': 2,
        'length': 4,
        'function': 'multiply',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'immediate',
                  'immediate']
        },

    3: {
        'opcode': 3,
        'length': 2,
        'function': 'input',
        'parameters': [0],
        'modes': ['position']
        },

    103: {
        'opcode': 3,
        'length': 2,
        'function': 'input',
        'parameters': [0],
        'modes': ['immediate']
        },

    4: {
        'opcode': 4,
        'length': 2,
        'function': 'output',
        'parameters': [0],
        'modes': ['position']
        },

    104: {
        'opcode': 4,
        'length': 2,
        'function': 'input',
        'parameters': [0],
        'modes': ['immediate']
        },

    5: {
        'opcode': 5,
        'length': 3,
        'function': 'jump-if-true',
        'parameters': [0, 0],
        'modes': ['position',
                  'position']
        },

    105: {
        'opcode': 5,
        'length': 3,
        'function': 'jump-if-true',
        'parameters': [0, 0],
        'modes': ['immediate',
                  'position']
        },

    1005: {
        'opcode': 5,
        'length': 3,
        'function': 'jump-if-true',
        'parameters': [0, 0],
        'modes': ['position',
                  'immediate']
        },

    1105: {
        'opcode': 5,
        'length': 3,
        'function': 'jump-if-true',
        'parameters': [0, 0],
        'modes': ['immediate',
                  'immediate']
        },

    6: {
        'opcode': 6,
        'length': 3,
        'function': 'jump-if-false',
        'parameters': [0, 0],
        'modes': ['position',
                  'position']
        },

    106: {
        'opcode': 6,
        'length': 3,
        'function': 'jump-if-false',
        'parameters': [0, 0],
        'modes': ['immediate',
                  'position']
        },

    1006: {
        'opcode': 6,
        'length': 3,
        'function': 'jump-if-false',
        'parameters': [0, 0],
        'modes': ['position',
                  'immediate']
        },

    1106: {
        'opcode': 6,
        'length': 3,
        'function': 'jump-if-false',
        'parameters': [0, 0],
        'modes': ['immediate',
                  'immediate']
        },

    7: {
        'opcode': 7,
        'length': 4,
        'function': 'less than',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'position',
                  'position']
        },

    107: {
        'opcode': 7,
        'length': 4,
        'function': 'less than',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'position',
                  'position']
        },

    1007: {
        'opcode': 7,
        'length': 4,
        'function': 'less than',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'immediate',
                  'position']
        },

    1107: {
        'opcode': 7,
        'length': 4,
        'function': 'less than',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'immediate',
                  'position']
        },

    10007: {
        'opcode': 7,
        'length': 4,
        'function': 'less than',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'position',
                  'immediate']
        },

    10107: {
        'opcode': 7,
        'length': 4,
        'function': 'less than',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'position',
                  'immediate']
        },

    11107: {
        'opcode': 7,
        'length': 4,
        'function': 'less than',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'immediate',
                  'immediate']
        },

    8: {
        'opcode': 8,
        'length': 4,
        'function': 'equals',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'position',
                  'position']
        },

    108: {
        'opcode': 8,
        'length': 4,
        'function': 'equals',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'position',
                  'position']
        },

    1008: {
        'opcode': 8,
        'length': 4,
        'function': 'equals',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'immediate',
                  'position']
        },

    1108: {
        'opcode': 8,
        'length': 4,
        'function': 'equals',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'immediate',
                  'position']
        },

    10008: {
        'opcode': 8,
        'length': 4,
        'function': 'equals',
        'parameters': [0, 0, 0],
        'modes': ['position',
                  'position',
                  'immediate']
        },

    10108: {
        'opcode': 8,
        'length': 4,
        'function': 'equals',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'position',
                  'immediate']
        },

    11108: {
        'opcode': 8,
        'length': 4,
        'function': 'equals',
        'parameters': [0, 0, 0],
        'modes': ['immediate',
                  'immediate',
                  'immediate']
        },

    9: {
        'opcode': 9,
        'length': 2,
        'function': 'rebase',
        'parameters': [0],
        'modes': ['immediate', ]
        },

    99: {
        'opcode': 99,
        'length': 1,
        'function': 'exit',
        'parameters': [],
        'modes': []
        },

    'None': {
        'opcode': 'None',
        'length': 0,
        'function': 'none',
        'parameters': 'None',
        'modes': 'None'
        },
}

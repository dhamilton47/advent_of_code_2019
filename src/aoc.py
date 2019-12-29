# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:41:25 2019

@author: Dan J. Hamilton
"""


# %% Import the "XXXX" data (as a string)
def read_program(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    return contents


# %% Program Dictionary

programs_available_dictionary = {
    'Gravity Assist': {'name': 'Gravity Assist',
                       'copies': ['GravAsst'],
                       'binary': '../data/adventofcode_2019_day_2_input.txt'},

    'System Diagnostics': {'name': 'Diagnostic Program',
                    'copies': ['Diagnostics'],
                    'binary': '../data/adventofcode_2019_day_5_input.txt'},

    'Amp': {'name': 'Amplifier Controller Software',
                  'copies': ['ampA', 'ampB', 'ampC', 'ampD'],
                  'binary': '../data/adventofcode_2019_day_7_input1.txt'},

    'BOOST': {'name': 'Basic Operation Of System Test',
              'copies': ['BOOST'],
              'binary': '../data/adventofcode_2019_day_9_input.txt'},

    'Registration Identifier': {'name': 'Emergency Hull Painting',
                                'copies': ['Registration'],
                                'binary': '../data/' +
                                'adventofcode_2019_day_11_input.txt'},

    'Arcade Cabinet': {'name': 'Arcade Game',
                       'copies': ['Arcade'],
                       'binary': '../data/adventofcode_2019_day_13_input.txt'},

    'Oxygen System': {'name': 'Remote Repair Program',
                      'copies': ['Oxygen'],
                      'binary': '../data/adventofcode_2019_day_15_input.txt'},

    'ASCII': {'name': 'Aft Scaffolding Control and Information Interface',
              'copies': ['ASCII'],
              'binary': '../data/adventofcode_2019_day_17_input.txt'},

    'Tractor Beam': {'name': 'Drone Control',
                     'copies': ['TractorBeam'],
                     'binary': '../data/adventofcode_2019_day_19_input.txt'},

    'Springdroid': {'name': 'springscript',
                    'copies': ['Springdroid'],
                    'binary': '../data/adventofcode_2019_day_21_input.txt'},

    'Ship Network': {'name': 'Network Interface Controller',
                     'copies': ['NIC'],
                     'binary': '../data/adventofcode_2019_day_23_input.txt'},

    'Search Droid': {'name': 'Droid Communications',
                     'copies': ['Search'],
                     'binary': '../data/adventofcode_2019_day_25_input.txt'},

    'None': {'name': '',
             'copies': [],
             'binary': ''}, }

# %% OpCode Dictionary

opcode_dictionary = {
            1: {'opcode': 1,
                'length': 4,
                'function': 'add',
                'parameters': [0, 0, 0],
                'modes': ['position',
                          'position',
                          'position']},
            101: {'opcode': 1,
                  'length': 4,
                  'function': 'add',
                  'parameters': [0, 0, 0],
                  'modes': ['immediate',
                            'position',
                            'position']},
            1001: {'opcode': 1,
                   'length': 4,
                   'function': 'add',
                   'parameters': [0, 0, 0],
                   'modes': ['position',
                             'immediate',
                             'position']},
            1101: {'opcode': 1,
                   'length': 4,
                   'function': 'add',
                   'parameters': [0, 0, 0],
                   'modes': ['immediate',
                             'immediate',
                             'position']},
            10001: {'opcode': 1,
                    'length': 4,
                    'function': 'add',
                    'parameters': [0, 0, 0],
                    'modes': ['position',
                              'position',
                              'immediate']},
            10101: {'opcode': 1,
                    'length': 4,
                    'function': 'add',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'position',
                              'immediate']},
            11101: {'opcode': 1,
                    'length': 4,
                    'function': 'add',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'immediate',
                              'immediate']},
            2: {'opcode': 2,
                'length': 4,
                'function': 'multiply',
                'parameters': [0, 0, 0],
                'modes': ['position',
                          'position',
                          'position']},
            102: {'opcode': 2,
                  'length': 4,
                  'function': 'multiply',
                  'parameters': [0, 0, 0],
                  'modes': ['immediate',
                            'position',
                            'position']},
            1002: {'opcode': 2,
                   'length': 4,
                   'function': 'multiply',
                   'parameters': [0, 0, 0],
                   'modes': ['position',
                             'immediate',
                             'position']},
            1102: {'opcode': 2,
                   'length': 4,
                   'function': 'multiply',
                   'parameters': [0, 0, 0],
                   'modes': ['immediate',
                             'immediate',
                             'position']},
            10002: {'opcode': 2,
                    'length': 4,
                    'function': 'multiply',
                    'parameters': [0, 0, 0],
                    'modes': ['position',
                              'position',
                              'immediate']},
            10102: {'opcode': 2,
                    'length': 4,
                    'function': 'multiply',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'position',
                              'immediate']},
            11102: {'opcode': 2,
                    'length': 4,
                    'function': 'multiply',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'immediate',
                              'immediate']},
            3: {'opcode': 3,
                'length': 2,
                'function': 'input',
                'parameters': [0],
                'modes': ['position']},
            103: {'opcode': 3,
                  'length': 2,
                  'function': 'input',
                  'parameters': [0],
                  'modes': ['immediate']},
            4: {'opcode': 4,
                'length': 2,
                'function': 'output',
                'parameters': [0],
                'modes': ['position']},
            104: {'opcode': 4,
                  'length': 2,
                  'function': 'input',
                  'parameters': [0],
                  'modes': ['immediate']},
            5: {'opcode': 5,
                'length': 3,
                'function': 'jump-if-true',
                'parameters': [0, 0],
                'modes': ['position',
                          'position']},
            105: {'opcode': 5,
                  'length': 3,
                  'function': 'jump-if-true',
                  'parameters': [0, 0],
                  'modes': ['immediate',
                            'position']},
            1005: {'opcode': 5,
                   'length': 3,
                   'function': 'jump-if-true',
                   'parameters': [0, 0],
                   'modes': ['position',
                             'immediate']},
            1105: {'opcode': 5,
                   'length': 3,
                   'function': 'jump-if-true',
                   'parameters': [0, 0],
                   'modes': ['immediate',
                             'immediate']},
            6: {'opcode': 6,
                'length': 3,
                'function': 'jump-if-false',
                'parameters': [0, 0],
                'modes': ['position',
                          'position']},
            106: {'opcode': 6,
                  'length': 3,
                  'function': 'jump-if-false',
                  'parameters': [0, 0],
                  'modes': ['immediate',
                            'position']},
            1006: {'opcode': 6,
                   'length': 3,
                   'function': 'jump-if-false',
                   'parameters': [0, 0],
                   'modes': ['position',
                             'immediate']},
            1106: {'opcode': 6,
                   'length': 3,
                   'function': 'jump-if-false',
                   'parameters': [0, 0],
                   'modes': ['immediate',
                             'immediate']},
            7: {'opcode': 7,
                'length': 4,
                'function': 'less than',
                'parameters': [0, 0, 0],
                'modes': ['position',
                          'position',
                          'position']},
            107: {'opcode': 7,
                  'length': 4,
                  'function': 'less than',
                  'parameters': [0, 0, 0],
                  'modes': ['immediate',
                            'position',
                            'position']},
            1007: {'opcode': 7,
                   'length': 4,
                   'function': 'less than',
                   'parameters': [0, 0, 0],
                   'modes': ['position',
                             'immediate',
                             'position']},
            1107: {'opcode': 7,
                   'length': 4,
                   'function': 'less than',
                   'parameters': [0, 0, 0],
                   'modes': ['immediate',
                             'immediate',
                             'position']},
            10007: {'opcode': 7,
                    'length': 4,
                    'function': 'less than',
                    'parameters': [0, 0, 0],
                    'modes': ['position',
                              'position',
                              'immediate']},
            10107: {'opcode': 7,
                    'length': 4,
                    'function': 'less than',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'position',
                              'immediate']},
            11107: {'opcode': 7,
                    'length': 4,
                    'function': 'less than',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'immediate',
                              'immediate']},
            8: {'opcode': 8,
                'length': 4,
                'function': 'equals',
                'parameters': [0, 0, 0],
                'modes': ['position',
                          'position',
                          'position']},
            108: {'opcode': 8,
                  'length': 4,
                  'function': 'equals',
                  'parameters': [0, 0, 0],
                  'modes': ['immediate',
                            'position',
                            'position']},
            1008: {'opcode': 8,
                   'length': 4,
                   'function': 'equals',
                   'parameters': [0, 0, 0],
                   'modes': ['position',
                             'immediate',
                             'position']},
            1108: {'opcode': 8,
                   'length': 4,
                   'function': 'equals',
                   'parameters': [0, 0, 0],
                   'modes': ['immediate',
                             'immediate',
                             'position']},
            10008: {'opcode': 8,
                    'length': 4,
                    'function': 'equals',
                    'parameters': [0, 0, 0],
                    'modes': ['position',
                              'position',
                              'immediate']},
            10108: {'opcode': 8,
                    'length': 4,
                    'function': 'equals',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'position',
                              'immediate']},
            11108: {'opcode': 8,
                    'length': 4,
                    'function': 'equals',
                    'parameters': [0, 0, 0],
                    'modes': ['immediate',
                              'immediate',
                              'immediate']},
            99: {'opcode': 99,
                 'length': 1,
                 'function': 'exit',
                 'parameters': [],
                 'modes': []},
            'None': {'opcode': 'None',
                     'length': 0,
                     'function': 'none',
                     'parameters': 'None',
                     'modes': 'None'},
            }
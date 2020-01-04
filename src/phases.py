# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:50:44 2019

@author: danha
"""

from register1 import Register1


# %%

def build_phase_choices(array, used_element):
    """
    Generate the remaining elements for the permuations as element is used.
    """
    remaining_elements = []
    for value in array:
        if value != used_element:
            remaining_elements.append(value)

    return remaining_elements


# %% Create 5P5 (permutations)

def phase_generator():
    """ Generate the permutations of initial set. """
    phase0 = [0, 1, 2, 3, 4]
    phases = []
    for index, element_1 in enumerate(phase0):
        phase1 = build_phase_choices(phase0, phase0[index])
        for index1, element_2 in enumerate(phase1):
            phase2 = build_phase_choices(phase1, phase1[index1])
            for index2, element_3 in enumerate(phase2):
                phase3 = build_phase_choices(phase2, phase2[index2])
                for index3, element_4 in enumerate(phase3):
                    phase4 = build_phase_choices(phase3, phase3[index3])
                    element_5 = phase4[0]
                    phases.append([element_1,
                                   element_2,
                                   element_3,
                                   element_4,
                                   element_5])

    return phases


def phase_generator1():
    """ Generate the permutations of initial set. """
    phase0 = [5, 6, 7, 8, 9]
    phases = []
    for index, element_1 in enumerate(phase0):
        phase1 = build_phase_choices(phase0, phase0[index])
        for index1, element_2 in enumerate(phase1):
            phase2 = build_phase_choices(phase1, phase1[index1])
            for index2, element_3 in enumerate(phase2):
                phase3 = build_phase_choices(phase2, phase2[index2])
                for index3, element_4 in enumerate(phase3):
                    phase4 = build_phase_choices(phase3, phase3[index3])
                    element_5 = phase4[0]
                    phases.append([element_1,
                                   element_2,
                                   element_3,
                                   element_4,
                                   element_5])

    return phases


def phase_load(data, index):
    """ Load each set of phase codes into the IntCode computer as required. """
    register = Register1()
    return register

    for i in register:
        register.register[i] = data[index][i]

    return register

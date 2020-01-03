# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:49:40 2019

@author: Dan J Hamilton
"""

# class Register
#     Properties
#         register


# %% Memory Class

class Register:
    """
        0: State,
        1: Input 1,
        2: Input 2,
        3: Output,
        4: Input counter,
        5: Output counter,
    """

    def __init__(self):
        self.register = {
            0: False,
            1: None,
            2: None,
            3: None,
            4: 1,
            5: 3,
        }

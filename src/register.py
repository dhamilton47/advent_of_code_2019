# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:49:40 2019

@author: Dan J Hamilton
"""

# class Register
#     Properties
#         program_name
#         purpose
#         value
#         state


# %% Memory Class

class Register:
    def __init__(self, purpose, value=None, state=0):
        # self.program_name = program_name
        self.purpose = purpose
        self.value = value
        self.state = state

    # def __init__(self, program_name, purpose, value=None, state=0):
    #     self.program_name = program_name
    #     self.purpose = purpose
    #     self.value = value
    #     self.state = state

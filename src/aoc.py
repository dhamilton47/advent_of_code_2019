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



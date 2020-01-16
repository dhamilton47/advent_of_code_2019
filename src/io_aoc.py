# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:25 2019

@author: Dan J Hamilton

"""


# %% IO Class

class IO:
    """
    Need to know I/O device to get/output data needed for execution
    of the Program(s).

    keyboard = user input from the keyboard
    buffer = an external function providing input to the buffer area.

    class IO
        Properties
            halt_condition
            input_value
            output_value

        Methods
            get_input
            return_output
    """

    def __init__(self):
        self.halt_condition = False
        self.input_value = None
        self.output_value = None

    def get_input(self):
        """
        Determine where and how to get input
        """

        return self.input_value.pop(0)

    def return_output(self, instruction):
        """
        Determine where to output results
        """

        self.output_value = instruction['parameters'][0]['value']

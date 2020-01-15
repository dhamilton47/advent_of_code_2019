# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:25 2019

@author: Dan J Hamilton
"""

"""
class IO
    Methods
        get_input
        return_output
"""


# %% IO Class

class IO:
    """
    Need to know I/O device to get/output data needed for execution
    of the Program(s).

    keyboard = user input from the keyboard
    buffer = an external function providing input to the buffer area.
    """

    def get_input(self, computer):
        """
        Determine where and how to get input
        """

        program = computer.program_loaded
        io_in, message_in = program.io_in

        if io_in == 'emulated':

            return computer.emulated_input.pop(0)

        raise ValueError('That device has not been attached.')

    def return_output(self, computer, instruction):
        """
        Determine where to output results
        """

        program = computer.program_loaded
        io_outs, messages_out = program.io_out

        if io_outs == 'emulated':
            computer.output_value = instruction['parameters'][0]['value']

            return

        raise ValueError('That device has not been attached.')

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:25 2019

@author: Dan J Hamilton
"""


# class IO
#     Methods
#         get_input
#         return_output


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

        process_active = computer.process_active
        program = computer.programs_loaded[process_active]
        io_in_count = program.io_in_count
        io_in = program.io_in[io_in_count]
        # print(f"I/O in device: {io_in}")

        message_in = program.messages_in[io_in_count]
        # print(f"message number = {io_in_count}, message = '{message_in}'")

        if io_in == 'keyboard':
            computer.programs_loaded[process_active].io_in_count += 1
            # program.messages_in_calls += 1
            return int(input(message_in))

        if io_in == 'buffer':
            io_in_count = program.io_in_count
            message_in = program.messages_in[io_in_count]

            buffer = computer.buffers[process_active].register
            value = buffer[buffer[4]]

            computer.buffers[process_active].register[4] += 1
            computer.programs_loaded[process_active].io_in_count += 1
            # print(f"{message_in}= {value}")

            return value

    def return_output(self, computer, instruction):
        """
        Determine where to output results
        """

        process_active = computer.process_active
        program = computer.programs_loaded[process_active]

        io_out_count = program.io_out_count
        io_out = program.io_out[io_out_count]
        # print(f"I/O out device: {io_out}")

        if io_out == 'monitor':
            message = program.messages_out[io_out_count]
            value = instruction['parameters'][0]['value']
            print(f"{message} {value}")

        elif io_out == 'buffer':
            buffer = computer.buffers[process_active].register
            computer.buffers[process_active].register[buffer[5]] = \
                instruction['parameters'][0]['value']
            # print(f"Register {buffer[5]} = "
            #       f"{computer.buffers[process_active].register[buffer[5]]}\n")
            computer.buffers[process_active].register[5] += 1
            computer.buffers[process_active].register[0] = False
            # return value

        program.io_out_count += 1

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
        process_active = computer.process_active
        # print(program.input_sources)
        program = computer.programs_loaded[process_active]
        io_in_count = program.io_in_count
        io_in = program.io_in[io_in_count]
        print(f"I/O in device: {io_in}")
        message_number = program.messages_in_calls
        message_in = program.messages_in[message_number]
        print(f"message number = {message_number}, message = '{message_in}'")
        if io_in == 'keyboard':
            # print(program.messages_in[program.messages_in_calls])
            # print(program['messages_in']['messages_in_calls'])
            program.messages_in_calls += 1
            return int(input(message_in))
            # print(answer)

        elif io_in == 'buffer':
            buffer = computer.buffers[process_active].register
            value = buffer[buffer[4]]
            print(f"Value in buffer [{process_active}] at register {buffer[4]}"
                  F" = {buffer[buffer[4]]}")
            computer.buffers[process_active].register[4] += 1
            return value

    def return_output(self, computer, instruction):
        process_active = computer.process_active
        # print(program.input_sources)
        program = computer.programs_loaded[process_active]
        io_out_count = program.io_out_count
        io_out = program.io_out[io_out_count]
        print(f"I/O out device: {io_out}")

        if io_out == 'monitor':
            message = program.messages_out[program.messages_out_calls]
            value = instruction['parameters'][0]['value']
            print(f"{message} {value}")

        elif io_out == 'buffer':
            buffer = computer.buffers[process_active].register
            computer.buffers[process_active].register[buffer[5]] = \
                instruction['parameters'][0]['value']
            computer.buffers[process_active].register[5] += 1
            computer.buffers[process_active].register[0] = False
            # return value

        program.messages_out_calls += 1

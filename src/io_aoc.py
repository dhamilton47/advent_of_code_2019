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
    # Need to know location to get/output information

    def get_input(self, computer, program_name):
        # print(program.input_sources)
        program = computer.programs_loaded[program_name]
        io_in = program_name.io_in
        message_number = program.messages_in_calls
        message_in = program.messages_in[message_number]
        if io_in == 'keyboard':
            # print(program.messages_in[program.messages_in_calls])
            # print(program['messages_in']['messages_in_calls'])
            return int(input(message_in))
            # print(answer)
            program.messages_in_calls += 1

        elif io_in == 'buffer':
            buffer = computer.buffers[program_name].register
            value = buffer[buffer[4]]
            computer.buffers[program_name].register[4] += 1
            return value

    def return_output(self, program, instruction):
        if program.io_out == 'monitor':
            message = program.messages_out[program.messages_out_calls]
            value = instruction['parameters'][0]['value']
            print(f"{message} {value}")

        elif program.io_out == 'buffer':
            pass

        program.messages_out_calls += 1

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

    # def get_input(self, computer, input1=None, input2=None):
    def get_input(self, computer):
        """
        Determine where and how to get input

        This program is still evolving as Day needs are revealed
        """

        program_name = computer.program_name
        program = computer.program_loaded

        # io_in_count = program.io_in_count
        # io_ins, messages_in = program.io_in
        # # print(io_in_count)
        # # io_in_count = io_in_count % len(io_ins)
        # # print(io_in_count)
        # io_in = io_ins[io_in_count]
        # message_in = messages_in[io_in_count]

        # One input only - emulated
        if program_name == 'Registration':
            # io_in_count = program.io_in_count
            io_ins, messages_in = program.io_in
            # io_in = io_ins[io_in_count]
            # message_in = messages_in[io_in_count]
            io_in = io_ins[0]
            message_in = messages_in[0]
            return computer.emulated_input

        # two input - first once, then repeatedly the 2nd - emulated
        if program_name == 'Amp':
            io_in_count = program.io_in_count
            io_ins, messages_in = program.io_in
            io_in = io_ins[io_in_count]
            message_in = messages_in[io_in_count]
            value = computer.emulated_input[io_in_count]

            computer.program_loaded.io_in_count = 1

            return value

        if io_in == 'keyboard':
            io_in_count = program.io_in_count
            io_ins, messages_in = program.io_in
            # print(io_in_count)
            # io_in_count = io_in_count % len(io_ins)
            # print(io_in_count)
            io_in = io_ins[io_in_count]
            message_in = messages_in[io_in_count]
            program.io_in_count += 1

            return int(input(message_in))

        if io_in == 'emulated':
            io_in_count = program.io_in_count
            io_ins, messages_in = program.io_in
            # print(io_in_count)
            # io_in_count = io_in_count % len(io_ins)
            # print(io_in_count)
            io_in = io_ins[io_in_count]
            message_in = messages_in[io_in_count]
            value = computer.emulated_input[io_in_count]
            # print(io_in_count, value)

            computer.program_loaded.io_in_count += 1

            return value

        else:
            raise ValueError('That device has not been attached.')

    def return_output(self, computer, instruction):
        """
        Determine where to output results
        """

        program_name = computer.program_name
        program = computer.program_loaded

        io_out_count = program.io_out_count
        io_outs, messages_out = program.io_out
        # io_out_count = io_out_count % len(io_outs)

        # if program_name != 'BOOST':
        #     io_out_count = io_out_count % len(io_outs)
        #     io_out = io_outs[io_out_count]
        #     message_out = messages_out[io_out_count]
        # else:
        #     io_out = io_outs[0]
        #     message_out = messages_out[0]
        #     print(f"I/O out device: {io_out}")

        if program_name == 'BOOST':
            io_out = io_outs[0]
            message_out = messages_out[0]
            value = instruction['parameters'][0]['value']
            computer.output_value = value
            return

        if program_name == 'Registration':
            # print(instruction['parameters'])
            value = instruction['parameters'][0]['value']
            program.io_out_count = not(program.io_out_count)

            computer.output_value = value
            return

        if io_out == 'monitor':
            io_out_count = io_out_count % len(io_outs)
            io_out = io_outs[io_out_count]
            message_out = messages_out[io_out_count]
            value = instruction['parameters'][0]['value']
            # print(f"{message_out} {value}")

            computer.output_value = value

        # elif io_out == 'buffer':
        #     buffer = computer.buffer.register
        #     computer.buffer.register[buffer[5]] = \
        #         instruction['parameters'][0]['value']
        #     # print(f"Register {buffer[5]} = "
        #     #       f"{computer.buffer.register[buffer[5]]}\n")
        #     computer.buffer.register[5] += 1
        #     computer.buffer.register[0] = False
        #     # else:

        else:
            raise ValueError('That device has not been attached.')

        program.io_out_count += 1

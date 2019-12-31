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
# Need to know location to get, output information

    def get_input(self, program):
        # print(program.input_sources)
        if program.input_sources == 'keyboard':
            # print(program.messages_in[program.messages_in_calls])
            # print(program['messages_in']['messages_in_calls'])
            answer = int(input(program.messages_in[program.messages_in_calls]))
            # print(answer)
            program.messages_in_calls += 1
            return answer
        elif program.input_sources == 'stack':
            pass

    def return_output(self, program, instruction):
        message = program.messages_out[program.messages_out_calls]
        value = instruction['parameters'][0]['value']
        print(f"{message} {value}")
        program.messages_out_calls += 1

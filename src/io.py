# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 00:05:25 2019

@author: Dan J Hamilton
"""


# %% IO Class

class IO:
    # def __init__(self, program=None):
    #     self.input_source = program['input_sources']
    #     self.messages_in = program['messages_in']
    #     self.messages_out = program['messages_out']
    #     self.messages_in_calls = program['messages_out_calls']
    #     self.messages_out_calls = program['messages_out_calls']

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

    def return_output(self):
        pass


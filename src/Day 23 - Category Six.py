# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 01:37:31 2020

@author: Dan J Hamilton
"""


import numpy as np

import aoc
from computer import Computer


"""
You'll need to rebuild the network from scratch.

The computers on the network are standard Intcode computers that
communicate by sending packets to each other. There are 50 of them
in total, each running a copy of the same Network Interface Controller
(NIC) software (your puzzle input). The computers have network
addresses 0 through 49; when each computer boots up, it will request
its network address via a single input instruction. Be sure to give
each computer a unique network address.

Once a computer has received its network address, it will begin doing
work and communicating over the network by sending and receiving
packets. All packets contain two values named X and Y. Packets sent
to a computer are queued by the recipient and read in the order
they are received.

To send a packet to another computer, the NIC will use three output
instructions that provide the destination address of the packet
followed by its X and Y values. For example, three output instructions
that provide the values 10, 20, 30 would send a packet with X=20 and
Y=30 to the computer with address 10.

To receive a packet from another computer, the NIC will use an
input instruction. If the incoming packet queue is empty,
provide -1. Otherwise, provide the X value of the next packet;
the computer will then use a second input instruction to receive
the Y value for the same packet. Once both values of the packet
are read in this way, the packet is removed from the queue.

Note that these input and output instructions never block.
Specifically, output instructions do not wait for the sent packet
to be received - the computer might send multiple packets before
receiving any. Similarly, input instructions do not wait for a
packet to arrive - if no packet is waiting, input instructions
should receive -1.

Boot up all 50 computers and attach them to your network. What is
the Y value of the first packet sent to address 255?
"""


# %%
def AND(x, y):
    return x & y


def OR(x, y):
    return x | y


def NOT(x, y):
    return not x


def ascii_interpreter(val):
    val1 = [ord(val[i]) for i in range(len(val))]
    # val1.append(10)

    return val1


def create_initial_network(network, input_queue):
    for i in range(50):
        network[i] = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'NIC')
        network[i].io.input_value = [i]
        input_queue[i] = []

    return network


def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.flash_memory()
    computer.halt_condition = True

    return computer


def main():
    pass


# %% Development Environment

opcode = 0

network = {}
input_queue = {}

network = create_initial_network(network, input_queue)


def input_queue_state(input_queue):
    if len(input_queue) == 0:
        emulated_input = [-1]
    else:
        x, y = input_queue[0]
        emulated_input = [x, y]

    return emulated_input


for i, _ in enumerate(network):
    network[i].process_run
    # for i, _ in enumerate(network):
    #     if len(input_queue[i]) == 0:
    #         network[i].emulated_input = [-1]
    #     else:
    #         x, y = input_queue[i][0]
    #         network[i].emulated_input = [x, y]
    network[i].io.input_value = input_queue_state(input_queue[i])

    network[i].process_run()
    address = network[i].io.output_value
    network[i].process_run()
    input_instruction = network[i].io.output_value
    network[i].process_run()
    y = network[i].io.output_value
    print(f"Address = {address}, x = {input_instruction}, y = {y}")
    input_queue[address].append((input_instruction, y))
    # else:
# input_queue[0] = []

# machine = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'NIC')
# machine.emulated_input = 0
# string = ''
# while opcode != 99:
#     machine.process_run()
#     if machine.output_value < 128:
#         # print(machine.output_value)
#         string += chr(machine.output_value)
#     else:
#         print(machine.output_value)
#         break

# print(chr(machine.output_value))


# %% Production Environment (LOL)

# if __name__ == "__main__":
#     main()

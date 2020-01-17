# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


import aoc
from computer import Computer


def blocks_remaining(display):
    """ Count the number of blocks to be broken """

    count = 0
    for i in range(1, 42):
        for j in range(1, 17):
            if display[j][i] == 2:
                count += 1

    return count


def output_cycle(machine):
    """ Cycle through the required number of """

    machine.process_run()
    left_offset = machine.io.output_value
    # left_offset = machine.output_value

    machine.process_run()
    top_offset = machine.io.output_value
    # top_offset = machine.output_value

    machine.process_run()
    item = machine.io.output_value
    # item = machine.output_value
    # print(f"x = {left_offset}, y = {top_offset}, item = {item}")

    return left_offset, top_offset, item  # , opcode


def create_initial_display(machine):
    """ Create the intial game display screen """

    display = [[0 for i in range(44)] for j in range(20)]
    opcode = 0

    while opcode != 99:
        opcode = machine.process_run()
        left_offset = machine.io.output_value
        # left_offset = machine.output_value
        if opcode == 99:
            break

        opcode = machine.process_run()
        top_offset = machine.io.output_value
        # top_offset = machine.output_value

        opcode = machine.process_run()
        item = machine.io.output_value
        # item = machine.output_value

        if item == 3:
            paddle_location = [left_offset, top_offset]

        if item == 4:
            ball_location = [left_offset, top_offset]

        display[top_offset][left_offset] = item

    return display, paddle_location, ball_location


def scoring(left_offset, top_offset, item, score):
    """ Keep the game score """

    if left_offset == -1 and top_offset == 0:
        score = item

    return score


def tracking(machine, paddle_location, ball_location, score):
    """ Track the movement of game objects """

    left_offset, top_offset, item = output_cycle(machine)

    score = scoring(left_offset, top_offset, item, score)

    if item == 3:
        paddle_location = [left_offset, top_offset]

    if item == 4:
        ball_location = [left_offset, top_offset]

    # print(f"Ball at ({ball_location[0], ball_location[1]}), "
    #       f"Paddle at ({paddle_location[0], paddle_location[1]}), "
    #       f"Score = {score}")

    return paddle_location, ball_location, score  # , opcode


def paddle_move(paddle_location, ball_location):
    """
    Move the paddle in response to ball movement so to keep the ball in play
    """

    if paddle_location[0] < ball_location[0]:
        return 1

    if paddle_location[0] > ball_location[0]:
        return -1

    return 0


def intcode(library, program):
    """ Create an IntCode Computer """

    computer = Computer(library, program)
    computer.flash_memory()
    computer.halt_condition = True

    return computer


def main():
    """ main() program """

    arcade = \
        intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Arcade Cabinet')

    arcade.io.input_value = [0]
    # arcade.emulated_input = [0]

    display, paddle_location, ball_location = create_initial_display(arcade)
    blocks = blocks_remaining(display)

    score = 0
    arcade.memory.bank[0] = 2

    while ball_location != [0, 31]:
        paddle_location, ball_location, score = \
            tracking(arcade, paddle_location, ball_location, score)

        arcade.io.input_value = [paddle_move(paddle_location, ball_location)]
        # arcade.emulated_input = [paddle_move(paddle_location, ball_location)]
        blocks = blocks_remaining(display)

    del arcade, display

    print(f"\nDay 13, Part 1 - number of blocks = {blocks}"
          f"\nDay 13, Part 2 - final score = {score}")


# %% Development Environment
# machine = intcode(aoc.PROGRAMS_AVAILABLE_DICTIONARY, 'Arcade Cabinet')

# machine.emulated_input = 0

# display, paddle_location, ball_location = create_initial_display(machine)
# blocks = blocks_remaining(display)

# score = 0
# machine.memory.bank[0] = 2

# while ball_location != [0, 31]:
#     paddle_location, ball_location, score = \
#         tracking(machine, paddle_location, ball_location, score)

#     machine.emulated_input = paddle_move(paddle_location, ball_location)
#     blocks = blocks_remaining(display)


# %% Production Environment (LOL)

if __name__ == "__main__":
    main()

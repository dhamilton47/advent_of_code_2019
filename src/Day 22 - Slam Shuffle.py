# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:04:20 2019

@author: Dan J Hamilton
"""


import numpy as np

import aoc


# %% Transform the "XXXX" from a string to a list
def transform_program(contents):
    memory = list(contents.split("\n"))
#    memory_length = len(memory)
#    for i in range(memory_length):
#        memory[i] = int(memory[i])

    return memory


def reverse(deck):
    # print(len(deck))
    # # data = deck[:n]
    data = deck[::-1]
    # print(len(data))

    return data


def reverse2(deck, cards):
    """
    Reverse the order of a deck of cards

    deck = the vector of cards
    n =  the number to cut
    """
    # print(len(deck))
    # # data = deck[:n]
    deck = [cards - deck[i] % cards for i in range(cards)]
    # data = deck[::-1]
    # print(len(data))

    return deck


def cut_n(deck, n):
    """
    Cut a deck of cards at the nth card

    deck = the vector of cards
    n =  the number to cut
    """

    return np.append(deck[n:], deck[:n])


def cut_n2(deck, n, cards):
    """
    Cut a deck of cards at the nth card

    deck = the vector of cards
    n =  the number to cut
    cards = number of cards in the deck
    """

    deck = [(deck[i] - n + 1) % cards for i in range(cards)]
    # print(deck[n:])
    # print(deck[:n])
    # data = np.append(deck[n:], deck[:n])

    return deck


def increment_n(deck, n):
    data = np.full((len(deck)), 0)

    index = 0
    for j in range(len(deck)):
        if index >= len(deck):
            index = index - len(deck)
        data[index] = deck[j]
        # print(len(deck))
        # print(len(data))
        index += n

    return data


def parse_shuffles(x):
    shuffles = []
    for i in x:
        if i[:4] == 'cut ':
            shuffles.append((1, int(i[4:])))
        elif i[:20] == 'deal with increment ':
            shuffles.append((2, int(i[20:])))
        else:
            shuffles.append((3, 0))

    return shuffles


def shuffle_rounds(deck, reps, x):
    deck = np.arange(deck)
    count = 0
    shuffles = parse_shuffles(x)

    for i in range(reps):
        for shuffle, n in shuffles:
            if shuffle == 1:
                deck = cut_n(deck, n)
            elif shuffle == 2:
                deck = increment_n(deck, n)
            else:
                deck = reverse(deck)

        if reps > 1:
            print(f"Day 22, Part 2, Round {i} Result = {deck[2019]}")
            if deck[2019] == 2019:
                count += 1

    return deck, count


# %% Development Environment

txtfile = "../data/AoC2019_day_22_input.txt"
contents = aoc.read_program(txtfile)
x = transform_program(contents)
length = len(x)


# a = np.arange(100)
# print(a)
# print(len(a))

number_of_cards_in_deck = 10007
number_of_cards_in_deck1 = 119315717514047

number_of_shuffle_reps = 12009
number_of_shuffle_reps1 = 101741582076661
# Parse shuffles

# deck = np.arange(number_of_cards_in_deck)

# shuffles = parse_shuffles(x)

# for shuffle, n in shuffles:
#     if shuffle == 1:
#         deck = cut_n(deck, n)
#     elif shuffle == 2:
#         deck = increment_n(deck, n)
#     else:
#         deck = reverse(deck)

# print(list(np.where(deck == 2019)[0]))

# final_deck, count = shuffle_rounds(number_of_cards_in_deck, 1, x)
# print(f"Day 22, Part 1 Result = {list(np.where(final_deck == 2019)[0])}")

final_deck, count = shuffle_rounds(number_of_cards_in_deck,
                                   number_of_cards_in_deck - 1, x)
print(f"Day 22, Part 2 Result = {final_deck[2019]}")

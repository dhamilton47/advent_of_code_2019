# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 08:34:47 2019

@author: Dan J Hamilton
"""


# %% Create initial set of possible passwords - results in Day 4 Part 1 answer

start1 = 387638
end1 = 919124
start = 388888
end = 899999


def create_possible_password():
    counter = 0
    password = []
    for i in range(start, end + 1):
        x = str(i)
        if x == '456789':
            continue
        if x[1] >= x[0]:
            if x[2] >= x[1]:
                if x[3] >= x[2]:
                    if x[4] >= x[3]:
                        if x[5] >= x[4]:
                            counter += 1
                            password.append(x)

    return counter, password


# %%

def positions_1_and_0(len_y, y):
    counter = 0
    password = []
    for i in range(len_y - 1, -1, -1):
        x = y[i]
        if x[1] == x[0] and x[2] != x[1]:
            counter += 1
            password.append(x)

    return counter, password


# %%

def positions_2_and_1(len_y, y):
    counter = 0
    password = []
    for i in range(len_y - 1, -1, -1):
        x = y[i]
        if x[1] > x[0] and x[2] == x[1] and x[3] != x[2]:
            counter += 1
            password.append(x)

    return counter, password


# %%

def positions_3_and_2(len_y, y):
    counter = 0
    password = []
    for i in range(len_y - 1, -1, -1):
        x = y[i]
        if x[2] > x[1] and x[3] == x[2] and x[4] != x[3]:
            counter += 1
            password.append(x)

    return counter, password


# %%

def positions_4_and_3(len_y, y):
    counter = 0
    password = []
    for i in range(len_y - 1, -1, -1):
        x = y[i]
        if x[3] > x[2] and x[4] == x[3] and x[5] != x[4]:
            counter += 1
            password.append(x)

    return counter, password


# %%

def positions_5_and_4(len_y, y):
    counter = 0
    password = []
    for i in range(len_y - 1, -1, -1):
        x = y[i]
        if x[4] > x[3] and x[5] == x[4]:
            counter += 1
            password.append(x)

    return counter, password


# %%

def remove_already_accepted(x, y):
    x_copy = x.copy()
    for i in range(len(y)):
        x_copy.remove(y[i])
    return x_copy


counter, password = create_possible_password()

counter1, password1 = positions_1_and_0(counter, password)
passworda = remove_already_accepted(password, password1)

counter2, password2 = positions_2_and_1(counter - counter1, passworda)
passworda = remove_already_accepted(passworda, password2)

counter3, password3 = positions_3_and_2(
        counter - counter1 - counter2, passworda)
passworda = remove_already_accepted(passworda, password3)

counter4, password4 = positions_4_and_3(
        counter - counter1 - counter2 - counter3, passworda)
passworda = remove_already_accepted(passworda, password4)

counter5, password5 = positions_5_and_4(
        counter - counter1 - counter2 - counter3 - counter4, passworda)
passworda = remove_already_accepted(passworda, password5)

print('Number of possible passwords for part 1 =', counter)

print('Number of possible passwords for part 2 =',
      counter1 + counter2 + counter3 + counter4 + counter5)

# %%

password6 = password1 + password2 + password3 + password4 + password5
password6.sort()


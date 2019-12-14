# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:56:26 2019

@author: Dan J Hamilton
"""

# %% Day 8, Part 1

# Need to enter a BIOS password to the Mars Rover
# You  receive an image of the password via the Digital Sending Network (DSN)
# DSN uses a Space Image Format to encode messages.
# You receive the instructions to decode.

# Images are sent as a series of digits that each represent the color of a
# single pixel. The digits fill each row of the image left-to-right, then
# move downward to the next row, filling rows top-to-bottom until every pixel
# of the image is filled.

# RGB or RGBA encoded

# Each image actually consists of a series of identically-sized layers that
# are filled in this way. So, the first digit corresponds to the top-left pixel
# of the first layer, the second digit corresponds to the pixel to the right of
# that on the same layer, and so on until the last digit, which corresponds to
# the bottom-right pixel of the last layer.

# For example, given an image 3 pixels wide and 2 pixels tall, the image data
# 123456789012 corresponds to the following image layers:

# Layer 1: 123
#          456

# Layer 2: 789
#          012

# The image you received is 25 pixels wide and 6 pixels tall.

# To make sure the image wasn't corrupted during transmission, the Elves would
# like you to find the layer that contains the fewest 0 digits. On that layer,
# what is the number of 1 digits multiplied by the number of 2 digits?

# %% Day 8, Part 2

# Decode the images
# The digits indicate the color of the corresponding pixel: 0 is black, 1 is
# white, and 2 is transparent.

# Then, the full image can be found by determining the top visible pixel in
# each position.

# %%


def read_program(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    return contents


def transform_program(contents, count, length):
    layers_index = [0]
    for i in range(count):
        layers_index.append(layers_index[-1] + length)

    image_layers = []
    for i in range(count):
        image_layers.extend([contents[layers_index[i]:layers_index[i + 1]]])

    return image_layers


def image_layer_digit_counter(image, image_length, digit):
    counter = 0
    for i in range(image_length):
        if image[i] == digit:
            counter += 1

    return counter


def lowest_count_index_finder(digits, count, images, target):
    lowest_count = digits
    for i in range(count):
        counter = image_layer_digit_counter(images[i], digits, target)
        if lowest_count > counter:
            lowest_count = counter
            lowest_layer_index = i

    return lowest_count, lowest_layer_index


def preprocess_transmission(x, y, txtfile):
    # load transmission information
    transmission_received = read_program(txtfile)

    # Process transmission dimensions
    digits_per_image_layer = x * y
    transmission_length = len(transmission_received)
    image_count = transmission_length // digits_per_image_layer
    image_count_error = transmission_length % digits_per_image_layer
    if image_count_error:
        raise Exception('Transmission corrupted. Partial final image')

    print('length of transmission = {}, number of images = {}'
          .format(transmission_length, image_count))

    # Find number of image layers
    image_layers = transform_program(transmission_received,
                                     image_count, digits_per_image_layer)

    return digits_per_image_layer, image_count, image_layers


def process_password(x, y, images, image_count):
    password = ['2' * x] * y

    for i in range(x):
        for j in range(y):
            for k in range(image_count):
                pixel = images[k][j][i]

                if pixel != '2':
                    if pixel == '0':
                        password[j] = replace_pixel(password[j], i, ' ')
                    else:
                        password[j] = replace_pixel(password[j], i, '#')
                    break

    return password


def create_images(image_layers, x, y, image_count):
    images = []
    for k in range(image_count):
        image = []
        for j in range(y):
            row = []
            for i in range(x):
                row.append(image_layers[k][j * 25 + i])
            image.append(row)
        images.append(image)

    return images


def replace_pixel(row, index, pixel):
    return row[:index] + pixel + row[index + 1:]


# %%

def day8_part1(x, y, txtfile, target_digit0, target_digit1, target_digit2):
    # Preprocess transmission data
    digits_per_image_layer, image_count, image_layers = \
        preprocess_transmission(x, y, txtfile)

    # Find target digit count for a layer
    count0, lowest_index = lowest_count_index_finder(digits_per_image_layer,
                                                     image_count,
                                                     image_layers,
                                                     target_digit0)

    image = image_layers[lowest_index]

    # find count of '1'
    count1 = image_layer_digit_counter(image,
                                       digits_per_image_layer,
                                       target_digit1)

    # find count of '2'
    count2 = image_layer_digit_counter(image,
                                       digits_per_image_layer,
                                       target_digit2)

    print(('Lowest image index = {}').format(lowest_index))
    print(("{}'s = {}, {}'s = {}, {}'s = {}")
          .format(target_digit0, count0,
                  target_digit1, count1,
                  target_digit2, count2))

    answer = count1 * count2
    print('Day 8, Part 1 = {}'.format(answer))


def day8_part2(x, y, txtfile):
    # Preprocess transmission data
    digits_per_image_layer, image_count, image_layers = \
        preprocess_transmission(x, y, txtfile)

    # Convert image_layers to images
    images = create_images(image_layers, x, y, image_count)

    # Proces images to password
    password = process_password(x, y, images, image_count)

    print('Day 8, Part 2 =')
    for i in range(y):
        print(''.join(password[i]))


# %% Develpment Environment

# # load transmission information
# txtfile = '../data/adventofcode_2019_day_8_input.txt'
# # transmission_received = read_program(txtfile)

# # Process transmission data
# x = 25
# y = 6

# digits_per_image_layer, image_count, image_layers = \
#     preprocess_transmission(x, y, txtfile)

# # Find target digit count for a layer
# target_digit = '0'
# count = image_layer_digit_counter(image_layers[0],
#                                   digits_per_image_layer, target_digit)

# # find image layer with lowest '0' count
# lowest_count = digits_per_image_layer
# for i in range(image_count):
#     count = image_layer_digit_counter(image_layers[i],
#                                       digits_per_image_layer, target_digit)
#     # print("Number of {}'s in image {} = {}".format(target_digit, i, count))
#     if lowest_count > count:
#         lowest_count = count
#         lowest_layer = image_layers[i]
#         lowest_layer_index = i

# # find count of '1'
# target_digit = '1'
# count1 = image_layer_digit_counter(image_layers[lowest_layer_index],
#                                    digits_per_image_layer, target_digit)

# # find count of '2'
# target_digit = '2'
# count2 = image_layer_digit_counter(image_layers[lowest_layer_index],
#                                    digits_per_image_layer, target_digit)

# answer = count1 * count2
# print('Day 8, Part 1 = {}'.format(answer))

# # Convert Image_layers to images

# images = create_images(image_layers, x, y, image_count)

# BIOS_password = ['2' * x] * y

# for i in range(x):
#     for j in range(y):
#         for k in range(image_count):
#             pixel = images[k][j][i]
#             # print('row = {}, column = {}, k= {}, pixel = {}'
#             #       .format(j, i, k, pixel))

#             if pixel != '2':
#                 # print(j, i)
#                 if pixel == '0':
#                     BIOS_password[j] = \
#                         replace_pixel(BIOS_password[j], i, ' ')
#                 else:
#                     BIOS_password[j] = \
#                         replace_pixel(BIOS_password[j], i, '#')
#                 break

# print('Day 8, Part 2 =')
# for i in range(y):
#     print(''.join(BIOS_password[i]))


# %% Production Environment

txtfile = '../data/adventofcode_2019_day_8_input.txt'

day8_part1(25, 6, txtfile, '0', '1', '2')
print()
day8_part2(25, 6, txtfile)

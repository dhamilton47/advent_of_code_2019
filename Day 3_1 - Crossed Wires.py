# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:10:33 2019

@author: danha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()
# %matplotlib inline

x_text = "./data/adventofcode_2019_day_3_wire_1_input.txt"
y_text = "./data/adventofcode_2019_day_3_wire_2_input.txt"


# %% Read in the wire directives
def read_text1(txtfile):
    f = open(txtfile, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    contents_split = pd.DataFrame(contents.split(','),
                                  columns=['move'], index=None)

    return contents_split, len(contents_split)


# %% Parse the line directives into direction and distance
def parse_movements(x, y):
    direction = []
    distance = []

    for i in range(y):
        direction.append(x.loc[i].move[0])
        distance.append(int(x.loc[i].move[1:]))

    x['direction'] = direction
    x['distance'] = distance
    return x


# %% Determine the end points of a line segment
def point1(x, y):
    col_x = [0]
    col_y = [0]

    for i in range(y):
        if x.direction[i] == 'L':
            col_x.append(col_x[i] - x.distance[i])
            col_y.append(col_y[i])
        elif x.direction[i] == 'R':
            col_x.append(col_x[i] + x.distance[i])
            col_y.append(col_y[i])
        elif x.direction[i] == 'U':
            col_x.append(col_x[i])
            col_y.append(col_y[i] + x.distance[i])
        else:
            col_x.append(col_x[i])
            col_y.append(col_y[i] - x.distance[i])

    x['x1'] = col_x[:-1]
    x['y1'] = col_y[:-1]
    x['x2'] = col_x[1:]
    x['y2'] = col_y[1:]
    return x


# %% Read in the line directives, parse them and determine the end points
def preprocess_data1(text):
    codes, len_codes = read_text1(text)
    codes = parse_movements(codes, len_codes)
    codes = point1(codes, len_codes)
    return codes, len_codes


# %% Create discrete, integer points (x, y) for a set of lines segments
def plot_points(x, y):
    plot_points_x = []
    plot_points_y = []
    point = []

    for i in range(y):
        seg_x = x.x2[i] - x.x1[i]
        seg_y = x.y2[i] - x.y1[i]

        sign_x = 1 if seg_x >= 0 else -1
        sign_y = 1 if seg_y >= 0 else -1

        tempx = plot_points_x[-1] if plot_points_x else 0
        tempy = plot_points_y[-1] if plot_points_y else 0

        if seg_x == 0:
            for i in range(1, 1 + abs(seg_y)):
                plot_points_x.append(tempx)
                plot_points_y.append(tempy + i * sign_y)
                point.append([tempx, tempy + i * sign_y])

        if seg_y == 0:
            for i in range(1, 1 + abs(seg_x)):
                plot_points_x.append(tempx + i * sign_x)
                plot_points_y.append(tempy)
                point.append([tempx + i * sign_x, tempy])

    plot_point = pd.DataFrame(plot_points_x, index=None, columns=['x'])
    plot_point['y'] = plot_points_y
    plot_point['pt'] = point

    return plot_point


# %% Determine all of the intersections of the two wires
def intersections(lst1, lst2):
    tup1 = map(tuple, list(plot_x.pt))
    tup2 = map(tuple, list(plot_y.pt))
    return list(map(list, set(tup1).intersection(tup2)))


# %% Determine the Manhatten distance between two points
def manhattan(pt1, pt2=[0, 0]):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


# %% Determine the minimum distance

def minimum_distance(x):
    distances = []

    for i in x:
        distances.append(manhattan(i))

    distances.sort()

    return 'Day 3 - Part 1 - Minimum distance is = ' + str(distances[0])


# %%
codes_x1, len_codes_x = preprocess_data1(x_text)
codes_y1, len_codes_y = preprocess_data1(y_text)
plot_x = plot_points(codes_x1, len_codes_x)
plot_y = plot_points(codes_y1, len_codes_y)
intersection = intersections(plot_x.pt, plot_y.pt)
print(minimum_distance(intersection))

# %% Plot the results

# Set the width and height of the figure
plt.figure(figsize=(12, 6))

plt.plot(codes_x1['x1'], codes_x1['y1'], label='Wire 1')
plt.plot(codes_y1['x1'], codes_y1['y1'][:], label='Wire 2')
plt.plot([0, intersection[13][0]], [0, intersection[13][1]], label='Wire 1')

# Add title
plt.title("Crossed Wires")

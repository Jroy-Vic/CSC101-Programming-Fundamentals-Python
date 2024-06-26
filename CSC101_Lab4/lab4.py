# Roy Vicerra - Lab 4

import data
import math

# Write your functions for each part in the space below.

# Part 1
# Purpose: take in a two-dimensional list and output the first element
#          of each sublist.
# Input: list[list[int]]
# Output: list[int]
# Example Input: [[1, 2], [], [3, 4]]
# Example of Given Output: [1,3]
def first_element(list_in: list[list[int]]):
    answer_list = []
    for x in list_in:
        if len(x) > 0:
            first_item = x[0]
            answer_list.append(first_item)
    return answer_list
  # return [l[0] for l in list_in if len(l) > 0]


# Part 2
# Purpose: create a Point class to take in a list of data.Points to output a
#          list of the x-coordinates of each data.Point.
# Input: list[data.Point]
# Output: list[int]
# Example Input: [data.Point(1,2), data.Point(3,4)]
# Example of Given Output: [1, 3]

def x_coordinates(list_in: list[data.Point]):
    x_coords = []
    for p in list_in:
        x_coords.append(p.x)
    return x_coords


# Part 3
# Purpose: this function takes in a list of data.Points as input and
#          returns a list of data.Points whose x and y coordinates are positive.
# Input: list[data.Point]
# Output: list[data.Point]
# Example Input: [data.Point(-3,5), data.Point(4,9), data.Point(-2,8)]
# Example of Given Output: [data.Point(4,9)]

def are_in_positive_quadrant(list_in: list[data.Point]):
    quad1_Points = []
    for p in list_in:
        if p.x > 0 and p.y > 0:
            quad1_Points.append(p)
    return quad1_Points


# Part 4
# Purpose: this function takes two data.Point values as inputs and
#          returns the Euclidean distance between the two points as a float.
# Input: data.Point, data.Point
# Output: float
# Example Input: data.Point(1,2), data.Point(2,3)
# Example of Given Output: 1.414

def distance(p1: data.Point, p2: data.Point) -> float:
    x_difference = p1.x - p2.x
    y_difference = p1.y - p2.y
    x_squared = x_difference * x_difference
    y_squared = y_difference * y_difference
    distance = math.sqrt(x_squared + y_squared)
    distance = round(distance, 3)
    return distance


# Part 5
# Purpose: this function takes two data.Point values as inputs and
#          returns the Manhattan distance between the two points as a float.
# Input: data.Point, data.Point
# Output: float
# Example Input: data.Point(1,2), data.Point(2,3)
# Example of Given Output: 2

def manhattan_distance(p1: data.Point,  p2: data.Point) -> float:
    x_difference = p1.x - p2.x
    y_difference = p1.y - p2.y
    if x_difference < 0:
        x_difference = x_difference * -1
    if y_difference < 0:
        y_difference = y_difference * -1
    manhattan_distance = x_difference + y_difference
    manhattan_distance = round(manhattan_distance, 3)
    return manhattan_distance


# Part 6
# Purpose: this function takes a list of data.Point values and
#          returns a list of floats representing the distances of each Point from the origin (0,0).
# Input: list[data.Point]
# Output: list[float] (using Distance Formula)
# Example Input: [data.Point(0,0), data.Point(1,1), data.Point(2,2)]
# Example of Given Output: [0, 1.414, 2.828]

def distance_all(list_p: list[data.Point]):
    list_dist = []
    for p in list_p:
        x_difference = p.x - 0
        y_difference = p.y - 0
        x_squared = x_difference * x_difference
        y_squared = y_difference * y_difference
        distance = math.sqrt(x_squared + y_squared)
        distance = round(distance, 3)
        list_dist.append(distance)
    return list_dist
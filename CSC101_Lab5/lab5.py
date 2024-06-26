import data
import math

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.

# Part 2
   # The function for Part 2 should be within the class in data.py.

# Part 3
# Purpose: this function takes two data.Time values and returns
#          a new data.Time value that represents the sum of the two input times.
# Input: data.Time, data.Time
# Output: data.Time
# Example Input: data.Time(3, 14, 15), data.Time(1, 9, 27)
# Example of Given Output: data.Time(4, 23, 42)

def time_add(time_1: data.Time, time_2: data.Time) -> data.Time:
    total_hours = time_1.hour + time_2.hour
    total_minutes = time_1.minute + time_2.minute
    total_seconds = time_1.second + time_2.second
    if total_seconds >= 60:
        add_minutes = total_seconds // 60
        excess_seconds = total_seconds % 60
        total_seconds = excess_seconds
        total_minutes = total_minutes + add_minutes
    if total_minutes >= 60:
        add_hours = total_minutes // 60
        excess_minutes = total_minutes % 60
        total_minutes = excess_minutes
        total_hours = total_hours + add_hours
    total_time = data.Time(total_hours, total_minutes, total_seconds)
    return total_time


# Part 4
# Purpose: this function takes a list of float values and returns
#          True if and only if its elements are in descending order.
# Input: list[float]
# Output: bool
# Example Input: [3.14, 2.799, 1.141]
# Example of Given Output: True

def is_descending(list_in: list[float]) -> bool:
    for n in range(len(list_in)):
        if list_in[n] <= list_in[(n + 1)]:
            return False
    return True


# Part 5
# Purpose: this function takes one list of int values and two other separate
#          int values, which represent two indexes; it returns the index
#          of the largest value in the input list that is within
#          the domain of the two inputted indexes; if the lower index is greater
#          than the upper index, it will return None.
# Input: list[int], int, int
# Output: int
# Example Input: [42, 12, 35, 36, 89], 1, 3
# Example of Given Output: 3

def largest_between(list_in: list[int], lower: int, upper: int) -> int:
    if lower > upper:
        return None
    else:
        index = lower
        for idx in range(len(list_in)):
            if idx >= lower and idx < upper:
                if list_in[idx] > list_in[idx+1]:
                    index = idx
            elif idx == upper:
                if list_in[idx] > list_in[index]:
                    index = upper
        return index


# Part 6
# Purpose: this function takes a list of data.Point values and returns
#          the index of the data.Point value that is furthest from the origin;
#          if the input list is empty, the function returns None.
# Input: list[data.Point]
# Output: int
# Example Input: [data.Point(4,2), data.Point(0,6), data.Point(9,3)]
# Example of Given Output: 2

def furthest_from_origin(list_in: list[data.Point]) -> int:
    if len(list_in) > 0:
        value = 0
        for idx in range(len(list_in)):
            if idx < (len(list_in) - 1):
                pnt = list_in[idx]
                pnt_comp = list_in[idx + 1]
                x_diff = pnt.x ** 2
                y_diff = pnt.y ** 2
                dist = math.sqrt(x_diff + y_diff)
                x_diff_comp = pnt_comp.x ** 2
                y_diff_comp = pnt_comp.y ** 2
                dist_comp = math.sqrt(x_diff_comp + y_diff_comp)
                if dist > dist_comp:
                    value = idx
            elif idx == (len(list_in) - 1):
                pnt = list_in[idx]
                pnt_comp = list_in[value]
                x_diff = pnt.x ** 2
                y_diff = pnt.y ** 2
                dist = math.sqrt(x_diff + y_diff)
                x_diff_comp = pnt_comp.x ** 2
                y_diff_comp = pnt_comp.y ** 2
                dist_comp = math.sqrt(x_diff_comp + y_diff_comp)
                if dist > dist_comp:
                    value = idx
        return value
    else:
        return None








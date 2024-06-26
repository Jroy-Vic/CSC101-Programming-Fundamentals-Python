# Roy Vicerra - Programming Assignment 1

import data
import math

# Write your functions for each part in the space below.

# Part 1
# Purpose: this function takes in a string and returns an int value
#          representing the number of vowels (a,e,i,o,u) within the string.
# Input: str
# Output: int
# Example Input: "bananas"
# Example of Given Output: 3

def vowel_count(str_in: str) -> int:
    vowels = 0
    for letter in str_in:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowels = vowels + 1
        if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
            vowels = vowels + 1
    return vowels


# Part 2
# Purpose: this function takes in a list of lists of integer values
#          to return a list of its elements that are only of length 2.
# Input: list[list[int]]
# Output: list[list[int]]
# Example Input: [[0, 2, 3], [1, 2], [], [0, 0], [1, 0, 2], [5, 5]]
# Example of Given Output: [[1, 2], [0, 0], [5, 5]]

def short_lists(list_in: list[list[int]]) -> list[list[int]]:
    list_out = []
    for list in list_in:
        if len(list) == 2:
            list_out.append(list)
    return list_out


# Part 3
# Purpose: this function takes in a list of lists of int values and returns
#          a new list composed of the same elements in the same order; however,
#          any nested list that is of length 2 must be rearranged so that its
#          elements are in ascending order.
# Input: list[list[int]]
# Output: list[list[int]]
# Example Input: [[0,0,0], [1,0], [4,2], [5,5,5]]
# Example of Given Output: [[0,0,0], [0,1], [2,4], [5,5,5]]

def ascending_pairs(list_in: list[list[int]]) -> list[list[int]]:
    list_out = []
    for nest in list_in:
        if len(nest) == 2:
            if nest[0] > nest[1]:
                nest = [nest[1], nest[0]]
        list_out.append(nest)
    return list_out


# Part 4
# Purpose: this function takes in two data.Price values and returns
#          their sum as a new data.Price value, however the number of cents
#          must not exceed 99.
# Input: data.Price, data.Price
# Output: data.Price
# Example Input: data.Price(5, 60), data.Price(4,40)
# Example of Given Output: data.Price(10,0)

def add_prices(price_1: data.Price, price_2: data.Price) -> data.Price:
    dollars = price_1.dollars + price_2.dollars
    cents = price_1.cents + price_2.cents
    if cents >= 100:
        dollars = dollars + (cents // 100)
        cents = cents % 100
    price_out = data.Price(dollars, cents)
    return price_out


# Part 5
# Purpose: this function takes in a data.Rectangle value and
#          returns the area of the provided rectangle
#          (first input = top-left corner, second input = bottom-right corner)
# Input: data.Rectangle(data.Point, data.Point)
# Output: float
# Example Input: data.Rectangle(data.Point(3,5), data.Point(7,2))
# Example of Given Output: 12

def rectangle_area(rectangle_in: data.Rectangle) -> float:
    p1 = rectangle_in.top_left
    p2 = rectangle_in.bottom_right
    length = p1.y - p2.y
    width = p2.x - p1.x
    area = length * width
    return area


# Part 6
# Purpose: this function takes into two types of inputs, one
#          string value (representing the name of an author) and
#          the other a list of data.Book values, and returns a
#          list of data.Book values that are written by the given author.
# Input: str, list[Book]
# Output: list[Book]
# Example Input: "Dr. Seuss", [data.Book(["Dr. Seuss","Fitzgerald"],"Green Eggs")]
# Example of Given Output: "Green Eggs"

def books_by_author(author: str, titles: list[data.Book]) -> list[data.Book]:
    fav_books = []
    for books in titles:
        for authors in books.authors:
            if authors == author:
                fav_books.append(books.title)
    return fav_books

# Part 7
# Purpose: this function takes in a data.Rectangle value and returns
#          a data.Circle value that represents the smallest circle
#          that encloses the rectangle.
# Input: data.Rectangle
# Output: data.Circle
# Example Input: data.Rectangle(data.Point(0,5), data.Point(5,0))
# Example of Given Output: data.Circle(data.Point(2.5,2.5), 3.536)

def circle_bound(rectangle_in: data.Rectangle) -> data.Circle:
    p_top_left = rectangle_in.top_left
    p_bottom_right = rectangle_in.bottom_right
    y_difference = (p_top_left.y - p_bottom_right.y) / 2
    x_difference = (p_bottom_right.x - p_top_left.x) / 2

    x_center = p_bottom_right.x - x_difference
    y_center = p_top_left.y - y_difference
    center = data.Point(x_center, y_center)

    distance_y = p_top_left.y - center.y
    distance_x = center.x - p_top_left.x
    dy_squared = distance_y * distance_y
    dx_squared = distance_x * distance_x
    radius = math.sqrt(dy_squared + dx_squared)
    radius = round(radius, 3)

    circle_out = data.Circle(center, radius)
    return circle_out


# Part 8
# Purpose: this function takes in a list of data.Employee values
#          and returns a list of string values of the names of employees
#          that are being paid less than the average pay of all listed employees.
# Input: list[data.Employee]
# Output: list[str]
# Example Input: [data.Employee("Roy", 16), data.Employee("Kevin", 20), data.Employee("Bryan", 23), data.Employee("Wilson", 22)]
# Example of Given Output: ["Roy", "Kevin"]

def below_pay_average(employee_list: list[data.Employee]) -> list[str]:
    below_avg = []
    total = 0
    if len(employee_list) > 0:
        for employee in employee_list:
            total = total + employee.pay_rate
        average_pay_rate = total / len(employee_list)

        for employee in employee_list:
            if employee.pay_rate < average_pay_rate:
                below_avg.append(employee.name)
    return below_avg


# Roy Vicerra - Programming Assignment 1

import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    def test_vowel_count_1(self):
        input = "apples"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input = "OraNgEs And SNAKeS"
        result = hw1.vowel_count(input)
        expected = 6
        self.assertEqual(expected, result)

    # Part 2

    def test_short_lists_1(self):
        input = [[0, 0, 1], [2, 2], [3, 3], [4, 4, 4]]
        result = hw1.short_lists(input)
        expected = [[2, 2], [3, 3]]
        self.assertEqual(expected, result)

    def test_short_lists_2(self):
        input = [[3, 3], [], [5, 5, 5]]
        result = hw1.short_lists(input)
        expected = [[3, 3]]
        self.assertEqual(expected, result)


    # Part 3

    def test_ascending_pairs_1(self):
        input = [[1,1,1], [0,1], [4,2], [6,2], [0,0,0]]
        result = hw1.ascending_pairs(input)
        expected = [[1,1,1], [0,1], [2,4], [2,6], [0,0,0]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        input = [[1, 2, 3], [], [-4, 2], [2], [1, 0]]
        result = hw1.ascending_pairs(input)
        expected = [[1, 2, 3], [], [-4, 2], [2], [0, 1]]
        self.assertEqual(expected, result)


    # Part 4

    def test_add_prices_1(self):
        input_1 = data.Price(5, 69)
        input_2 = data.Price(3, 2)
        result = hw1.add_prices(input_1, input_2)
        expected = data.Price(8, 71)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        input_1 = data.Price(5, 360)
        input_2 = data.Price(3, 43)
        result = hw1.add_prices(input_1, input_2)
        expected = data.Price(12, 3)
        self.assertEqual(expected, result)


    # Part 5

    def test_rectangle_area_1(self):
        input = data.Rectangle(data.Point(0,5), data.Point(10,0))
        result = hw1.rectangle_area(input)
        expected = 50
        self.assertEqual(expected, result)
    def test_rectangle_area_2(self):
        input = data.Rectangle(data.Point(-3, 5.5), data.Point(10.67, 2))
        result = hw1.rectangle_area(input)
        expected = 47.845
        self.assertEqual(expected, result)


    # Part 6

    def test_books_by_author_1(self):
        input_1 = "Neil Gaiman"
        input_2 = [data.Book(["Neil Gaiman", "Terry Pratchett"], "Good Omens"), data.Book(["Lisa Lutz", "David Hayward"], "Heads You Lose")]
        result = hw1.books_by_author(input_1, input_2)
        expected = ["Good Omens"]
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        input_1 = "Stephen King"
        input_2 = [data.Book(["Emily Schultz", "Stephen King"], "Joyland"), data.Book(["Liam Callanan", "David Mitchell"], "The Cloud Atlas"), data.Book(["Stephen King"], "It")]
        result = hw1.books_by_author(input_1, input_2)
        expected = ["Joyland", "It"]
        self.assertEqual(expected, result)


    # Part 7
    def test_circle_bound_1(self):
        input = data.Rectangle(data.Point(0,5), data.Point(5,0))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(2.5,2.5), 3.536)
        self.assertEqual(expected, result)

    def test_circle_bound_2(self):
        input = data.Rectangle(data.Point(3,7.5), data.Point(5,-3))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(4,2.25), 5.344)
        self.assertEqual(expected, result)


    # Part 8

    def test_below_pay_average_1(self):
        input = [data.Employee("Roy", 16), data.Employee("Kevin", 20), data.Employee("Bryan", 23), data.Employee("Wilson", 22)]
        result = hw1.below_pay_average(input)
        expected = ["Roy", "Kevin"]
        self.assertEqual(expected, result)

    def test_below_pay_average_2(self):
        input = []
        result = hw1.below_pay_average(input)
        expected = []
        self.assertEqual(expected, result)


%
if __name__ == '__main__':
    unittest.main()

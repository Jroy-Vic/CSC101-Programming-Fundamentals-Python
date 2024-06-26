# Roy Vicerra - Lab 4

import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[1,2], [], [3,4]]
        result = lab4.first_element(input)
        expected = [1,3]
        self.assertEqual(expected, result)


    # Part 2

    def test_x_coordinates_1(self):
        input = [data.Point(1,2), data.Point(3,4)]
        result = lab4.x_coordinates(input)
        expected = [1,3]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = [data.Point(-16,0), data.Point(0,0), data.Point(-5.35,-2.79)]
        result = lab4.x_coordinates(input)
        expected = [-16,0,-5.35]
        self.assertEqual(expected, result)

    # Part 3

    def test_are_in_positive_quadrant_1(self):
        input = [data.Point(-3,5), data.Point(4,9), data.Point(-2,8), data.Point(3,-4), data.Point(2,2)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(4,9), data.Point(2,2)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        input = [data.Point(-3,-5), data.Point(1.25,2.59), data.Point(0,0)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(1.25,2.59)]
        self.assertEqual(expected, result)


    # Part 4

    def test_distance_1(self):
        input_1 = data.Point(2,3)
        input_2 = data.Point(4,5)
        result = lab4.distance(input_1,input_2)
        expected = 2.828
        self.assertEqual(expected, result)
    def test_distance_2(self):
        input_1 = data.Point(-2,-3)
        input_2 = data.Point(-4,-5)
        result = lab4.distance(input_1,input_2)
        expected = 2.828
        self.assertEqual(expected, result)


    # Part 5

    def test_manhattan_distance_1(self):
        input_1 = data.Point(2,3)
        input_2 = data.Point(4,5)
        result = lab4.manhattan_distance(input_1,input_2)
        expected = 4
        self.assertEqual(expected, result)
    def test_manhattan_distance_2(self):
        input_1 = data.Point(0.5,-3)
        input_2 = data.Point(-4,5)
        result = lab4.manhattan_distance(input_1,input_2)
        expected = 12.5
        self.assertEqual(expected, result)


    # Part 6

    def test_distance_all_1(self):
        input = [data.Point(1,2), data.Point(3,4), data.Point(5,6)]
        result = lab4.distance_all(input)
        expected = [2.236, 5, 7.810]
        self.assertEqual(expected, result)
    def test_distance_all_2(self):
        input = [data.Point(-1, 2), data.Point(3, -4), data.Point(5, 0)]
        result = lab4.distance_all(input)
        expected = [2.236, 5, 5]
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()

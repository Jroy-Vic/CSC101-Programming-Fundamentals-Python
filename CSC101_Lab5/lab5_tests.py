import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3

    def test_time_add_1(self):
        input_1 = data.Time(3, 14, 15)
        input_2 = data.Time(1, 9, 27)
        result = lab5.time_add(input_1, input_2)
        expected = data.Time(4, 23, 42)
        self.assertEqual(expected, result)

    def test_time_add_2(self):
        input_1 = data.Time(3, 14, 15)
        input_2 = data.Time(1, 58, 48)
        result = lab5.time_add(input_1, input_2)
        expected = data.Time(5, 13, 3)
        self.assertEqual(expected, result)


    # Part 4

    def test_is_descending_1(self):
        input = [1.141, 2.779, 3.14]
        result = lab5.is_descending(input)
        expected = True
        self.assertNotEqual(expected, result)

    def test_is_descending_2(self):
        input = [5.34, 3.234, 5.234, 1.2321, 0.532, 5.3234]
        result = lab5.is_descending(input)
        expected = False
        self.assertEqual(expected, result)

    # Part 5

    def test_largest_between_1(self):
        input_1 = [42, 12, 35, 36, 89]
        input_2 = 1
        input_3 = 3
        result = lab5.largest_between(input_1, input_2, input_3)
        expected = 3
        self.assertEqual(expected, result)

    def test_largest_between_2(self):
        input_1 = [19, 21, 14, -20, 29, 32, -13, 17, 23]
        input_2 = 2
        input_3 = 7
        result = lab5.largest_between(input_1, input_2, input_3)
        expected = 5
        self.assertEqual(expected, result)

    def test_largest_between_3(self):
        input_1 = [19, 21, 14, -20, 29, 32, -13, 17, 23]
        input_2 = 7
        input_3 = 2
        result = lab5.largest_between(input_1, input_2, input_3)
        expected = None
        self.assertEqual(expected, result)

    # Part 6

    def test_furthest_from_origin_1(self):
        input = [data.Point(4,2), data.Point(0,6), data.Point(9,3)]
        result = lab5.furthest_from_origin(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_furthest_from_origin_2(self):
        input = [data.Point(0,0), data.Point(-5,-9), data.Point(9,3)]
        result = lab5.furthest_from_origin(input)
        expected = 1
        self.assertEqual(expected, result)

    def test_furthest_from_origin_3(self):
        input = []
        result = lab5.furthest_from_origin(input)
        expected = None
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()

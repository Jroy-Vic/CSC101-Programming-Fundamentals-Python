import convert
import unittest

# Roy Vicerra

class TestCases(unittest.TestCase):

    # Task 1

    def test_str_to_float_1(self):
        input = "hello"
        result = convert.str_to_float(input)
        expected = None
        self.assertEqual(expected, result)

    def test_str_to_float_2(self):
        input = "123.45"
        result = convert.str_to_float(input)
        expected = 123.45
        self.assertEqual(expected, result)
import group
import unittest

# Roy Vicerra

class TestCases(unittest.TestCase):

    # Task 1

    def test_groups_of_3_1(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = group.groups_of_3(input)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(expected, result)

    def test_groups_of_3_2(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8]
        result = group.groups_of_3(input)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        self.assertEqual(expected, result)

    def test_groups_of_3_3(self):
        input = [1, 2, 3, 4, 5, 6, 7]
        result = group.groups_of_3(input)
        expected = [[1, 2, 3], [4, 5, 6], [7]]
        self.assertEqual(expected, result)

    def test_groups_of_3_4(self):
        input = [1, 2, 3, 4, 5, 6]
        result = group.groups_of_3(input)
        expected = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(expected, result)
# Roy Vicerra - Lab3 Task 3

import unittest
import functions

class Lab3TestCases(unittest.TestCase):
    def test_double_one(self):  # Although the function passed the first time, this does not mean that it worked properly.
                                # It just so happens that 2 doubled is equal to 2 squared.
                                # To sufficiently test this function, you would need at least 2 or more tests to ensure
                                # that it is working properly. As we saw, plugging in 3 into the function did not work.
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)

    def test_double_two(self):
        result = functions.double(3)
        expected = 6
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

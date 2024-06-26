import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    def test_create_rectangle_1(self):
        input_1 = data.Point(2,2)
        input_2 = data.Point(10,10)
        result = hw2.create_rectangle(input_1, input_2)
        expected = data.Rectangle(data.Point(2,10), data.Point(10,2))
        self.assertEqual(expected, result)

    def test_create_rectangle_1(self):
        input_1 = data.Point(-3,13)
        input_2 = data.Point(-8,7)
        result = hw2.create_rectangle(input_1, input_2)
        expected = data.Rectangle(data.Point(-8,13), data.Point(-3,7))
        self.assertEqual(expected, result)

    def test_create_rectangle_3(self):
        input_1 = data.Point(-3,13)
        input_2 = data.Point(-3,7)
        result = hw2.create_rectangle(input_1, input_2)
        expected = data.Rectangle(data.Point(-3,13), data.Point(-3,7))
        self.assertEqual(expected, result)


    # Part 2

    def test_shorter_duration_than_1(self):
        input_1 = data.Duration(5,25)
        input_2 = data.Duration(8,45)
        result = hw2.shorter_duration_than(input_1, input_2)
        expected = True
        self.assertEqual(expected, result)

    def test_shorter_duration_than_2(self):
        input_1 = data.Duration(10,30)
        input_2 = data.Duration(10,15)
        result = hw2.shorter_duration_than(input_1, input_2)
        expected = False
        self.assertEqual(expected, result)

    # Part 3

    def test_songs_shorter_than_1(self):
        input_1 = [data.Song("grentperez", "About Love", data.Duration(4,18)), data.Song("Luna Li", "2516", data.Duration(1,8)), data.Song("keshi", "SOMEBODY", data.Duration(2,44))]
        input_2 = data.Duration(3,0)
        result = hw2.songs_shorter_than(input_1, input_2)
        expected = [data.Song("Luna Li", "2516", data.Duration(1,8)), data.Song("keshi", "SOMEBODY", data.Duration(2,44))]
        self.assertEqual(expected, result)

    def test_songs_shorter_than_2(self):
        input_1 = [data.Song("grentperez", "About Love", data.Duration(4,18)), data.Song("Luna Li", "2516", data.Duration(1,8)), data.Song("keshi", "SOMEBODY", data.Duration(2,44))]
        input_2 = data.Duration(1,0)
        result = hw2.songs_shorter_than(input_1, input_2)
        expected = []
        self.assertEqual(expected, result)


    # Part 4

    def test_running_time_1(self):
        input_1 = [data.Song("grentperez", "About Love", data.Duration(4,18)), data.Song("Luna Li", "2516", data.Duration(1,8)), data.Song("keshi", "SOMEBODY", data.Duration(2,44))]
        input_2 = [0, 1, 2, 0, 1, 2]
        result = hw2.running_time(input_1, input_2)
        expected = data.Duration(16, 20)
        self.assertEqual(expected, result)

    def test_running_time_2(self):
        input_1 = [data.Song("grentperez", "About Love", data.Duration(4,18)), data.Song("Luna Li", "2516", data.Duration(1,8)), data.Song("keshi", "SOMEBODY", data.Duration(2,44))]
        input_2 = [0, 2, 4, -1, 2]
        result = hw2.running_time(input_1, input_2)
        expected = data.Duration(9, 46)
        self.assertEqual(expected, result)

    # Part 5

    def test_validate_route_1(self):
        input_1 = [['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
        input_2 = ['san luis obispo', 'santa margarita', 'san luis obispo', 'pismo beach', 'san luis obispo', 'santa margarita', 'atascadero', 'creston']
        result = hw2.validate_route(input_1, input_2)
        expected = True
        self.assertEqual(expected, result)

    def test_validate_route_2(self):
        input_1 = [['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
        input_2 = ['san luis obispo', 'atascadero']
        result = hw2.validate_route(input_1, input_2)
        expected = False
        self.assertEqual(expected, result)

    def test_validate_route_3(self):
        input_1 = [['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
        input_2 = ['san luis obispo']
        result = hw2.validate_route(input_1, input_2)
        expected = True
        self.assertEqual(expected, result)

    def test_validate_route_4(self):
        input_1 = [['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
        input_2 = []
        result = hw2.validate_route(input_1, input_2)
        expected = True
        self.assertEqual(expected, result)


    # Part 6

    def test_longest_repetition_1(self):
        input = [1, 1, 2, 2, 1, 1, 1, 3]
        result = hw2.longest_repetition(input)
        expected = 4
        self.assertEqual(expected, result)

    def test_longest_repetition_2(self):
        input = [1, 1, 2, 2, 2, 1, 1, 1]
        result = hw2.longest_repetition(input)
        expected = 5
        self.assertEqual(expected, result)

    def test_longest_repetition_3(self):
        input = [0, 1, 2, 1, 2, 3, 5, 4]
        result = hw2.longest_repetition(input)
        expected = None
        self.assertEqual(expected, result)

    def test_longest_repetition_4(self):
        input = [0, 1, 2, 1, 2, 2, 5, 4]
        result = hw2.longest_repetition(input)
        expected = 4
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    def test_selection_sort_books_1(self):
        input = [data.Book("Harper Lee", "To Kill A Mocking Bird"), data.Book("J.D. Salinger", "The Catcher in the Rye"), data.Book("Ray Bradbury", "Fahrenheit 451")]
        expected = [data.Book("Ray Bradbury", "Fahrenheit 451"), data.Book("J.D. Salinger", "The Catcher in the Rye"), data.Book("Harper Lee", "To Kill A Mocking Bird")]
        lab6.selection_sort_books(input)
        self.assertEqual(expected, input)

    def test_selection_sort_books_2(self):
        input = [data.Book("Harper Lee", "To Kill A Mocking Bird"), data.Book("J.D. Salinger", "The Catcher in the Rye"), data.Book("Ray Bradbury", "Fahrenheit 451"), data.Book("John Steinback", "Of Mice and Men"), data.Book("Aldous Huxley", "Brave New World")]
        expected = [data.Book("Aldous Huxley", "Brave New World"), data.Book("Ray Bradbury", "Fahrenheit 451"), data.Book("John Steinback", "Of Mice and Men"), data.Book("J.D. Salinger", "The Catcher in the Rye"), data.Book("Harper Lee", "To Kill A Mocking Bird")]
        lab6.selection_sort_books(input)
        self.assertEqual(expected, input)

    def test_selection_sort_books_3(self):
        input = []
        expected = []
        lab6.selection_sort_books(input)
        self.assertEqual(expected, input)

    # Part 2

    def test_swap_case_1(self):
        input = "BaNaNa"
        expected = "bAnAnA"
        result = lab6.swap_case(input)
        self.assertEqual(expected,result)

    def test_swap_case_2(self):
        input = "BaNaNaS aRe VerY GooD"
        expected = "bAnAnAs ArE vERy gOOd"
        result = lab6.swap_case(input)
        self.assertEqual(expected,result)

    # Part 3

    def test_str_translate_1(self):
        input_1 = "abcdcba"
        input_2 = 'a'
        input_3 = 'x'
        expected = "xbcdcbx"
        result = lab6.str_translate(input_1, input_2, input_3)
        self.assertEqual(expected,result)

    def test_str_translate_2(self):
        input_1 = "HelLo World"
        input_2 = 'l'
        input_3 = 'x'
        expected = "Hexxo Worxd"
        result = lab6.str_translate(input_1, input_2, input_3)
        self.assertEqual(expected,result)

    # Part 4
    def test_histogram_1(self):
        input = "This is how this works"
        expected = {"This": 2, "Is": 1, "How": 1, "Works": 1}
        result = lab6.histogram(input)
        self.assertEqual(expected, result)

    def test_histogram_2(self):
        input = "Fear leads to anger; anger leads to hatred; hatred leads to conflict; conflict leads to suffering"
        expected = {'Anger': 2, 'Conflict': 2, 'Fear': 1, 'Hatred': 2, 'Leads': 4, 'Suffering': 1, 'To': 4}
        result = lab6.histogram(input)
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()

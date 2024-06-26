import data
import unittest


class TestCases(unittest.TestCase):
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(point.x, 7)
        self.assertAlmostEqual(point.y, 20)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(point.x, 4)
        self.assertAlmostEqual(point.y, 19)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual(repr(point), 'Point(5, 75)')


if __name__ == '__main__':
    unittest.main()

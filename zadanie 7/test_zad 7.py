import unittest
from zad7 import calculate_distance

class TestCalculateDistance(unittest.TestCase):

    def test_distance_positive_coordinates(self):
        self.assertAlmostEqual(calculate_distance(0, 0, 3, 4), 5.0)

    def test_distance_negative_coordinates(self):
        self.assertAlmostEqual(calculate_distance(-1, -2, -4, -6), 5.0)

    def test_distance_mixed_coordinates(self):
        import math
        self.assertAlmostEqual(calculate_distance(-1, 2, 2, -2), math.sqrt(20))

if __name__ == "__main__":
    unittest.main()

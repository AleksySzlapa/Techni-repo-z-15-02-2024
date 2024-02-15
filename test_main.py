from unittest import TestCase
import unittest

class Test(unittest.TestCase):
    def test_non_existing_file(self):
        self.fail()

    def test_empty_file(self):
        self.fail()

    def test_all_positives(self):
        self.fail()

    def test_all_negatives(self):
        self.fail()

    def test_mix(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()

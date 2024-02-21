from unittest import TestCase
import unittest
from main import file_sumer
class Test(unittest.TestCase):

    def test_non_existing_file(self):
        file = 'thios path doesnt exist'
        with self.assertRaises(FileNotFoundError):
            result = file_sumer(file)


    def test_empty_file(self):
        file = 'test2.txt'
        expected = 0
        result = file_sumer(file)
        self.assertEqual(expected, result)

    def test_all_in_range(self):
        file = 'test3.txt'
        expected = 6
        result = file_sumer(file)
        self.assertEqual(expected, result)

    def test_out_of_range(self):
        file = 'test4.txt'
        with self.assertRaises(ValueError):
            result = file_sumer(file)

    def test_only_plain_text(self):
        file = 'test5.txt'
        with self.assertRaises(TypeError):
            result = file_sumer(file)

if __name__ == '__main__':
    unittest.main()

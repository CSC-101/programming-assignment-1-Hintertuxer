import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
import unittest
from hw1 import vowel_count

class TestVowelCount(unittest.TestCase):
    def test_vowel_count_mixed_case(self):
        self.assertEqual(vowel_count("Hello World"), 3)

    def test_vowel_count_all_vowels(self):
        self.assertEqual(vowel_count("AEIOUaeiou"), 10)

    def test_vowel_count_no_vowels(self):
        self.assertEqual(vowel_count("rhythm"), 0)

    # Part 2
from hw1 import short_lists

class TestShortLists(unittest.TestCase):
    def test_short_lists_with_mixed_lengths(self):
        self.assertEqual(short_lists([[1, 2], [3], [4, 5], [6, 7, 8]]), [[1, 2], [4, 5]])

    def test_short_lists_with_no_two_element_lists(self):
        self.assertEqual(short_lists([[1], [3, 4, 5], []]), [])

    def test_short_lists_all_two_element_lists(self):
        self.assertEqual(short_lists([[10, 20], [30, 40], [50, 60]]), [[10, 20], [30, 40], [50, 60]])


    # Part 3


    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()

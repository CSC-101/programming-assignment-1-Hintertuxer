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


    # Part 3


    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()

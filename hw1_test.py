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
from hw1 import ascending_pairs

class TestAscendingPairs(unittest.TestCase):
    def test_ascending_pairs_mixed_lengths(self):
        self.assertEqual(ascending_pairs([[3, 1], [2, 5, 4], [8, 7], [10]]), [[1, 3], [2, 5, 4], [7, 8], [10]])

    def test_ascending_pairs_with_two_element_lists_only(self):
        self.assertEqual(ascending_pairs([[1, 2], [4, 3], [3, 3]]), [[1, 2], [3, 4], [3, 3]])

    def test_ascending_pairs_no_two_element_lists(self):
        self.assertEqual(ascending_pairs([[1, 2, 3], [4], [5, 6, 7]]), [[1, 2, 3], [4], [5, 6, 7]])

    # Part 4
from hw1 import add_prices, Price

class TestAddPrices(unittest.TestCase):
    def test_add_prices_no_cents_overflow(self):
        price1 = Price(3, 40)
        price2 = Price(4, 50)
        result = add_prices(price1, price2)
        self.assertEqual(result.dollars, 7)
        self.assertEqual(result.cents, 90)

    def test_add_prices_with_cents_overflow(self):
        price1 = Price(3, 75)
        price2 = Price(2, 50)
        result = add_prices(price1, price2)
        self.assertEqual(result.dollars, 6)
        self.assertEqual(result.cents, 25)


    # Part 5
from hw1 import rectangle_area, Rectangle, Point

class TestRectangleArea(unittest.TestCase):
    def test_rectangle_area_standard_case(self):
        top_left = Point(1, 5)
        bottom_right = Point(4, 1)
        rect = Rectangle(top_left, bottom_right)
        self.assertEqual(rectangle_area(rect), 12)

    def test_rectangle_area_zero_area(self):
        top_left = Point(3, 3)
        bottom_right = Point(3, 3)
        rect = Rectangle(top_left, bottom_right)
        self.assertEqual(rectangle_area(rect), 0)

    # Part 6
from hw1 import books_by_author
from hw1 import Book

class TestBooksByAuthor(unittest.TestCase):
    def test_books_by_author_found(self):
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
        book2 = Book("Tender is the Night", "F. Scott Fitzgerald")
        book3 = Book("To Kill a Mockingbird", "Harper Lee")
        books = [book1, book2, book3]
        result = books_by_author("F. Scott Fitzgerald", books)
        self.assertEqual(result, [book1, book2])

    def test_books_by_author_not_found(self):
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
        book2 = Book("Tender is the Night", "F. Scott Fitzgerald")
        books = [book1, book2]
        result = books_by_author("Harper Lee", books)
        self.assertEqual(result, [])

    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()

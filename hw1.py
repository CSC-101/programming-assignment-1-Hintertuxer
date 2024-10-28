import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(input_string: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u) in the input string.
    
    Inputs:
        - input_string (str): The string to check for vowels.
    
    Output:
        - int: The count of vowels in the input string.
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = sum(1 for char in input_string if char in vowels)
    return count

# Part 2
def short_lists(list_of_lists: list[list[int]]) -> list[list[int]]:
    """
    Returns a new list containing only the lists with exactly two elements
    from the input list of lists.

    Inputs:
        - list_of_lists (list[list[int]]): A list of lists of integers.

    Output:
        - list[list[int]]: A list of lists with exactly two elements each.
    """
    return [lst for lst in list_of_lists if len(lst) == 2]

# Part 3
def ascending_pairs(list_of_lists: list[list[int]]) -> list[list[int]]:
    """
    Returns a new list with elements of length 2 sorted in ascending order.
    Lists of other lengths remain unchanged.

    Inputs:
        - list_of_lists (list[list[int]]): A list of lists of integers.

    Output:
        - list[list[int]]: A list where lists of length 2 have their elements in ascending order.
    """
    return [sorted(lst) if len(lst) == 2 else lst for lst in list_of_lists]

# Part 4
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents
def add_prices(price1: Price, price2: Price) -> Price:
    """
    Computes the sum of two Price objects, ensuring the cents are within 0-99.

    Inputs:
        - price1 (Price): The first price to add.
        - price2 (Price): The second price to add.

    Output:
        - Price: A new Price object representing the sum, with cents in the range 0-99.
    """
    # Add dollars and cents separately
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    # Handle any overflow of cents above 99
    if total_cents >= 100:
        total_dollars += total_cents // 100  # Add overflow to dollars
        total_cents = total_cents % 100  # Keep cents in range 0-99

    # Return a new Price object with adjusted dollars and cents
    return Price(total_dollars, total_cents)

price1 = Price(3, 75)
price2 = Price(2, 50)
print(add_prices(price1, price2))

# Part 5
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right


def rectangle_area(rect: Rectangle) -> float:
    """
    Computes the area of an axis-aligned rectangle given by top-left and bottom-right corners.

    Inputs:
        - rect (Rectangle): The rectangle for which to compute the area.

    Output:
        - float: The area of the rectangle.
    """
    # Calculate width and height from the rectangle's coordinates
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y

    # Calculate and return the area
    return width * height

# Part 6
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
    """
    Returns a list of books written by the specified author.

    Inputs:
        - author_name (str): The name of the author to filter by.
        - books (list[Book]): A list of Book objects to search within.

    Output:
        - list[Book]: A list of Book objects written by the specified author.
    """
    return [book for book in books if book.author == author_name]

# Part 7
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

import math

def circle_bound(rect: Rectangle) -> Circle:
    """
    Computes a bounding circle that fully encloses a given rectangle.

    Inputs:
        - rect (Rectangle): The rectangle for which to compute the bounding circle.

    Output:
        - Circle: A Circle object with its center at the rectangle's center and radius equal to the distance
                  from the center to one of the rectangle's corners.
    """
    # Calculate the center of the rectangle
    x_center = (rect.top_left.x + rect.bottom_right.x) / 2
    y_center = (rect.top_left.y + rect.bottom_right.y) / 2
    center = Point(x_center, y_center)

    # Calculate the radius as the distance from the center to the top-left corner
    radius = math.sqrt((center.x - rect.top_left.x) ** 2 + (center.y - rect.top_left.y) ** 2)

    # Return the Circle object
    return Circle(center, radius)
"""
top_left = Point(1, 5)
bottom_right = Point(4, 1)
rect = Rectangle(top_left, bottom_right)

bounding_circle = circle_bound(rect)
print(f"Center: ({bounding_circle.center.x}, {bounding_circle.center.y}), Radius: {bounding_circle.radius}")
# Expected output: Center: (2.5, 3.0), Radius: distance from (2.5, 3.0) to (1, 5)
"""

# Part 8
class Employee:
    def __init__(self, name: str, pay: float):
        self.name = name
        self.pay = pay


def below_pay_average(employees: list[Employee]) -> list[str]:
    """
    Returns a list of names of employees whose pay is below the average pay of all employees.

    Inputs:
        - employees (list[Employee]): A list of Employee objects.

    Output:
        - list[str]: A list of names of employees with below-average pay.
    """
    # Handle an empty list
    if not employees:
        return []

    # Calculate total pay and average pay
    total_pay = sum(employee.pay for employee in employees)
    average_pay = total_pay / len(employees)

    # Collect names of employees with below-average pay
    below_average = [employee.name for employee in employees if employee.pay < average_pay]

    return below_average
"""
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 40000)
employees = [emp1, emp2, emp3]

print(below_pay_average(employees))
# Expected output: ['Alice', 'Charlie'] since the average pay is 50000
"""


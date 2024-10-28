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


# Part 6


# Part 7


# Part 8



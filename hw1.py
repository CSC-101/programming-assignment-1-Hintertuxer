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


# Part 3


# Part 4


# Part 5


# Part 6


# Part 7


# Part 8



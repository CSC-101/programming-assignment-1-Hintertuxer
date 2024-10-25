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


# Part 5


# Part 6


# Part 7


# Part 8



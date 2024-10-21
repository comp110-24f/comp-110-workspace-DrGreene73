"""Implementing some more list utility functions!"""

__author__ = "730663166"


def only_evens(input: list[int]) -> list[int]:
    """Returns a new list only composed of even numbers."""
    new_list: list[int] = list()
    for elem in input:
        if elem % 2 == 0:
            new_list.append(elem)  # fairly easy
    return new_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Generates a kist which is a subset of the input list."""
    sub_list = []
    if len(input) == 0 or start >= len(input) or end <= 0:
        # took some time because I didn't realize that it was written word for word
        return sub_list
    if start < 0:  # this dumb less than sign caused me some points
        start = 0
    if end > len(input):
        end = len(input)
    for elem in range(start, end):
        sub_list.append(input[elem])
        # I forgot we could use range, so I had struggled with this
    return sub_list


def add_at_index(input: list[int], element: int, index: int) -> None:
    """Modifys the input list to place element at given index."""
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # was needed to add space at end of list
    idx = len(input) - 1
    while idx > index:
        input[idx] = input[idx - 1]
        idx -= 1
    input[index] = element
    # This took a while for me. I didn't know how to exactly write this code so
    # I received some help for this

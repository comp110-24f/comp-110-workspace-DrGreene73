"""Using functions to deepen my understanding of historical styles."""

__author__ = "730663166"


def all(lists: list[int], num: int) -> bool:
    """Returns a bool depending on the comparison of the list and numbers"""
    if len(lists) == 0:
        return False
    for elem in lists:
        if elem != num:
            return False
    return True


# I had contemplated on whether or not we could use for loops
# or while loops, so i tried different things for a couple of hours


def max(input: list[int]) -> int:
    """Gives back the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    final_value = input[0]
    for elem in input:
        if elem > final_value:
            final_value = elem
    return final_value


# This also gave me trouble, as i was trying to figure out how I could
# give the biggest number back.
# Some ideas may have worked, but only because im delusional


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determines if two lists are equal at every element."""
    if list_1 != list_2:
        return False
    for index in range(len(list_1)):
        if list_1[index] != list_2[index]:
            return False
    return True


# I didn't know that the range function needed to be used, so I tried
# using a while loop but I could only check at every index.
# I also had lines


def extend(list1: list[int], list2: list[int]) -> None:
    """Extends (or adds on to) a list that exists (bars)."""
    index = 0
    while index < len(list2):
        list1.append(list2[index])
        index += 1


# Fairly easy to do, took like a minute


# for much of this i struggled as i didnt know if for loops were
# allowed.
# Also I tried experimenting too much with both types of loops
# separate and together.

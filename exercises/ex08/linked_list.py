"""A file that uses recursive functions... EX08."""

from __future__ import annotations

__author__ = "730663166"


class Node:
    """A class built for recursive functions."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Needed for the class to function in other functions."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Returns the data of the Node stored at the index given."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)
    # Took me a while but i got it figured out.


def max(head: Node | None) -> int:
    """Returns the maximum data value in the linked list."""
    # I had a feeling that something else was needed but i didn't know what to do.
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    max_value_of_rest: int = max(head.next)
    if head.value > max_value_of_rest:
        max_value_of_rest = head.value
    return max_value_of_rest


def linkify(items: list[int]) -> Node | None:
    """Returns a linked list of nodes with the same value in order of the input list."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list of Nodes with values scaled by scaling factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))

"""Defining unit tests for more utility functions!"""

__author__ = "730663166"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_empty() -> None:
    """Tests to see if a list will come out as only evens"""
    assert only_evens([]) == []


def test_only_evens_none() -> None:
    """Tests to see if a list will come out as only evens"""
    a: list[int] = [1, 3, 5, 7]
    assert only_evens(a) == []


def test_only_evens() -> None:
    """Tests to see if a list will come out as only evens"""
    a: list[int] = [1, 2, 3, 4, 6, 7]
    assert only_evens(a) == [2, 4, 6]


def test_sub_empty() -> None:
    """Edge case?"""
    b: list[int] = []
    assert sub(b, 0, 2) == []


def test_sub_range() -> None:
    """Edge case?"""
    b: list[int] = [2, 3, 4, 9, 11]
    assert sub(b, 1, 3) == [3, 4]


def test_sub_negative() -> None:
    """Edge case?"""
    b: list[int] = [2, 3, 4, 9, 11]
    assert sub(b, -1, 6) == [2, 3, 4, 9, 11]


def test_add_at_index_empty() -> None:
    """Tests how the function should mutate the input."""
    c: list[int] = []
    assert add_at_index(c, 1, 0) == [1]


def test_add_at_index_good() -> None:
    """Tests how the function should mutate the input."""
    c: list[int] = [0, 1, 3, 5, 7]
    assert add_at_index(c, 2, 2) == [0, 1, 2, 3, 5, 7]


def test_add_at_index_raises_indexerror() -> None:
    """Tests how the function should mutate the input."""
    c: list[int] = [0, 1, 3, 5, 7]
    with pytest.raises(IndexError):
        add_at_index(c, 10, 7)


# a lot of unit tests I won't lie
# I kinda had some trouble creating these as a line of code in my utils.py file messed
# up the auto-grader, even when I corrected the code

"""File to define Fish class."""


class Fish:
    """An object that defines the fish of a river."""

    age: int

    def __init__(self):
        """Sets the age of fish to 0."""
        self.age = 0
        return None

    def one_day(self):
        """Ages the fish by one after a day passes."""
        self.age += 1
        return None

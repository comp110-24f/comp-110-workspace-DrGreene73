"""File to define Bear class."""


class Bear:
    """An object that defines the bears of a river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Sets the age and hunger of a bear to zero."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Ages the bear by one after a day passes."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Sets the hunger score to the number of fish eaten plus the previous score."""
        self.hunger_score += num_fish
        return None

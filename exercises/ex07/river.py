"""File to define River class."""

__author__ = "730663166"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """An object that defines life of a river."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish from the populatioon if they are older than a certain age."""
        surviving_fish: list = list()
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        surviving_bears: list = list()
        for bears in self.bears:
            if bears.age <= 5:
                surviving_bears.append(bears)
        self.bears = surviving_bears
        # Kinda confusing because of all the selfs
        return None

    def bears_eating(self):
        """Removes fish from a population and satiates bears hunger."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        # fairly easy
        return None

    def check_hunger(self):
        """Checks the hunger of bears, and removes them if they are too hungry."""
        survivng_bears: list = list()
        for bears in self.bears:
            if bears.hunger_score >= 0:
                survivng_bears.append(bears)
        self.bears = survivng_bears
        # once I figured out how to use the for loops it was easier
        return None

    def remove_fish(self, amount: int):
        """Removes an amount of fish from the front of the list."""
        count = 0
        while count < amount and self.fish:
            self.fish.pop(0)
            count += 1
        return None

    def repopulate_fish(self):
        """Repopulates the fish."""
        num_pairs = len(self.fish) // 2
        count = 0
        while count < num_pairs * 4:
            self.fish.append(Fish())
            count += 1
        # used while loops because I couldn't figure out how to do so with for.
        # goes for the other functions with while loops.
        return None

    def repopulate_bears(self):
        """Repopulates the bears."""
        num_pairs = len(self.bears) // 2
        count = 0
        while count < num_pairs:
            self.bears.append(Bear())
            count += 1
        return None

    def view_river(self):
        """Allows us to see the progress of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        # like squeezing lemons
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        i = 0
        while i < 7:
            self.one_river_day()
            i += 1
        return None

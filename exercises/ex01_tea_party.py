"""Exercise 01: My very own tea party!"""

__author__: str = "730663166"


def main_planner(guests: int) -> None:
    "Calls each function and produces an output."
    # I had struggled with this part for a little bit, as I tried adding int variables-
    # -to strings and kept getting errors.
    # Also didn't realise that I needed guests when adding the numbers.
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    # This was fairly easy to me
    "A function providing the number of teabags for each person."
    return people * 2


def treats(people: int) -> int:
    # Didn't realise int needed to be infront return statement.
    "The number of treats needed for the number of teas being drunk."
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    "Provides the total cost of the tea and treats."
    # Saw that variable assignments cant be used as we havent used them.
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

"""EX02: Creating a character-styled Wordle."""

__author__ = "730663166"


def input_word() -> str:
    """Takes input word and returns it."""
    word: str = str(input("Enter a 5-character word: "))
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """Prompts the user to enter a single character"""
    letter: str = str(input("Enter a single character: "))
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter
    # this followed nearly the exact same pattern as the previous function,
    # only a little words and numbers were changed.


def contains_char(word: str, letter: str) -> None:
    """Checks for index of the word to see if they match"""
    index: int = 0
    instances: int = 0
    print("Searching for " + letter + " in " + word)
    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            instances += 1
        index += 1
    if instances == 0:
        print("No instances of " + letter + " found in " + word)
    elif instances == 1:
        print(str(instances) + " instance of " + letter + " found in " + word)
    else:
        print(str(instances) + " instances of " + letter + " found in " + word)
    # This part gave me trouble as I was stuck here for a few minutes, but after
    # looking at some practice problems and the CQ3, i figured out how it shoud work


def main() -> None:
    """Handles all function calls and variable assignments."""
    contains_char(word=input_word(), letter=input_letter())
    # this was easy for me, took like a minute


if __name__ == "__main__":
    main()

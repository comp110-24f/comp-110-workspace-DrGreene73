"""The full (not really) game of NYT's Wordle."""

__author__ = "730663166"


def input_guess(secret_word_len: int) -> str:
    """Prompts the user to enter a word"""
    guess: str = str(input(f"Enter a {secret_word_len} character word: "))
    while len(guess) != secret_word_len:
        guess = input((f"That wasn't {secret_word_len} chars! Try again: "))
    return guess
    # I struggled with this part as I had an error, but I
    # realised it was because I had a dash in my code


def contains_char(search_char: str, single_char: str) -> bool:
    """Supposed to find a char in the letter searched for."""
    assert len(single_char) == 1
    index = 0
    while index < len(search_char):
        if single_char == search_char[index]:
            return True
        else:
            index += 1
    return False
    # Fairly easy, took me a good 15 minutes because I had to
    # make sure the index would increase to a point where
    # all indexes where checked before the function returned false


def emojified(guess: str, secret_word: str) -> str:
    """Represents the accuracy of a guess"""
    assert len(guess) == len(secret_word)
    result_emojis = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    while index < len(guess):
        if guess[index] == secret_word[index]:
            result_emojis += GREEN_BOX
        elif contains_char(secret_word, guess[index]):
            result_emojis += YELLOW_BOX
        else:
            result_emojis += WHITE_BOX
        index += 1
    return result_emojis
    # When I ran this in the actual file, I had multiple colored boxes
    # because I had two separate indexes. When I made it one,
    # the function worked as intended.
    # This ended up taking hours due to simple errors on my part.


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 0
    max_turns = 6
    won = False

    while turns < max_turns and not won:
        turns += 1
        print(f"=== Turn {turns}/6 ===")

        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            won = True
    if not won:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")
    # This was a little difficult as I thought the instructions were
    # vague, but I was able to figure it out.
    # Also, struggled with the print statements and emojified


if __name__ == "__main__":
    main(secret="codes")

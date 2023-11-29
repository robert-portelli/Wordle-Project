# main.py
"""A wordle clone"""
# import pathlib
# import random
from string import ascii_letters
from string import ascii_uppercase
from rich.console import Console
from guess_styler import display_guesses

WORD = 'SNAKE'
WORD_LEN = 5
MAX_ATTEMPTS = 6
STATUS = str('_' * WORD_LEN)
GUESSES = [STATUS] * MAX_ATTEMPTS
CONSOLE = Console(width=40)
CHARACTERS = ascii_uppercase
BANNER = f"Please enter {WORD_LEN} of the following characters:\
    {CHARACTERS}"

def main_process():
    while True:
        print(BANNER)
        guess = input("\nGuess word: ").upper()

        # handle incorrect quantity of guessed characters
        if len(guess) != WORD_LEN:
            print(f"{guess} is {len(guess)} characters not {WORD_LEN}")
            continue

        # handle repeat guess
        if guess in set(GUESSES):
            print(f"You already guessed the word {guess}.")
            continue

        # handle incorrect character(s) given in guess
        if not set(guess).issubset(CHARACTERS):
            invalid_chars = set(guess) - CHARACTERS
            print(f"{', '.join(invalid_chars)} is not a valid choice.\
                  Please use {', '.join(CHARACTERS)}")
            continue
        return guess


if __name__ == "__main__":
    for _ in range(MAX_ATTEMPTS):
        display_guesses(GUESSES, WORD)
        GUESSES[_] = main_process()
        if GUESSES[_] == WORD:
            break

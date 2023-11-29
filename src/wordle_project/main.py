# main.py
"""A wordle clone"""
# import pathlib
# import random
from rich.console import Console
from guess_styler import display_guesses

WORD = 'SNAKE'
WORD_LEN = 5
MAX_ATTEMPTS = 6
STATUS = str('_' * WORD_LEN)
GUESSES = [STATUS] * MAX_ATTEMPTS
CONSOLE = Console(width=40)


if __name__ == "__main__":
    for _ in range(MAX_ATTEMPTS):
        display_guesses(GUESSES, WORD)
        GUESSES[_] = input("\nGuess word: ").upper()
        if GUESSES[_] == WORD:
            break

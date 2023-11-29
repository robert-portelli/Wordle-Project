# main.py
"""A wordle clone"""
import pathlib
import random
import tomllib
from string import ascii_letters
from string import ascii_uppercase
from rich.console import Console
from guess_styler import display_guesses

WORDS_PATH = pathlib.Path(__file__).parent / "WORDS.toml"
WORD_LEN = 5
MAX_ATTEMPTS = 6
STATUS = str('_' * WORD_LEN)
GUESSES = [STATUS] * MAX_ATTEMPTS
CONSOLE = Console(width=40)
CHARACTERS = ascii_uppercase
BANNER = f"Please enter {WORD_LEN} of the following characters:\
    {CHARACTERS}"
WORD_TOPIC = 'misc'


def main():
    word = pre_process(WORDS_PATH)
    for _ in range(MAX_ATTEMPTS):
        display_guesses(GUESSES, word)
        GUESSES[_] = main_process()
        if GUESSES[_] == word:
            break

def pre_process(path):
    words = tomllib.loads(path.read_text())
    topic = words[WORD_TOPIC]['words'][0]['words']
    desired_words = [word for word in topic if len(word) == WORD_LEN]
    return random.sample(desired_words, k=1)

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
    pass

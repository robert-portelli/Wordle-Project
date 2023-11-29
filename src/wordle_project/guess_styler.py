"""
Module: guess_styler.py

This module defines a function for styling guessed letters based on their correctness
and their position in the target word. It utilizes the Rich library for console styling.

Example usage:
TARGET = "example"
GUESSES = ["example", "exemplar", "excavate"]
display_guesses(GUESSES, TARGET)

"""

from string import ascii_letters
from rich.console import Console


def display_guesses(guesses, word):
    """
    Display styled guesses for each letter in a list of guesses based on correctness and position.

    Parameters:
    - guesses (list): A list of strings representing guessed words.
    - word (str): The target word to compare guesses against.

    Returns:
    None
    """
    # Create a Rich Console instance for styling output
    console = Console()

    # Iterate through each guess in the list of guesses
    for guess in guesses:
        # Initialize an empty list to store styled characters for the current guess
        styled_guess = []
        # Iterate through each letter in the current guess and its corresponding letter in the target word
        for letter, correct in zip(guess, word):
            # Structural pattern matching to determine the styling based on conditions
            match (letter, correct):
                # Case: Correct guess (letter matches the correct letter in the word)
                case (letter, correct) if letter == correct:
                    style = "bold white on green"
                # Case: Incorrect guess, but the letter is in the word
                case (letter, _) if letter in word:
                    style = "bold white on yellow"
                # Case: Incorrect guess, and the letter is not in the word but is a valid letter (ascii_letters)
                case (letter, _) if letter in ascii_letters:
                    style = "white on #666666"
                # Case: Incorrect guess, and the letter is neither correct nor a valid letter
                case (letter, _):
                    style = "dim"
            # Append the styled letter to the list
            styled_guess.append(f"[{style}]{letter}[/]")

        # Print the styled guess, centering the output
        console.print("".join(styled_guess), justify="center")


if __name__ == "__main__":
    # Example usage:
    TARGET = "example"
    GUESSES = ["example", "exemplar", "excavate"]

    # Display styled guesses for the example word and guesses
    display_guesses(GUESSES, TARGET)

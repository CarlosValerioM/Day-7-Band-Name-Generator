#!/usr/bin/env python3
"""
hangman.py - A simple Hangman game.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/10
License: MIT
Dependencies: None (built-in functions only)

Description:
This script implements a basic Hangman game where the player guesses letters of a hidden word.
The game provides feedback on correct and incorrect guesses and ends when the player either
completes the word or runs out of attempts.

Usage:
Run the script and follow the prompts:
    python hangman.py

Example Output:
    Guess a letter: e
    Correct! The word so far: _ e _ _ _
"""
import random  # Importing the random module to select a random word from the list.


# Function to check if the chosen letter exists in the word
def is_letter_in_word(chosen, word):
    index = []  # List to store the indices of the letter in the word
    # Iterate through the word and find the positions of the chosen letter
    for i, letter in enumerate(word):
        if letter == chosen:
            index.append(i)  # Add the index to the list if the letter matches
    return index  # Return the list of indices


# Function to update the player’s word with the chosen letter
def add_letter(index, letter, player_word):
    for i in index:
        player_word[i] = letter  # Replace the placeholder with the chosen letter
    return player_word  # Return the updated player word


# Main function to run the Hangman game
def main():
    print("Welcome to Hangman!")  # Display welcome message

    # List of 5-letter words to choose from
    words = [
        "apple", "house", "grape", "water", "light",
        "heart", "stone", "plant", "chair", "table",
        "music", "peace", "night", "cloud", "peace",
        "bread", "sleep", "plane", "dream", "party", "fight"
    ]

    # Randomly select a word from the list
    word = random.choice(words)

    lives = 5  # The player starts with 5 lives
    player_word = ["_", "_", "_", "_", "_"]  # The player’s word is initially hidden as underscores

    # Main game loop, continues until the player runs out of lives or guesses the word
    while lives and "".join(player_word) != word:
        print(player_word)  # Display the current state of the player's word
        letter_chosen = input("Guess a letter: ")  # Prompt the player to guess a letter
        index = is_letter_in_word(letter_chosen, word)  # Check if the letter is in the word

        # If the letter is not in the word, the player loses a life
        if not index:
            print(f"You guessed {letter_chosen}, that's not in the word. You lose a life.")
            lives -= 1  # Reduce one life
        else:
            player_word = add_letter(index, letter_chosen, player_word)  # Update the word with the chosen letter


# This ensures that the main function is only called when the script is run directly
if __name__ == '__main__':
    main()
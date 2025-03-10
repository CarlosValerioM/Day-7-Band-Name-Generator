# Day-7-Hangman-Game
Your Hangman Game - Difficulty: Easy

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/07

## License:
MIT License

## Dependencies:
random (Python built-in library)
## Description:
hangman.py is a simple Python script for playing the classic game of Hangman. It randomly selects a word from a predefined list and allows the player to guess letters one at a time. The game continues until the player either guesses the word correctly or runs out of lives.

## How the game works:
1. The game randomly selects a 5-letter word from a list.
2. The player starts with 5 lives.
3. The player is asked to guess one letter at a time.
4. If the guessed letter is in the word, it replaces the corresponding underscore(s) in the word.
5. If the guessed letter is not in the word, the player loses one life.
5. The game continues until the word is fully guessed or the player loses all their lives.
## Usage:
Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/Day-7-Hangman-Game.git
```
Navigate to the project directory:
```bash
cd Day-7-Hangman-Game
```
Run the script:
```bash
python hangman.py
```
The script will display the current word (with underscores for unguessed letters) and prompt the player to guess a letter.

## Example Output:
```arduino
Welcome to Hangman!
['_', '_', '_', '_', '_']
Guess a letter: a
['a', '_', '_', '_', '_']
Guess a letter: o
You guessed o, that's not in the word. You lose a life.
['_', '_', '_', '_', '_']
...
```
## How it works:
The script selects a random 5-letter word from a list.

The player guesses letters one by one. If the letter is found in the word, the script updates the player’s word.

The player is allowed 5 incorrect guesses before they lose the game.

## License:
This project is licensed under the MIT License.

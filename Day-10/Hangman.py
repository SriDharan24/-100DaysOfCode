# hangman.py

import random
import sys

WORD_LIST = [
    "python", "developer", "hangman", "challenge", "function",
    "variable", "iteration", "condition", "syntax", "exception"
]

MAX_LIVES = 6

def choose_word():
    """Randomly pick a word from WORD_LIST."""
    return random.choice(WORD_LIST)

def display_state(word, guessed_letters, lives):
    """Display the current hangman state."""
    display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\nWord: {display}")
    print(f"Lives left: {lives}")
    print(f"Guessed: {', '.join(sorted(guessed_letters))}\n")

def hangman():
    word = choose_word()
    guessed_letters = set()
    lives = MAX_LIVES

    print("🪢 Welcome to Hangman!")
    print(f"You have {lives} lives to guess the word.\n")

    # Game loop
    while lives > 0:
        display_state(word, guessed_letters, lives)

        guess = input("Enter a letter (or 'quit' to exit): ").lower().strip()
        if guess == "quit":
            print("Goodbye!")
            sys.exit()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("⚠️  You've already guessed that letter.")
            continue

        guessed_letters.add(guess)
        if guess in word:
            print("✅  Correct!")
            # Check win
            if all(letter in guessed_letters for letter in word):
                print(f"\n🎉 You guessed it! The word was **{word}**.")
                break
        else:
            lives -= 1
            print("❌  Wrong!")
            if lives == 0:
                print(f"\n💀 You ran out of lives. The word was **{word}**.")

if __name__ == "__main__":
    hangman()

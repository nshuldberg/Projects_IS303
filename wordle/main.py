<<<<<<< HEAD
# Noah Shuldberg
# Wordle word-guessing game
from worlde_functions import get_guess, choose_word, evaluate_guess, display_guess, has_won
import sys
# Welcome player to the game
print("\nWelcome to the Wordle!")
# Play again while loop
play_again = "Y"
num_guesses = 1
while play_again == "Y":
    attempt = 0
    if num_guesses > 0:
        num_guesses = 6
        # Generate secret word
        word = choose_word('')
        guess_list = []
        # Run get_guess
        while attempt < num_guesses:
            print(f"\nGuess #{attempt+1}")
            guess = get_guess("")
            if guess in guess_list:
                print("You already guessed this word! Try again.")
                continue
            elif guess == word:
                attempt += 1
                break
            else:
                # Evaluate guess
                feedback = evaluate_guess(guess, word)
                attempt += 1
            guess_list.append(guess)
            # Display guess
            print(display_guess(guess, feedback))
            
    if has_won(guess, word) == True:
        print("You guessed the word! Congratulations!")
        print(f"It took you {attempt}/6 attempts.")
    elif has_won(guess,word) == False:
        print(f"So close! The correct word was {word}")
    play_again = input("Would you like to play again? (Y/N) ").upper()
=======
# Noah Shuldberg
# Wordle Game
from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won
print("Welcome to the Wordle!")
play_again = "Y"
while play_again != "N":
    num_guesses = 6
    attempt = 0
    guess_list = []
    # Generate secret word
    word = choose_word()
    while attempt < num_guesses:
            
            # Prompt user for guess
            print(f"\nGuess #{attempt+1}")
            guess = get_guess("")

            # Check if word has already been guessed before taking away a guess.
            while guess in guess_list:
                print("You already guessed this word! Try again.")
                guess = get_guess("")

            guess_list.append(guess)  

            # Break if guess is right
            if guess == word:
                attempt += 1
                break

            # If guess is wrong, evaluate player's guess
            feedback = evaluate_guess(guess, word)
            print('\n')
            display_guess(guess, feedback)
            attempt += 1

    if has_won(guess, word) == True:
        print("Congratulations! You guessed the word.")
    else:
        print(f"So close! The word was {word}")
    play_again = input("Would you like to play again? (Y/N): ").upper()
>>>>>>> 7a84d9a76bf4297e73f79b8669315e3f35e5e2be

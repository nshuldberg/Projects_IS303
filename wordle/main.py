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
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
# Noah Shuldberg
# Wordle word-guessing game
import worlde_functions
# Welcome player to the game
# Play again while loop
play_again = ""
while play_again != "N":
    num_guesses = 6
    while num_guesses > 0:
        # Generate secret word
        rand_word = ""
        word = worlde_functions.choose_word(rand_word)

        # Run get_guess
        for guess in range(num_guesses):
            guess = worlde_functions.get_guess(guess)
            if guess == word:
                break
            else:
                
            
            # if guess has correctly placed letters, display greens.
            # if guess[0] == word[0]:
                # print("G----")
            # if guess has correct letters (not correctly placed), display yellows.
            # if guess has no correct letters, display nothing.
            num_guesses -= 1


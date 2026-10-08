# Noah Shuldberg
# Functions for Rock, Paper, Scissors game

# Input: choose rock, paper, or scissors
# input.lower
# Check if input is equal to "rock", "paper", or "scissors".
# Return choice

def get_player_choice(choice):
    player_choice = None
    options = ["rock", "paper", "scissors"]
    while player_choice not in options:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice in options: 
            break
        else:
            print("Invalid input. Try again.")
            continue
    return player_choice



def determine_winner(player, computer):
    if (player == "rock" and computer == "rock") or (player == "paper" and computer == "paper") or (player == "scissors" and computer == "scissors"):
       win_decision = "Tie!"
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
       win_decision = "You win!"
    elif (player == "scissors" and computer == "rock") or (player == "paper" and computer == "scissors") or (player == "rock" and computer == "paper"):
        win_decision = "You lose!"

    return win_decision 





# Compare player's choice and computer's choice.
# Store the values
# Categorize them as win, lose, tie.
# Noah Shuldberg
# Rock, Paper, Scissors game
import random

# Get Player Choice function
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

# Determine winner function
def determine_winner(player, computer):
    if (player == "rock" and computer == "rock") or (player == "paper" and computer == "paper") or (player == "scissors" and computer == "scissors"):
       win_decision = "Tie!"
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
       win_decision = "You win!"
    elif (player == "scissors" and computer == "rock") or (player == "paper" and computer == "scissors") or (player == "rock" and computer == "paper"):
        win_decision = "You lose!"

    return win_decision 
# Welcome player
print("Welcome to rock, paper, scissors!")

wins = 0
losses = 0

while True:
    rounds_play = int(input("How many rounds would you like to play?: "))
    if rounds_play <= 0:
        print("Invalid input. Try again.")
        continue
    else:
        if rounds_play % 2 == 0:
            print("There must be a winner, so please enter an odd number!")
            continue
        elif rounds_play % 2 != 0:
            print(f"\n{rounds_play} rounds! Let's play!")
            break 
        
while (wins + losses) < rounds_play:
    # Begin function #1: Get player and computer's input
    choice = ""
    options_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options_list)
    player_choice = get_player_choice(choice)
    print(f"\nYour choice: {player_choice}")
    print(f"\nOpponent's choice: {computer_choice}")
    print("\n" + determine_winner(player_choice, computer_choice))
    if determine_winner(player_choice, computer_choice) == "Tie!":
        print("Round doesn't count. Play again.")
        continue

    # Begin function #2: Compare player and computer choices.
    if determine_winner(player_choice, computer_choice) == "You win!":
        wins += 1
    elif determine_winner(player_choice, computer_choice) == "You lose!":
        losses += 1
print("Game over!")
print(f"You: {wins} | Computer: {losses}")
if wins > losses:
    print("\nYou win! Congrats!")
else:
    print("\nYou lost. Better luck next time!")
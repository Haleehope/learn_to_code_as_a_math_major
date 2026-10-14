# ###################################################################
# Rock paper scissors
# ###################################################################

# this is a generic CS project that I feel like is an assignment in every intro to CS class
# you could also do tic tac toe

# the computer will randomly pick rock, paper, or scissors, so we need to import the random library
import random

# random.randint gives a random integer, so we will map this to a list with the strings rock, paper, and scissors
choices = ["rock", "paper", "scissors"]

# start with the player and computer scores as zero
player_score = 0
computer_score = 0

# best out of five means that a player wins if they win 3 games
# while neither player has won 3 games...
while player_score < 3 and computer_score < 3:
    # input the player's choice
    player = input("Rock, paper, or scissors? ").lower()

    # error handle with continue
    if player not in choices:
        print("Invalid choice. Try again.")
        continue

    # make the computer randomly choose a choice
    computer = random.randint(0, 3)
    print("Computer chose:", choices[computer])

    # if their choices are the same, then it's a tie
    if player == computer:
        print("Tie!")
    # else if it's one of multiple choices where the player wins
    elif (
        (player == "rock" and choices[computer] == "scissors")
        or (player == "paper" and choices[computer] == "rock")
        or (player == "scissors" and choices[computer] == "paper")
    ):
        print("You win this round!")
        player_score += 1
    # else the computer won
    else:
        print("Computer wins this round!")
        computer_score += 1

    # print the current score
    print(f"Score: You {player_score}, Computer {computer_score}")

# print who won at the end
if player_score == 3:
    print("You won the match!")
else:
    print("Computer won the match!")

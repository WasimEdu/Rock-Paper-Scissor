# Created by: Wasim

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    randon_number = random.randint(0, 2)

    user_pick = input("Type Rock, Paper, Scissor or Q to quit: ").lower()

    if user_pick == "q":
        break

    if user_pick not in options:
        continue

    computer_pick = options[randon_number]
    print("Computer picked", computer_pick + ".")

    if user_pick == "rock" and computer_pick == "scissor":
        print("You Win!")
        user_wins += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You Win!")
        user_wins += 1

    elif user_pick == "scissor" and computer_pick == "paper":
        print("You Win!")
        user_wins += 1

    else:
        print("You Lost!")
        computer_wins += 1
    
print("You win", user_wins, "times")
print("Computer win", computer_wins, "times")
print("Good Bye!")
import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
player_choice = input("Enter your choice = ").lower()

if (
    (player_choice == "rock" and computer_choice == "scissors")
    or (player_choice == "scissors" and computer_choice == "paper")
    or (player_choice == "paper" and computer_choice == "rock")
):
    print(f"You win,Computer picked {computer_choice}")

elif player_choice == computer_choice:
    print("You tied")

elif (
    player_choice != "rock" and player_choice != "scissors" and player_choice != "paper"
):
    print("Invalid choice")

else:
    print(f"You lost, Computer picked {computer_choice}")

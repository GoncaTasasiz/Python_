import random

rock_paper_scissors = ["Rock", "Paper", "Scissors"]

computer_choise = random.choice(rock_paper_scissors).lower()

user_choice = input("Select any of them: Rock, Paper, or Scissors: ").lower()

if user_choice == computer_choise:
    print(f"Computer chose: {computer_choise}")
    print("It's a draw!")
elif user_choice == "rock" and computer_choise == "scissors":
    print(f"Computer chose: {computer_choise}")
    print("You win :) ")  
elif user_choice == "scissors" and computer_choise == "paper":
    print(f"Computer chose: {computer_choise}")
    print("You win :) ")
elif user_choice == "paper" and computer_choise == "rock":
    print(f"Computer chose: {computer_choise}")
    print("You win :) ")
else:
    print(f"Computer chose: {computer_choise}")
    print("You lose :( Try again)")    
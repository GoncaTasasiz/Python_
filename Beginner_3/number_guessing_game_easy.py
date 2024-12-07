import random

print("""
   ______                        __  __            _   __                __             
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                              """)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

number = random.randint(1, 100)

if level == "easy":
    attempts = 10
    print(f"You have {attempts} attempts to guess the number.")
if level == "hard":
    attempts = 5
    print(f"You have {attempts} attempts to guess the number.")

continue_guess = True
while continue_guess: 
    if attempts < 1:
        print("You've run out of guesses. Refresh the page to run again. ")   
    continue_guess = False 
    guess = int(input("Make a guess: ")) 
    if number > guess:
        attempts -= 1
        print("Too low")
        print("guess again")
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif number < guess:
        attempts -= 1
        print("Too high")    
        print("guess again")
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif number == guess:
        print(f"You got it! The answer was {number}")
        continue_guess = False       
        
    


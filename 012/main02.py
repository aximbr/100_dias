#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
EASY_LEVEL = 10
HARD_LEVEL = 5

def generate_guess_number():
    import random
    return random.randint(1,100)

def clear():
    import os
    os.system("cls")

def set_level():
    entry_level = input("Choose a dificult. Type 'easy' or 'hard': ")
    if entry_level.lower() == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_number(number_in, n_in):
    global is_game_over
    if n_in < number_in:
        return "Too low."
    elif n_in > number_in:
        return "Too high."
    else:
        is_game_over = True
        return "Yout got it! The number was " + str(number_in)

#main()
clear()
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm guessing a number between 1 and 100.")


tentatives = set_level()
number = generate_guess_number()
is_game_over = False

while (tentatives >0) and not is_game_over:
    print(f"You have {tentatives} attempts remaining to guess the number.")
    n = int(input("Make a guess: "))
    print(f"{check_number(number, n)}")
    tentatives -= 1
    if (tentatives > 0) and not is_game_over:
        print("Guess again.")
    elif (tentatives < 1):
        print(f"You runnout of tentatives. The guessed number was {number}")

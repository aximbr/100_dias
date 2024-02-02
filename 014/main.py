#import

from game_data import data
from art import logo, vs
MAX_INDEX = len(data) -1

#support functions
def clear():
    import os
    os.system("cls")

def print_message(A_in, B_in):
    print(f"Compare A: {data[A_in]['name']}, a {data[A_in]['description']}, from {data[A_in]['country']}")
    print(vs)
    print(f"Against B: {data[B_in]['name']}, a {data[B_in]['description']}, from {data[B_in]['country']}")

def check_answer(A_in, B_in):
    answer = ""
    while answer not in ["A","B"]:
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if answer == "A":
        if data[A_in]['follower_count'] > data[B_in]['follower_count']:
            return 1
        else:
            return -1
    else:
        if data[B_in]['follower_count'] > data[A_in]['follower_count']:
            return 1
        else:
            return -1 

def game(A_in, B_in):
    print_message(A_in, B_in)
    return check_answer(A_in, B_in)
    

#main()
from random import randint
clear()
print(logo)
score = 0
isGameOver = False
option_A = 0
option_B = 0

while option_A == option_B:
    option_A = randint(0, MAX_INDEX)
    option_B = randint(0, MAX_INDEX)

while not isGameOver:
    if game(option_A, option_B) > 0:
        score += 1
        clear()
        print(f"You're Right. Your score: {score}")
        option_A = option_B
        while option_A == option_B:
            option_B = randint(0, MAX_INDEX)

    else:
        isGameOver = True
        clear()
        print(logo)
        print(f"Sorry you're wrong. The final score: {score}")

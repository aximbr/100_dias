#Heads and tails
import random

user_choice =int(input("Enter your choice: 0 = heads and 1 = tails: "))

computer_choice = random.randint(0, 1)

if user_choice == computer_choice:
    print("Congratule you win!")
else:
    print("Sorry you loose!")


#Rock, paper scissor game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand = [rock, paper, scissors]

user_entry = int(input("Select your option: (0)for Rock, (1) for paper or (2) for scissor\n"))

computer_choice = random.randint(0,2)

print("Your choice:")
print(hand[user_entry])
print("computer choice:")
print(hand[computer_choice])

if user_entry < 0 or user_entry > 2:
    print("Invalid choice, you lose.")

elif user_entry == computer_choice: 
    print("It's a draw!")
    
elif user_entry == 0: #Rock
    if computer_choice == 1:
        print("You Win!")
    else:
        print("You lose!")

elif user_entry == 1: #Papaer
    if computer_choice == 0:
        print("You Win!")
    else:
        print("You lose!")

else:  #Scissor
    if computer_choice == 0:
        print("You lose!")
    elif computer_choice == 1:
        print("You Win!")
    

import os
import math
from art import logo

#clearin the screen
#os.system('cls')
def cls():
    os.system('cls')

def add_bind(name_in, bind_in):
    new_entry = {}
    new_entry["name"] = name_in
    new_entry["bind_value"] = bind_in
    bind.append(new_entry)


#main()
cls()
print(logo)
bind = []
running = True

while running:
    name_entry = input("What's your name? :")
    bind_entry = int(input("What's your bid? :$"))
    add_bind(name_in= name_entry, bind_in= bind_entry)
    answer = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    if answer != "yes":
        running = False
    cls()

winner = 0
high_bind = 0
numbers_of_bidders = len(bind)
for key in range(numbers_of_bidders):
    if bind[key]["bind_value"] > high_bind:
        high_bind = bind[key]["bind_value"]
        winner = key
print(f"The winner is {bind[winner]['name']}")

   


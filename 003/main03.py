#Test of condition
print("Welcome to our rollecoaster!")
height = int(input("Enter your height in cm :"))

#test condition
if height >= 120:
    age = int(input("Enter your age :"))
    if age >=18:
        print("You will pay $12 for your ticket")
    elif age >=12:
        print("You will pay $7 for your ticket")
    else:
        print("You will pay $5 for your ticket")
    print("Enjoy your hide!")
else:
    print("Sorry you are too short, go home!")

#Test of condition
print("Welcome to our rollecoaster!")
height = int(input("Enter your height in cm :"))
bill = 0

#test condition
if height >= 120:
    age = int(input("Enter your age :"))
    if (age >=45) and (age <= 55):
        print("Senior ticket is $0.")
    elif age >=18:
        print("Adult ticket is $12.")
        bill = 12
    elif age >=12:
        print("Young ticket is $7.")
        bill = 7
    else:
        print("Child ticket is $5.")
        bill = 5
    answer = input("Do you want a photo> Y or N: " )
    if answer == "Y":
        bill += 3
    print(f"Your total ticket is ${bill}")
else:
    print("Sorry you are too short, go home!")
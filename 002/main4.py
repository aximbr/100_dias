#Tip Calculator
print("Welcome to the Tip Calculator")
bill = float(input("Enter the total of bill: $"))
tip = int(input("Enter the value of tip 10, 12 or 15: "))
split = int(input("Enter number of people to split the bill: "))

#calculate the amount per user
amount = bill * (1+ tip/100)
amount /= split

#Print out
print(f"Each persorn should pay ${round(amount,2)}")

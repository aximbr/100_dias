print("Welcome to love calculator!")
name_1 = input("Enter the name of first person :")
name_2 = input("Enter the name of second person :")

name_together = name_1 + name_2

name_together_lower = name_together.lower()

#Let´s count TRUE and LOVE
count_1 = 0
count_2 = 0
count_1 += name_together_lower.count("t")
count_1 += name_together_lower.count("r")
count_1 += name_together_lower.count("u")
count_1 += name_together_lower.count("e")

count_2 += name_together_lower.count("l")
count_2 += name_together_lower.count("o")
count_2 += name_together_lower.count("v")
count_2 += name_together_lower.count("e")

result = count_1*10 + count_2

#print out result
if (result < 10) or (result >90):
    print(f"Your score is {result}, you go together like Coke and Metos.")
elif (result > 40) and (result < 50):
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")


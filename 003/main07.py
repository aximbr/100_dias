#Another exercise with conditional
print("Welcome to Python pizza!")
size = input("Enter your pizza size Small, Medium or Large : ")
add_pepperoni = input("Add pepperoni (Y/N)? ")
extra_cheese = input("Add extra cheese (Y/N)? ")

pizza_value = 0 

if size == "S":
    pizza_value = 15
elif size == "M":
    pizza_value = 20
else:
    pizza_value = 25

if add_pepperoni == "Y":
    if size == "S":
        pizza_value += 2
    else:
        pizza_value += 3

if extra_cheese == "Y":
    pizza_value += 1

print(f"Your final bill is: {pizza_value}.")


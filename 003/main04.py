#Day 3 - BMI with details
weight = float(input("Enter your weight in kilos:"))
height = float(input("Enter your height in meters:"))
bmi = round(weight/(height**2), 1)

print(f"Your BMI is {bmi}")
#Print diagnostic based on BMI
if bmi< 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("Your are normal weight.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")



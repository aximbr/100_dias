#Who will pay the bill
import random

names_string = input("Enter names of people that are in the table separated by comma: ")

names = names_string.split(",")

nr_names = len(names)

choosed = names[random.randint(0,nr_names -1)]

print(f"The bill goes to {choosed}")


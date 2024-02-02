#check if a number is prime
def prime_checker(number):
    if (number == 2) or ( (number >1) and (number%2 == 1)):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#main
n = int(input("Check this number: "))
prime_checker(number=n)


#Calculator functions
#Add
def add(n1, n2):
    """add two numbers"""
    return n1 + n2

#Subtraction
def sub(n1, n2):
    """subtract n1 from n2"""
    return n1 - n2

#Multiply
def mult(n1, n2):
    """return the product of n1 by n2"""
    return n1*n2

#Division
def div(n1, n2):
    """returns the division n1 by n2"""
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div
}

num1 = int(input("What's the first number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick a operation from the line above: ")
num2 = int(input("What's the second number: "))

answer = operations[operation_symbol](num1, num2)
#operation_function = operations[operation_symbol]
#answer = operation_funtion(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick a operation from the line above: ")
num3 = int(input("What's the next number: "))
answer2 = operations[operation_symbol](answer, num3)
print(f"{answer} {operation_symbol} {num3} = {answer2}")

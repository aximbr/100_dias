

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

def calculator():
    continue_run = True

    num1 = int(input("What's the first number: "))
    for symbol in operations:
            print(symbol)

    while continue_run:
        operation_symbol = input("Pick a operation: ")
        next_num = int(input("What's the next number: "))

        answer = operations[operation_symbol](num1, next_num)
        print(f"{num1} {operation_symbol} {next_num} = {answer}")

        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to a new calculation ") != "y":
            continue_run = False
            calculator()
        num1 = answer
        

#main()
calculator()

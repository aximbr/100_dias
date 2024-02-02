MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


PENNY = 0.01
NICKLE = 0.05
DIME = 0.10
QUARTER = 0.25

def cls():
    """Clear the screen"""
    import os
    os.system("cls")

def print_message():
    """Print the initial message and return the command"""
    command = input("What would you like? (espresso/latte/cappuccino):").lower()
    return command

def print_report(money_in):
    """Print report related to resources remain"""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffe: {resources['coffee']}")
    print(f"Money: ${money_in}")


def is_resources(selection_in):
    """Check if there is enough resorce for drink selected"""
    for x in MENU[selection_in]["ingredients"]:
        if resources[x] < MENU[selection_in]["ingredients"][x]:
            print(f"Sorry there is not enough {x}.")
            return False
        else:
            return True


def ask_coin(selection_in):
    """Ask for coins and check if it's enough for the drink selected"""
    money_in = 0.0
    expense = MENU[selection_in]["cost"]
    print("Please insert coins.")
    num_quarter = int(input("How many quarters: "))
    num_dime = int(input("How many dimes: "))
    num_nickle = int(input("How many nickles: "))
    num_penny = int(input("How many pennies: "))
    money_in = num_quarter * QUARTER + num_dime * DIME + num_nickle * NICKLE + num_penny * PENNY
    if money_in > expense:
        print(f"Here is ${round(money_in - expense, 2)} in change.")
        money_in = expense
    elif money_in < expense:
        print("Sorry, that's not enough money. Money refunded.")
        money_in = 0
    else:
        money_in = expense
    return money_in


def execute(selection_in):
    """Prepare the receipt, decrement resourses"""
    for x in MENU[selection_in]["ingredients"]:
        resources[x] -= MENU[selection_in]["ingredients"][x]
    print(f"Here is your {selection_in}. ☕ Enkoy!")


#main()
cls()
money = 0.0
command = ""

while command != "off":
    command = print_message()
    if command == "report":
        print_report(money)
    elif command == "espresso" or command == "latte" or command == "cappuccino" :
        if is_resources(command):
            money_in = ask_coin(command)
            if money_in > 0:
                execute(command)
                money += money_in
#end











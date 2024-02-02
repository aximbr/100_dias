from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def cls():
    """Clear the screen"""
    import os
    os.system("cls")

def print_message(menu_in):
    """Print the initial message and return the command"""
    command = input(f"What would you like? {menu_in.get_items()}: ").lower()
    return command


#main()

my_menu = Menu()
my_coffe_maker = CoffeeMaker()
my_money_machine = MoneyMachine()


cls()
command = ""

while command != "off":
    command = print_message(my_menu)
    if command == "report":
        my_coffe_maker.report()
        my_money_machine.report()
    elif command == "espresso" or command == "latte" or command == "cappuccino" :
         if my_coffe_maker.is_resource_sufficient(my_menu.find_drink(command)):
            if my_money_machine.make_payment(my_menu.find_drink(command).cost):
                my_coffe_maker.make_coffee(my_menu.find_drink(command))

#end


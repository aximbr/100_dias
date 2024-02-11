#import turtle

#timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# #mdule ^      class  ^   class ^

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("LightSeaGreen")

# my_screen = Screen()


# x = 100
# timmy.forward(x)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squitle", "Chamander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align["Pokemon Name"] = "l"

print(table)

from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

winner = ""

turtles = []

def create_turtles():
    x_start = -230
    y_start = -150
    y_increment = 50
    for color in colors:
        new_turtle = Turtle(shape = "turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=x_start, y=y_start)
        y_start += y_increment
        turtles.append(new_turtle)

def move_turtles():
    global winner
    for turtle in turtles:
        fwd_steps = randint(0, 10)
        turtle.forward(fwd_steps)
        current_x_pos = turtle.xcor()
        if current_x_pos >= 230:
            winner = turtle.pencolor()
            return True
    return False


def check_winner(winner_in, user_bet_in):
    if winner_in == user_bet_in:
        print(f"You Win! The {winner_in} is the winner.")
    else:
        print(f"You lose. The {winner_in} is the winner.")
  

#main()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win this race? Enter a color: ")
create_turtles()

is_race_finish = False

while not is_race_finish:
    is_race_finish = move_turtles()

check_winner(winner, user_bet)

screen.exitonclick()
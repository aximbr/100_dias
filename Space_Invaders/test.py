from turtle import Turtle
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
#screen.tracer(0)

screen.addshape(name="monster1_up.gif" )
screen.addshape(name="monster1_down.gif" )

monster = Turtle()
while True:
    monster.clear()
    monster.shape("monster1_up.gif")
    time.sleep(0.5)
    monster.clear()
    monster.shape("monster1_down.gif")

screen.exitonclick()


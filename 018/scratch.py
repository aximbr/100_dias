from turtle import Turtle, Screen
from random import random, choice

tim = Turtle()
tim.color("red")
tim.shape("turtle")

#draw a square 100x100
# for _ in range (4):
#     tim.forward(100)
#     tim.right(90)

#draw a dash line
# def dash_trace(size, step):
#     for x in range (round(size/step)):
#         tim.pendown()
#         tim.forward(step)
#         tim.penup()
#         tim.forward(step)

# dash_trace(70,7)

#draw triangule, ..., decagon
# line_size = 100
# for sides in range (3,11):
#     r = random()
#     g = random()
#     b = random()
#     newcor = (r, g, b)
#     tim.color(newcor)
#     for _ in range(sides):
#         tim.forward(line_size)
#         tim.right(360/sides)

#Random walk
# line_size = 20
# angle =[0, 90, 180, 270]
# tim.hideturtle()
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     r = random()
#     g = random()
#     b = random()
#     newcor = (r, g, b)
#     tim.color(newcor)  
#     x = choice(angle)
#     tim.setheading(x)
#     tim.forward(line_size)

#Draw a spirograph
def set_random_color():
    r = random()
    g = random()
    b = random()
    newcor = (r, g, b)
    return newcor

radius_size = 50
tim.hideturtle()
tim.speed("fastest")

for x in range (0, 360, 10):
        tim.setheading(x)
        tim.circle(radius_size)
        tim.color(set_random_color())
        
        
        
        

screen = Screen()
screen.exitonclick()


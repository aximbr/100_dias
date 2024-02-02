from turtle import Turtle, Screen
from random import random, choice

tim = Turtle()
screen = Screen()
screen.colormode(255)

    
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), 
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), 
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), 
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def set_random_color():
    return choice(color_list)

def draw_dot_line(heading):
    tim.setheading(heading)
    tim.fd(40)
    for _ in range(10):
        tim.color(set_random_color())
        tim.stamp()
        tim.fd(40)
        

def jump_line():
    tim.setheading(90)
    tim.fd(40)
    tim.color(set_random_color())
    tim.stamp
    
    
    

tim.hideturtle
tim.shape("circle")
#tim.dot(20,set_random_color())
tim.speed("fastest")
tim.penup()

tim.setposition(-200.0, -300.0)

for _ in range (5):
    jump_line()
    draw_dot_line(0)
    jump_line()
    draw_dot_line(180)
    





screen.exitonclick()


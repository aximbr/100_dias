from turtle import Turtle
import random

#create a new class Food  that iheritage from superclass Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__() #This call the initialzer from superclass Turtle
        #this ne class knows all methods and atributes from superclass
        self.shape("circle")
        self.penup()
        #make the food a cicle 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

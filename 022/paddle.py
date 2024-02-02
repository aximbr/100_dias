from turtle import Turtle

WIDTH = 20
HEIGHT = 100

Y_POS = 0
MOVE_STEP = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, pos_in):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.goto(pos_in)
        
    
    def up(self):
        if self.ycor() < 210:
            new_y = self.ycor() + MOVE_STEP
            self.goto(self.xcor(), new_y)
     

    def down(self):
        if self.ycor() >  -210:
            new_y = self.ycor() - MOVE_STEP
            self.goto(self.xcor(), new_y)
            
from turtle import Turtle

FONT = ("Courier", 24, "normal")
HEIGHT = 260
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, HEIGHT)
        self.print_level()
        
    def increase_level(self):
        self.level += 1
        self.print_level()


    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font= FONT )

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font= FONT ) 

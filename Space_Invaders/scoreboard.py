from turtle import Turtle

FONT = ("Courier", 24, "normal")
HEIGHT = 260
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-280, HEIGHT)
        self.print_score()
        
    def increase_score(self):
        self.score += 1
        self.print_score()


    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT )

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font= FONT ) 

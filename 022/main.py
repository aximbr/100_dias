#Pong Game
#Create the screen height=600 width=800
#Create and move a paddle (width = 20, height = 100, x_pos = 350, y_pos = 0)
#Create another paddle
#Create the ball and make it move
#Detect when collide with wall and bouce back
#Detect when collide with paddle
#Detect when paddle misses
#TODO:Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600
R_POS = (350, 0)
L_POS = (-350, 0)
BALL_POS = (0, 0)

screen = Screen()
screen.setup(width = WIDTH, height= HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle(R_POS)
paddle_l = Paddle(L_POS)

ball = Ball(BALL_POS)

scoreboard = Scoreboard()
    
screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

is_game_run = True

while is_game_run:
    time.sleep(0.05)
    screen.update()
    ball.move()
    #check if the ball reach the wall (top or bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #check if the ball reach the paddle
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #check if the ball pass a paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score_l()
        time.sleep(0.1)
    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score_r()
        time.sleep(0.1)
    
    
    
screen.exitonclick()

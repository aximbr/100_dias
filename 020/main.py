#TODO: Detect collision with food. Create a new food in random location
#TODO: Create a scoreboard
#TODO: Detect collision with wall
#TODO: Detect collision with tail

from turtle import Screen, Turtle
from snake import Snake
import time
 

    

#Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #turn off tracer


#create snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
        







screen.exitonclick()
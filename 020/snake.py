from turtle import Turtle

START_POSITION = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

        
    def create_snake(self):
        for pos in START_POSITION:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setposition(pos)
            self.segments.append(new_segment)


    def move(self):
        seg_len = len(self.segments)
        for pos in range(seg_len -1, 0, -1):
            new_x = self.segments[pos-1].xcor()
            new_y = self.segments[pos-1].ycor()
            self.segments[pos].goto((new_x, new_y))
        self.head.forward(MOVE_STEP)

    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
     

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


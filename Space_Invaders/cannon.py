from turtle import Turtle

TOP_POSITION = -260
MOVE_DISTANCE = 10
CANNON_START_POSITION = 0
MISSIL_START_POSITION = -250

class Cannon(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cannons = []
        self.missiles = []
        self.cannon_x_pos = CANNON_START_POSITION
        self.create_cannon()
        
        
    def create_cannon(self):
        y = TOP_POSITION
        len_size = 0.5
        for _ in range(3):
            new_segment = Turtle()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.penup()
            new_segment.goto(self.cannon_x_pos, y)
            new_segment.shapesize(stretch_wid=0.5, stretch_len= len_size)
            len_size *= 2
            y -= 10
            self.cannons.append(new_segment)
            
            
    def create_missil(self):
        len_size = 0.1
        new_missil = Turtle()
        new_missil.color("white")
        new_missil.shape("square")
        new_missil.penup()
        new_missil.goto(self.cannon_x_pos, MISSIL_START_POSITION)
        new_missil.shapesize(stretch_wid=0.5, stretch_len= len_size)
        self.missiles.append(new_missil) 
       
    def move_right(self):
        if self.cannons[-1].xcor() < 260:
            for x in self.cannons:
                x.goto(x.xcor() + MOVE_DISTANCE, x.ycor())
            self.cannon_x_pos = self.cannons[0].xcor()
        
    def move_left(self):
        if self.cannons[-1].xcor() > -260:
            for x in self.cannons:
                x.goto(x.xcor() - MOVE_DISTANCE, x.ycor())
            self.cannon_x_pos = self.cannons[0].xcor()
            
            
#FIXME:O último missil para antes de chegar ao final da tela            
    def missil_up(self):
            if len(self.missiles) > 0:
                for m in range(len(self.missiles)):
                    if self.missiles[m].ycor() < 260:
                        self.missiles[m].goto(self.missiles[m].xcor(),  self.missiles[m].ycor() + MOVE_DISTANCE)
                
                for m in range(len(self.missiles)):
                    if self.missiles[m].ycor() >= 260:
                        self.delete_missil(m)       
                        
    def delete_missil(self, missil_to_delete):
        self.missiles[missil_to_delete].ht()
        #del self.missiles[missil_to_delete]  
   
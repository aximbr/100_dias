from turtle import Turtle

BLOCKS = 5
START_ELEMENT_X = -250
START_ELEMENT_Y = -200
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 60
ELEMENT_WIDTH = 5
ELEMENT_HEIGHT = 10
SPACE_BETWEEN_BLOCKS = 30

class Fortress(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.elements = []
        self.create_block()
        
        
    def create_block(self):
        x = START_ELEMENT_X
        y = START_ELEMENT_Y
        x_stretch = ELEMENT_HEIGHT/20
        y_stretch = ELEMENT_WIDTH/20
        
        for _ in range(BLOCKS):
            for y_pos in range(0, BLOCK_HEIGHT, ELEMENT_HEIGHT):
                for x_pos in range(0, BLOCK_WIDTH, ELEMENT_WIDTH):
                    new_element = Turtle()
                    new_element.color("white")
                    new_element.shape("square")
                    new_element.penup()
                    new_element.goto(x_pos + x , y_pos + y)
                    new_element.shapesize(stretch_wid=x_stretch, stretch_len= y_stretch)
                    self.elements.append(new_element)
            x =  x + BLOCK_WIDTH + SPACE_BETWEEN_BLOCKS
            
 
    def delete_element(self, element_to_delete):
        self.elements[element_to_delete].ht()
        del self.elements[element_to_delete]   
        
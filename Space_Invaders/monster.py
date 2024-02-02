from turtle import Turtle
import time

MONSTER_PER_LINE = 5
NUMBER_OF_LINES = 4
START_MONSTER_X = -250
START_MONSTER_Y = 0

SPACE_BETWEEN_LINE = 80
SPACE_BETWEEN_ROW = 80

class Monster(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.monsters = []
        self.create_monster()
        self.direction = "right"
        
        
        
    def create_monster(self):
        y_space = 0
        for _ in range(NUMBER_OF_LINES):
            x_space = 0
            for _ in range(MONSTER_PER_LINE):
                new_monster = Turtle()
                #new_monster.color("white")
                new_monster.penup()
                new_monster.shape("monster1_up.gif")
                new_monster.goto(START_MONSTER_X + x_space, START_MONSTER_Y + y_space)
                self.monsters.append(new_monster)
                x_space += SPACE_BETWEEN_ROW
            y_space += SPACE_BETWEEN_LINE
            
    
    def move_monster_right(self):
        for monster in self.monsters:
            #monster.clear()
            monster.goto(monster.xcor() + 5, monster.ycor())
            if monster.shape() == "monster1_up.gif":
                monster.shape("monster1_down.gif")
            else:
                monster.shape("monster1_up.gif")
    
    
    def move_monster_left(self):
        for monster in self.monsters:
            #monster.clear()
            monster.goto(monster.xcor() - 5, monster.ycor())
            if monster.shape() == "monster1_up.gif":
                monster.shape("monster1_down.gif")
            else:
                monster.shape("monster1_up.gif")       
       
    
    def move_monster(self):
        if len(self.monsters) > 0:     
            if self.direction == "right" and self.right_monster() < 250:
                self.move_monster_right()
            else:
                self.direction = "left"
            if self.direction == "left" and self.left_monster() > -250:
                self.move_monster_left()
            else:
                self.direction = "right"

        
    def delete_monster(self, index_to_delete):
        self.monsters[index_to_delete].ht()
        del self.monsters[index_to_delete]

                
    def right_monster(self):
        current_right = 0
        for index in range(len(self.monsters)):
            if self.monsters[index].xcor() > self.monsters[current_right].xcor():
                current_right = index
        return self.monsters[current_right].xcor()
    
    def left_monster(self):
        current_left = 0
        for index in range(len(self.monsters)):
            if self.monsters[index].xcor() < self.monsters[current_left].xcor():
                current_left = index
        return self.monsters[current_left].xcor()
            
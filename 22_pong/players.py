from turtle import Turtle
P1_STARTING_POSITION = [(-380,20),(-380,0),(-380,-20)]
P2_STARTING_POSITION = [(375,20),(375,0),(375,-20)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20


class P1:
    def __init__(self):
        self.parts = []
        self.create_parts()
        self.main = self.parts[0]
    
    def create_parts(self):
         for position in P1_STARTING_POSITION:
              self.add_part(position)

    def add_part(self,position):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.parts.append(new_square)
    
    def up(self):
            self.main.setheading(UP)
            for part in self.parts[1:]:
                 old_cor_x = self.parts[0].xcor()
                 old_cor_y = part.ycor() 
                 part.goto(old_cor_x, old_cor_y+MOVE_DISTANCE)
            self.main.forward(MOVE_DISTANCE)
    def down(self):
            self.main.setheading(DOWN)
            for part in self.parts[1:]:
                 old_cor_x = self.parts[0].xcor()
                 old_cor_y = part.ycor() 
                 part.goto(old_cor_x, old_cor_y-MOVE_DISTANCE)
            self.main.forward(MOVE_DISTANCE)

class P2:
    def __init__(self):
        self.parts = []
        self.create_parts()
        self.main = self.parts[0]
    
    def create_parts(self):
         for position in P2_STARTING_POSITION:
              self.add_part(position)

    def add_part(self,position):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.parts.append(new_square)
    
    def up(self):
            self.main.setheading(UP)
            for part in self.parts[1:]:
                 old_cor_x = self.parts[0].xcor()
                 old_cor_y = part.ycor() 
                 part.goto(old_cor_x, old_cor_y+MOVE_DISTANCE)
            self.main.forward(MOVE_DISTANCE)
    def down(self):
            self.main.setheading(DOWN)
            for part in self.parts[1:]:
                 old_cor_x = self.parts[0].xcor()
                 old_cor_y = part.ycor() 
                 part.goto(old_cor_x, old_cor_y-MOVE_DISTANCE)
            self.main.forward(MOVE_DISTANCE)



from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.new_level()
        self.setheading(90)
        

    def new_level(self):
        self.goto(STARTING_POSITION)

   
    def move(self):
        self.forward(MOVE_DISTANCE)    
    
    def has_Finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
    
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)

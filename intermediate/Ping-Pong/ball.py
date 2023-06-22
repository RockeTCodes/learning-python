from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.moving_speed = 0.1

    def move(self):
        xcor = self.xcor() + self.xmove
        ycor = self.ycor() + self.ymove
        self.goto(xcor, ycor)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.moving_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.moving_speed = 0.1
        self.bounce_x()

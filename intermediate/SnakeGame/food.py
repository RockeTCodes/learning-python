from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)  # length and width
        self.speed("fastest")
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)

    def reset_food(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)

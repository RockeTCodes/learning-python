from turtle import Turtle, Screen
from time import sleep

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.new_snake()

    def new_snake(self):
        for positions in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(positions)
            self.segments.append(segment)

    def move_snake(self):
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(STEP)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def increase_snake(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.new_snake()
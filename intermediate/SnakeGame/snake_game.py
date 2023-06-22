from turtle import Turtle, Screen
from time import sleep

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []


starting_positions = [(0, 0), (-20, 0), (-40, 0)]


for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)


is_playing = True

while is_playing:
    screen.update()
    sleep(0.1)


screen.exitonclick()

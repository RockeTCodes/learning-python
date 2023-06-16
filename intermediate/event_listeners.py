from turtle import Turtle, Screen

rocket = Turtle()
screen = Screen()

rocket.shape("turtle")


def move_forwards():
    rocket.forward(10)


def turn():
    rocket.right(90)


screen.screensize(400, 400)
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="Up", fun=turn)
screen.exitonclick()

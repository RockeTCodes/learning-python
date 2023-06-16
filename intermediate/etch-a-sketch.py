from turtle import Turtle, Screen

rocket = Turtle()
screen = Screen()


def move_forwards():
    rocket.forward(10)


def move_backwards():
    rocket.backward(10)


def turn_right():
    rocket.right(10)


def turn_left():
    rocket.left(10)


def clear():
    rocket.clear()
    rocket.penup()
    rocket.home()
    rocket.pendown()


screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

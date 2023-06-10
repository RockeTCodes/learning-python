from turtle import Turtle, Screen


# initialising the rocket object from Turtle class
rocket = Turtle()


rocket.shape("turtle")
rocket.color("red")
rocket.forward(300)
rocket.left(90)
rocket.forward(300)
rocket.left(90)
rocket.forward(300)
rocket.left(90)
rocket.forward(300)
rocket.left(90)


my_screen = Screen()
my_screen.exitonclick()

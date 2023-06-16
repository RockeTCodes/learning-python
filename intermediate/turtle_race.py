from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(
    title="Choose your Turtle: ", prompt="Who will win? ")

colors = ["red", "blue", "yellow", "green", "orange"]
allturtles = list()
x = -230
y = -100
for tuttle_index in range(0, 5):
    rocket = Turtle(shape="turtle")
    rocket.color(colors[tuttle_index])
    rocket.penup()
    rocket.goto(x=x, y=y)
    y += 40
    allturtles.append(rocket)


if user_choice:
    start_game = True

while start_game:
    for turtle in allturtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_choice:
                print(f"You have won! The winning turtle is {winner}.")
                start_game = False
            else:
                print(f"You have lost. The winning turtle is {winner}. ")
                start_game = False

        turtle.forward(random.randint(0, 10))


screen.exitonclick()

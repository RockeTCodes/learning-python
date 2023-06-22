from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.new_car()

    def new_car(self):
        if random.randint(1,6) == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(1,2)
            car.penup()
            car.setheading(180)
            car.goto(300,random.randint(-250,250))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
    
    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        
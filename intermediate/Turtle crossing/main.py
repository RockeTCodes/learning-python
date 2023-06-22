import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

level = 1

player = Player()

cars = CarManager()

scoreboard = Scoreboard()




    


screen.listen()
screen.onkey(player.move,"Up")

is_Playing = True
while is_Playing:
    time.sleep(0.1)
    screen.update()
    cars.new_car()
    cars.move_cars()
    for car in cars.cars:
        if car.distance(player) < 20:
            is_Playing = False
            scoreboard.game_over()

    if player.has_Finished():
        player.new_level()
        cars.increase_speed()
        level += 1
        scoreboard.update_scoreboard(level)        
            
    

screen.exitonclick()
from turtle import Screen
from time import sleep
from snake_game_oops import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_Playing = True

while is_Playing:
    screen.update()
    sleep(0.1)
    snake.move_snake()
    if snake.segments[0].distance(food) < 15:
        score_board.inc_score()
        snake.increase_snake()
        food.reset_food()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        is_Playing = False
        score_board.game_over()
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            is_Playing = False
            score_board.game_over()

screen.exitonclick()

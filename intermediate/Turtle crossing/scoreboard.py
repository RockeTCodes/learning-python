from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.update_scoreboard(0)
        

    def update_scoreboard(self,level):
        self.clear()
        self.write(f"Level: {level}",align="left",font=FONT)

    
    def game_over(self):
        self.goto(-0, 0)
        self.write(f"Game Over",align="center",font=FONT)
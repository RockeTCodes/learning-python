from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./intermediate/SnakeGame/data.txt","r") as file:
             self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center" ,font=("Ariel", 24, "normal"))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open ("./intermediate/SnakeGame/data.txt","w") as file:
                file.write(str(self.score))
        self.score = 0     

    
    def inc_score(self):
        self.score += 1
        self.update_score()
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(x=0, y=270)
        self.score=0
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 15, "normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 15, "normal"))

    def gameover(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=("Ariel", 30, "normal"))
        self.goto(x=0, y=-20)
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 15, "normal"))
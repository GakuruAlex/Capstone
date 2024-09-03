from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.display_score()
    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font= FONT)
    def increase_score(self):
        self.level += 1
        self.display_score()

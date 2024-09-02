from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.speed("fast")
        self.penup()
        self.setheading(90)
        self.goto(0, -150)
    
    def move_up(self):
        self.forward(10)
from turtle import Turtle

class Car(Turtle):
    def __init__(self, location, colour, rate):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len= 1, stretch_wid= 0.5)
        self.color(colour)
        self.speed(rate)
        self.penup()
        self.goto(location)

    def move(self, to):
        self.goto(to)
        
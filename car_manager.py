from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.generate_cars()
    def generate_car(self):
        car = Turtle("square")
        car.shapesize(stretch_len=2, stretch_wid=4)
        car.penup()
        car.color(choice(COLORS))
        rand_y = randint(-250, 250)
        car.goto(300, rand_y)
        self.cars.append(car)
    def move_cars(self):
        for car in self.cars:
            car.backwards(STARTING_MOVE_DISTANCE)


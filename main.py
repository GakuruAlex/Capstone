import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()

game_is_on = True
counter = 0
while game_is_on:
    counter += 1
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(player.move, "w")
    car_manager.generate_car()

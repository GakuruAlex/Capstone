from turtle import Screen, Turtle
import time
from random import choice
from car import Car
from player import Player
COLORS = ["red", "yellow", "orange", "green", "blue", "black", "magenta"]
def draw_lanes(turtle, y_cor):
    turtle.pendown()
    turtle.goto(x= 370, y=y_cor)
    turtle.penup()


def main() -> None:
    screen = Screen()
    turtle = Turtle()

    screen.setup(width= 800, height = 400)
    screen.title("Capstone Game")
    screen.bgcolor("white")
    screen.tracer(0)
    turtle.penup()
    turtle.goto(-370, -140)
    turtle.color("black")
    y_cor = turtle.ycor()
    for _ in range(0, 15):
        draw_lanes(turtle, y_cor)
        y_cor += 20
        turtle.goto(-370, y_cor)
    turtle.hideturtle()
    game_is_on = True

    player = Player()
    while game_is_on:
        screen.tracer(0)
        car = Car(location=(370, -130), colour= choice(COLORS), rate="slowest" )
        screen.listen()
        screen.update()
        time.sleep(1)
        screen.onkey(player.move_up, "Up")
        screen.tracer(1)
        car.move((-370, -130))
        if car.xcor() < -350:
            car.clear()
            screen.update()
        if player.ycor() > 140:
            game_is_on = False
            print(player.ycor())




    screen.exitonclick()


if __name__ == "__main__":
    main()
from turtle import Screen, Turtle

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
    turtle.penup()
    turtle.goto(-370, -140)
    turtle.color("black")
    y_cor = turtle.ycor()
    for _ in range(0, 15):
        draw_lanes(turtle, y_cor)
        y_cor += 20
        turtle.goto(-370, y_cor)
    game_is_on = True
    while game_is_on:
        screen.update()



    screen.exitonclick()


if __name__ == "__main__":
    main()
from turtle import Screen, Turtle

def main() -> None:
    screen = Screen()
    turtle = Turtle()
    screen.setup(width= 800, height = 600)
    screen.bgcolor("white")
    screen.tracer(0)
    turtle.color("black")
    turtle.pencolor("black")
    
    
    game_is_on = True
    while game_is_on:
        screen.update()



    screen.exitonclick()


if __name__ == "__main__":
    main()
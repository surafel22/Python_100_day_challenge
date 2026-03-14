from turtle import Turtle, Screen
import  time
tim = Turtle()


def draw():
    side = 2
    return side
gon = draw()

on = True
while on :
    time.sleep(0.01)

    gon += 1
    if gon <= 10:
        for i in range(gon):
            print(gon)
            tim.forward(100)
            tim.right(360/gon)

    else:
        on=False


screen = Screen()
screen.exitonclick()

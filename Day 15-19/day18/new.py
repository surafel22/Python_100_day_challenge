from turtle import Turtle, Screen
import  time
tim = Turtle()
tim.speed("fastest")

# def draw():
#     side = 2
#     side+=1
#     return side


on = True
while on :
    time.sleep(0.01)
    gon = 4

    if gon <= 20:
        for i in range(gon):
            print(gon)
            tim.forward(100)
            tim.right(360/gon)
            gon+=1
    else:
        on=False


screen = Screen()
screen.exitonclick()

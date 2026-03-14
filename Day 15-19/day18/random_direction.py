from turtle import Turtle, Screen
import random as r
tim = Turtle()
tim.speed("fastest")
num = [1,2,3,4,]
def move(where):
    if where == 1:
        tim.forward(10)
    elif where == 2:
        tim.right(90)
        tim.forward(10)
    elif where == 3:
        tim.left(180)
        tim.forward(10)
    else:
        tim.left(90)
        tim.forward(10)
on = True
while on:
    for e in range(1000):
       rand = r.choice(num)
       move(rand)
    on = False


screen = Screen()
screen.exitonclick()
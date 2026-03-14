import turtle as t

tim = t.Turtle()
def move_forward():
    tim.fd(10)
def move_back():
    tim.backward(10)
def turn_left():
    curr = tim.heading() + 10
    tim.setheading(curr)
def turn_right():
    curr = tim.heading() - 10
    tim.setheading(curr)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen = t.Screen()
screen.listen()
screen.onkey(key="w",fun= move_forward)
screen.onkey(key="s",fun= move_back)
screen.onkey(key="d",fun= turn_right)
screen.onkey(key="a",fun= turn_left)
screen.onkey(key="c",fun= clear)

screen.exitonclick()
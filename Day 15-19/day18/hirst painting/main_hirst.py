import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()

color_list = [(203,104,34),(23,123,26),(233,12,123),(67,204,134),(23,123,233),(217,237,109)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_dot = 100
for dot_count in range(1, num_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(40)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(40)
        tim.setheading(180)
        tim.forward(400)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
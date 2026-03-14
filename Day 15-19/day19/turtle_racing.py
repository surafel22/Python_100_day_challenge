import turtle as t
import  random as r
on = False
screen = t.Screen()

screen.setup(width=900, height=400)
user_bet = screen.textinput("Make your bet : ", "Which turtle win the race ; Enter a colour : ")
color_list = ["indigo","blue","green","yellow","red","orange","pink"]
y_list = [-100,-70,-40,-10,20,50,80]
all_turtles = []
for i in range (0,len(color_list)):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(f"{color_list[i]}")
    new_turtle.penup()
    new_turtle.goto(-430, y_list[i])
    all_turtles.append(new_turtle)

if user_bet :
    on = True

while on:
    random_distance = r.randint(0,10)
    for turtle in all_turtles:
        if turtle.xcor() > 430:
            on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! the winner turtle is {winning_turtle}")
            else:
                print(f"You lost! the winner turtle is {winning_turtle}")
        random_distance = r.randint(0, 10)
        turtle.forward(random_distance)






screen.exitonclick()
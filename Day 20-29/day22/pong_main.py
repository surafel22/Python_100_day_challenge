from turtle import Screen
from paddle import Paddle
from pong_ball import Ball
from  score_board import ScoreBoard
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
ball = Ball()
scoreboard = ScoreBoard()

screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.onkey(r_paddle.paddle_up,"i")
screen.onkey(r_paddle.paddle_down,"k")

screen.onkey(l_paddle.paddle_up,"w")
screen.onkey(l_paddle.paddle_down,"s")
pong_on = True
while pong_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        time.sleep(ball.move_speed)
    if ball.xcor() > 380 :
        ball.reset_ball()
        scoreboard.l_point()
    elif ball.xcor() < -380 :
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
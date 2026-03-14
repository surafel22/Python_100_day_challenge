import time
from snake import Snake
from turtle import  Screen
from  food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My First Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score = ScoreBoard()
screen.update()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.count()
        snake.extend_snake()

    if snake.head.xcor() > 285 or snake.head.xcor() < -299 or snake.head.ycor() < -297 or snake.head.ycor() > 297:
        score.reset()
        snake.reset()

    for parts in snake.snake_parts[1:]:

        # if parts == snake.head:
        #     pass
        if snake.head.distance(parts) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")



while True:
    snake.move()
    sc.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            
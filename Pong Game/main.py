from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.title("Pong Game")
sc.bgcolor("black")
sc.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
b = Ball()
sb = Scoreboard()

sc.listen()
sc.onkey(l_paddle.move_up, "w")
sc.onkey(l_paddle.move_down, "s")
sc.onkey(r_paddle.move_up, "Up")
sc.onkey(r_paddle.move_down, "Down")

while True:
    time.sleep(b.speed_value)
    sc.update()
    b.move_up()

    if b.ycor() > 280 or b.ycor() < -290:
        b.bounce_y()

    # Detect collision with paddles
    if (b.distance(l_paddle) < 50 and b.xcor() < -320) or (b.distance(r_paddle) < 50 and b.xcor() > 320):
        b.bounce_x()

    # Detect when right paddle misses
    if b.xcor() > 380:
        b.reset_pos()
        sb.l_point()

    # Detect when left paddle misses
    if b.xcor() < -380:
        b.reset_pos()
        sb.r_point()

sc.exitonclick()

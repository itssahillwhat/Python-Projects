from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.speed_value = 0.1

    def move_up(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed_value *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.speed_value = 0.1
        self.bounce_x()

    def speedup(self):
        self.speed(self.speed_value + 1)
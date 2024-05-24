import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('Hirst Spot.jpg', 25)
color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

t = Turtle()
sc = Screen()
sc.colormode(255)
t.speed('fastest')
t.hideturtle()
t.penup()
t.goto(-250, -250)

for _ in range(10):
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    t.backward(500)
    t.left(90)
    t.forward(50)
    t.right(90)

sc.exitonclick()

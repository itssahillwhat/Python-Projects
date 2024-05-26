from turtle import Turtle, Screen
import random

sc = Screen()
sc.setup(500, 400)

bet = sc.textinput("Turtle Race", "Bet which turtle will win")
y_corr = [0, 40, 80, -40, -80, -120]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
Turtles = []

for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, y_corr[i])
    Turtles.append(t)

condition = True
while condition:
    for t in Turtles:
        if t.xcor() >= 230:
            if bet == t.pencolor():
                print(f"You've won!, {t.pencolor()} is the winner")
            else:
                print(f"You've lose!, {t.pencolor()} is the winner")
            condition = False
        else:
            t.forward(random.randint(0, 10))

sc.exitonclick()
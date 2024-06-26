import turtle
import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

correct_states = []
score = 0

while len(correct_states) < 50:
    ans_state = screen.textinput(title=f"{score}/50 State Correct", prompt="What's another state's name?")

    if ans_state.lower() == "exit":
        missing_states = [state for state in states if state not in correct_states]
        new_data = pd.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    ans_state = ans_state.title()  # Convert to title case
    if ans_state in states:
        score += 1
        correct_states.append(ans_state)
        state_data = data[data.state == ans_state]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans_state)


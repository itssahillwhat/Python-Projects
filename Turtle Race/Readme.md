# Turtle Race

This mini project simulates a turtle race using Python's `turtle` graphics module. Users can place bets on which turtle they think will win the race. The race involves multiple turtles moving randomly across the screen, and the first turtle to reach the finish line wins.

## Requirements

- Python 3.x
- `turtle` module (included with Python's standard library)

## How to Run

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/itssahillwhat/Python-Projects/Turtle Race.git
   cd Turtle Race
   ```

2. **Run the Script:**

   ```sh
   python main.py
   ```

3. **Place Your Bet:**

   - A dialog box will appear asking you to enter the color of the turtle you want to bet on. Choose from the following colors: `red`, `orange`, `yellow`, `green`, `blue`, `violet`.

4. **Watch the Race:**

   - The turtles will start racing towards the right side of the screen. The first turtle to reach the end of the screen (x-coordinate ≥ 230) is the winner.
   - A message will be displayed in the console indicating whether you won or lost the bet based on the color of the winning turtle.

## Code Explanation

### Setup Screen

```python
sc = Screen()
sc.setup(500, 400)
```

- Initializes the screen with a width of 500 pixels and a height of 400 pixels.

### User Bet

```python
bet = sc.textinput("Turtle Race", "Bet which turtle will win")
```

- Prompts the user to input their bet on which turtle will win the race.

### Initialize Turtles

```python
y_corr = [0, 40, 80, -40, -80, -120]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
Turtles = []

for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, y_corr[i])
    Turtles.append(t)
```

- Creates six turtles with different colors.
- Positions the turtles at the starting line with different y-coordinates.

### Start Race

```python
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
```

- The race continues in a loop until one of the turtles crosses the finish line (x-coordinate ≥ 230).
- Each turtle moves a random distance between 0 and 10 units in each iteration.
- When a turtle wins, the program checks if the winning turtle's color matches the user's bet and displays the appropriate message.

### Close Screen

```python
sc.exitonclick()
```

- Keeps the screen open until the user clicks on it, allowing them to see the final result of the race.

## Customization

You can customize the turtle race by modifying the following parameters:
- **Turtle Colors:** Change the `colors` list to include different colors.
- **Starting Positions:** Adjust the `y_corr` list to change the starting y-coordinates of the turtles.
- **Race Distance:** Modify the condition in the while loop to change the finish line's x-coordinate.

Enjoy your turtle race game!

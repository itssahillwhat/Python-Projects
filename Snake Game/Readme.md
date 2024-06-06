# Snake Game
Snake Game is a classic arcade game built using Python's Turtle module. In this game, players control a snake that grows in length as it consumes food while avoiding collisions with walls and its own body.

## Screenshot
<img src="Output.png" alt="Output Screenshot"/>

## Requirements

- Python 3.x
- `turtle` module (included with Python's standard library)

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/itssahillwhat/Python-Projects.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Snake Game
    ```
3. Run the game:
    ```bash
    python main.py
    ```
## Notes
* **Controls:** Use the arrow keys (Up, Down, Left, Right) to control the direction of the snake.
* **Gameplay Mechanics:**
  * The snake moves continuously in the direction it is facing.
  * The aim is to eat the food (green circles) that appear on the screen to grow the snake.
  * Avoid running into walls or the snake's own body, as this will end the game.
  * The game ends when the snake collides with a wall or itself.
  * The score is displayed at the top of the game window.
  * The highest score achieved is stored and updated in the `data.txt` file.
* **Customization Options:** You can customize the game by modifying the script, such as changing the snake's speed, color, or the appearance of the food.
* **Saving High Score:** The high score is saved in a file named `data.txt`. Ensure this file is in the same directory as the script to properly track and update the high score.


## Helpful Links

* [The tracer method](https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer)

* [The shape and shapesize methods](https://docs.python.org/3/library/turtle.html#turtle.shape)

* [The write method](https://docs.python.org/3/library/turtle.html#turtle.write)

## Contributing
Contributions to this project are welcome! Here are some ways you can contribute:

* Report bugs or suggest new features by opening an issue.
* Fork the repository, make your changes, and submit a pull request.

Please make sure to update tests as appropriate and follow the existing code style.

Enjoy creating your Snake Game!

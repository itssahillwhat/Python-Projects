# U.S. States Game

This project is a U.S. States guessing game built with Python using the Turtle graphics library and Pandas for data handling. The game displays a blank U.S. map and prompts the user to enter the names of U.S. states. Correct guesses are displayed on the map, and the game continues until the user names all 50 states or exits.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/itssahillwhat/Python-Projects.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Us States Game
    ```

3. Install the required packages:
    ```bash
    pip install pandas turtle
    ```

4. Ensure you have the `blank_states_img.gif` and `50_states.csv` files in the project directory.

## Usage

Run the game using the following command:
```bash
python main.py
```

## Game Instructions
1. A window will appear with a blank U.S. map.
2. You will be prompted to enter the name of a U.S. state.
3. If the state name is correct, it will be displayed on the map at its corresponding location.
4. The game continues until you have named all 50 states or type "exit" to quit the game.
5. If you quit the game, a states_to_learn.csv file will be created with the states you did not guess.


## Features
* Interactive map with real-time state name entry.
* Keeps track of correct guesses and displays them on the map.
* Generates a CSV file of states to learn if the user exits before guessing all states.


## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
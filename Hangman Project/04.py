import random
import sys

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ["_" for _ in range(word_length)]

while chosen_word != "".join(display) and lives > 0:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(stages[lives])
            sys.exit("You Lose")

    # Update display
    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

# Check if the user has won or lost
if "_" not in display:
    print("You win.")
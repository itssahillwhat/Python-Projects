#Step 5

import random, words, art, sys

print(art.logo)

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while chosen_word != "".join(display) and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed the letter '{guess}'. Try again.")
        continue
    # Check guessed letter
    if guess not in chosen_word:
        print(f"{guess} is not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            print(art.stages[lives])
            sys.exit("You Lose")

    # Update display
    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(art.stages[lives])

# Check if the user has won or lost
if "_" not in display:
    print("You win.")
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
#print(f"Pssst, the correct answer is {number}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "hard":
    attempt = 5
else:
    attempt = 10

for _ in range(attempt):
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess : "))
    if guess > number:
        print("Too high\nGuess again")
    elif guess < number:
        if attempt == 1:
            print("Too low.\nYou've run out of guesses, you lose.")
        else:
            print("Too low\nGuess again")
    else:
        print(f"You got it, The answer was{number}")
        break
    attempt -= 1
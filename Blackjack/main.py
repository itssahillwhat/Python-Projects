from art import logo
import random
import os
import sys


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    elif os.name == 'nt':
        _ = os.system('cls')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You lose 😭"
    elif computer_score > 21:
        return "You win 😁"
    elif user_score > computer_score:
        return "You Win 😃"
    else:
        return "You lose 😤"


def blackjack():
    while True:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ") != "y":
            sys.exit(0)

        clear_screen()
        print(logo)

        user = [random.choice(cards) for _ in range(2)]
        computer = [random.choice(cards)]

        while True:
            print(f"Your cards {user}, current score: {sum(user)}")
            print(f"Computer's first card: {computer}")

            if input("Type 'y' to get another card, type 'n' to pass: ") != "y":
                break

            user.append(random.choice(cards))

        while sum(computer) != 0 and sum(computer) < 17:
            computer.append(random.choice(cards))

        print(f"Your final hand: {user}, final score: {sum(user)}")
        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")

        result = compare(sum(user), sum(computer))
        print(result)


blackjack()
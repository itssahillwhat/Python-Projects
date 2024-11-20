import random
from game_data import data
from art import logo, vs

print(logo)

def higher_lower(score):
    A = random.choice(data)
    B = random.choice(data)

    while True:
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")

        print(vs)

        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

        user = input("Who has more followers? Type 'A' or 'B': ")

        if user == "A":
            if A['follower_count'] > B['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                break
        else:
            if B['follower_count'] > A['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                break

        A = B
        B = random.choice(data)

        while A == B:
            B = random.choice(data)

score = 0
higher_lower(score)
import os
import platform
import art

def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.")
auction = []

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))  # Convert bid to integer for numerical comparison

    bidder = {
        "name": name,
        "bid": bid,
    }
    auction.append(bidder)

    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if other_bidder.lower() == "yes":
        clear_console()
    else:
        max_bid = 0
        winner = ""

        for item in auction:
            if item["bid"] > max_bid:
                max_bid = item["bid"]
                winner = item["name"]

        # Print the winner
        print(f"The winner is {winner} with a bid of ${max_bid}")
        break

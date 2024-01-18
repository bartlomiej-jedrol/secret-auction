import os

bids = {}
should_run = True

# Adds bider to the bids dictionary.
def add_bider(bider_name, bider_value):
    bids[bider_name] = bider_value

# Clear console for a new bider.            
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

# Chooses winner with the highest bid.
def choose_winner(bids_dict):
    winner_name = "No winner"
    winner_bid = 0

    for bider in bids_dict:
        if bids_dict[bider] > winner_bid:
            winner_name = bider
            winner_bid = bids[bider]
    
    print(f"The winner is {winner_name} with a bid of ${winner_bid}!")

# Collecting inputs from users until they want to continue.
while should_run == True:
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's is your bid?: $"))
    
    add_bider(name, bid)
    
    other_bids = input("Are there any other bids? Type 'yes' or 'no'.\n").lower()
    if other_bids == "yes":
        clear_console()
    elif other_bids == "no":
        should_run = False
        choose_winner(bids)



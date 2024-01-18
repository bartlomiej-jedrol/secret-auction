import os

biders = []
should_run = True
winner_name = ""

def add_bider(bider_name, bider_value):
    biders.append(
        {
            "name": bider_name,
            "bid": bider_value,
        }
    )
            
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def choose_winner(biders_list):
    print(biders_list)
    # winner_name = ""
    winner_bid = 0

    for bider in biders_list:
        if bider["bid"] > winner_bid:
            winner_name = bider["name"]
            winner_bid = bider["bid"]
    
    print(f"The winner is ... with a bid of ${winner_bid}!")

while should_run == True:
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's is your bid?: $"))
    
    add_bider(name, bid)
    
    other_biders = input("Are there any other biders? Type 'yes' or 'no'.\n").lower()
    if other_biders == "yes":
        clear_console()
    else:
        should_run = False

choose_winner(biders)








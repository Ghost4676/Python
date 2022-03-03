import click
from art import logo1
def cls():
    click.clear()
# print(logo1)

bid_data={}

def highest_bidder(bidding):
    highest_bid = 0
    winner = ""
    for bidder in bidding:
        bidss = bidding[bidder]
        if bidss > highest_bid:
            highest_bid = bidss
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")



condition = True
while condition:
    name = input("Whats your name ? ")
    bid = int(input("Whats your bid price ? $"))
    bid_data[name] = bid
    other_users = input("Anyone else who wants to bid? ").lower()
    if other_users == "no":
        highest_bidder(bid_data)
        condition = False
    # else:
    #     click.clear()    



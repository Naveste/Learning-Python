import os

bidders = {}
active = True

while active:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    bidders[name] = bid #store key and value from user input in the empty dictionary, bidders.
    print("bidders:",bidders)
    other_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if other_bid == 'yes':
        os.system('cls')
        active = True
    if other_bid == 'no':
        active = False

highest_bidder = max(bidders, key=bidders.get).title() #get bidder with highest value.
#print("highest_bidder:",highest_bidder)

all_values = bidders.values() #display all values.
#print("\nall_values:",all_values)

highest_bid = max(all_values) #display highest value.
#print("\nhighest_bid:",highest_bid)

print(f"\nThe winner is {highest_bidder} with a bid of ${highest_bid}.")
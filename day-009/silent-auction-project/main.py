from art import logo

print(logo)

bidding_dict = {}
auction_is_active = True

while auction_is_active:
    name = input("Please enter your name?: ")
    price = int(input("How much would you like to bid? $"))
    bidding_dict[name] = price
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if more_bidders == "no":
        winner = max(bidding_dict, key= lambda x: bidding_dict[x])
        print(f"The winner is {winner} with a bid of ${bidding_dict[winner]}!")
        auction_is_active = False
    else:
        print("\n" * 20)
        

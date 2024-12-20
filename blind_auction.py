import art

print("Welcome to the secret auction program.")
print(art.logo)
# sample_bidders = {
#     "John": 100,
#     "Jane": 200,
#     "Jack": 300,
#     "deepak": 400,
#     "nims": 56569
# }
def bid_winner(bidders):
    max = 0
    winner = ""
    for key in bidders:
        if bidders[key] > max:
            max = bidders[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${max}")
# name = input("what is your name? : ")
bidders = {}
# bid = int(input("What is your bid? : $"))

# should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
# print("\n" * 100)
continue_bidding = True
while continue_bidding: 
    name = input("what is your name? : ")
    bid = int(input("What is your bid? : $"))
    bidders[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':  ").lower()
    print("\n" * 90)
    if should_continue == "no":
        continue_bidding = False
    elif should_continue == "yes":
        continue_bidding = True

print(bidders)


    # print(bidders)
bid_winner(bidders)
# bid_winner(sample_bidders)

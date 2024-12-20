print("Welcome to the secret auction program.")
bidders = {}
sample_bidders = {
    "John": 100,
    "Jane": 200,
    "Jack": 300,
    "deepak": 400,
    "nims": 56569
}

name = input("what is your name? : ")

bid = int(input("What is your bid? : $"))

should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
print("\n" * 100)
while should_continue == "yes":
    bidders[name] = bid
    name = input("what is your name? : ")
    bid = int(input("What is your bid? : $"))
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':  ").lower()
    print("\n" * 90)
print(bidders)

def bid_winner(bidders):
    max = 0
    winner = ""
    for key in bidders:
        if bidders[key] > max:
            max = bidders[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${max}")
    print(bidders)
bid_winner(bidders)
bid_winner(sample_bidders)
input()
from art import logo
player={}
more_players = "yes"

print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name? :")
bid = int(input("What is your bid? $"))
more_players = input("Are there any bidders? Type 'yes' or 'no' :")
player[name]=bid
highest_bid = bid
highest_bidder = name

while(more_players == "yes"):
	name = input("What is your name? :")
	bid = int(input("What is your bid? $"))
	more_players = input("Are there any bidders? Type 'yes' or 'no' :")
	player[name] = bid
	if(highest_bid <bid):
		highest_bid = bid
		highest_bidder = name

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

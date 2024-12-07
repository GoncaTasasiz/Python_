import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')    

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]    
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name : \n")
    bid_price = int(input("What is your bid price? : \n"))
    
    bids[name] = bid_price
    other_users = input("IS there any other user? Type 'Yes' or 'No': \n").lower()
    if other_users == "yes":
        clear()
    elif other_users == "no":
        clear()
        bidding_finished = True
        find_highest_bidder(bids)
    
   

bids = {}
finished = False
def high(record):
    highest = 0
    winner=""
    for name in record:
        amount = record[name]
        if amount > highest:
            highest = amount
            winner = name #cuz name  is a key which is a name
    print(f"the winner is {winner} with amount of {highest}$")
while not finished:
    name = input("what is your name ?")
    price = float(input("what is ur bid price $"))
    bids[name]=price
    is_finished = input("is there another bidder choose yes or no : ").lower()
    if is_finished=="no":
        finished=True
        high(bids)
    else:
        print("invalid response")

bids = {}
finished = False
def high(record):
    highest = 0
    winner=""
    for j in record:
        
        amount = record[j]
        if amount>highest:
            highest = amount
            winner = j #cuz j  is a key which is a name
    print(f"the winner is {winner} with amount of {highest}")
while not finished:
    name = input("what is your name ?")
    price = float(input("what is ur bid price $"))
    bids[name]=price
    is_finished = input("is there another bidder choose yes or no").lower()
    if is_finished=="no":
        finished=True
        high(bids)
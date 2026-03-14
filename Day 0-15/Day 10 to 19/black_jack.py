import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    """"return a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """take list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score == computer_score:
        return "the match is draw "
    elif computer_score == 0:
        return "the dealer wins the match "
    elif user_score == 0:
        return "the player wins the match "
    elif user_score > 21 :
        return "you lost the match "
    elif computer_score > 21 :
        return "you win the game "
    elif user_score > computer_score:
        return "you win "
    else :
        return "you lose "
def play_game():
    
    user_card = []
    computer_cards = []
    is_game_over = False



    for _ in range(2):
        user_card.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_cards)
        print(f"ur cards {user_card},current score {user_score}")
        print(f" computer's first card : {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("do u wnat to draw another card choose y for drawing or n for to pass : ").lower()
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card)
        computer_score = calculate_score(computer_cards)
    print(f"ur final hand : {user_card} , final score : {user_score}")
    print(f"computer's final hand : {computer_cards}, final score : {computer_score} ")
    print(compare(user_score,computer_score))
    
   
while input("do u want to play again choose y or n ").lower()=='y':
   play_game()
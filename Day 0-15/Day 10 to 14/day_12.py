import random 

secret_num = random.randint(1,100)
attempt = 0
make_guess = int(input("make ur guess"))

# def compare():
#     att = 0 
#     if secret_num == guessing:
#         return "yeeeeehooooo u win "
#     elif secret_num < guessing:
        
#         return "too high "
#     elif secret_num > guessing:
        
#         return "too low "
def diff(make_guess):
    global attempt
    if difficulty == 'easy':
        attempt = 10
        print( f"you have {attempt} attempt")
        if secret_num == make_guess:
            return "yeeeeehooooo u win "
        elif secret_num < make_guess:
            attempt-=1
            print ("too high ")
            if attempt==0:
                return "u lose"
        elif secret_num > make_guess:
            attempt-=1
            print( "too low ")
            if attempt==0:
                return "u lose"
    elif difficulty == 'hard':
        attempt = 5
        print(f"you have {attempt} attempt")
        if secret_num == make_guess:
            return "yeeeeehooooo u win "
        elif secret_num < make_guess:
            attempt-=1
            print( "too high ")
            if attempt==0:
                return "u lose"
        elif secret_num > make_guess:
            attempt-=1
            print ("too low ")
            if attempt==0:
                return "u lose"
    else:
        return "invalid input choose easy or hard"

print (secret_num)


print("I am thinking a number between 1 to 100 ")
difficulty = input("choose diffiulty : 'easy' or 'hard' : ").lower()

    

diff(make_guess)



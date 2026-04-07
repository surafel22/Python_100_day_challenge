import random
secret_num = random.randint(1,100)
def random_chooser():
    
    return secret_num
# print("I am thinking a number between 1 to 100")
difficulty = input("choose diffiulty : 'easy' or 'hard'").lower()
def guess():
    make_guess = int(input("make ur guess"))
    if difficulty == 'easy':
        attempts = 10
       # print(f"u have {attempts} attempt/s")
        if secret_num == make_guess:
            return "yeeeeehoooo u nail it"
        else:
            if secret_num < make_guess:
                print("too high")
                new = attempts-1
            else :
                print("too low")
                new = attempts-1
            print(f"u have {new} attempts left")
    if new == 0 :
        return "u lose the game"
    print(attempts)
    print(new)
print(secret_num)

while input("do u wnat to play number guessing game y or n") == 'y':
    guess()



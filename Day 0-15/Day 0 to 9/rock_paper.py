import random
print("Welcome to Rock, paper, scissor game!")
game = True
while game:
    palyer = int(input("Which one do you chose? 0 for rock, 1 for paper and 2 for scissors."))
    comp = random.randint(0,2)
    if (comp == palyer):
        print("Tie!")
    else:
        if(palyer==0 and comp== 2):
            print(f"you won!")
        elif(palyer==0 and comp==1):
            print("You lost!")
        elif(palyer==1 and comp==0):
            print("you won! ")
        elif(palyer==1 and comp==2):
            print("you lost! ")
        elif(palyer==2 and comp==0):
            print("you lose! ")
        elif(palyer==2 and comp==1):
            print("you won! ")
        q = input("Enter 0 to Quit")
        if (q =="0"):
            game = False

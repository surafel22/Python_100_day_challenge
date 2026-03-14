print("welcome to treasure finding game ")
path = input("which path do you want to take left or right")

if path == "right":
    print("lost to the jungle muhehe")
elif path == "left":
   lake = input("you reach at a lake choose wait or swim")
else:
    print("invalid")

if lake == "wait":
    door = input("you found three doors choose green yellow or red")
elif lake == "swim":
    print("you are eaten by a shark")
else:
    print("invalid choose")

if door == "red":
    print("yeeeeeeehoooooooo you win you found it")
elif door == "global":
    print("You are swallowed by long grasses")
elif door == "yellow":
    print("you enter into an eternal doom")
else:
    print("invalid response")
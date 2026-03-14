import random
name_str = input("Enter a name separated by comma to pick meal buyer \n ")
name = name_str.split(", ") 
#print(name[random.randint(0,len(name)-1)])
print(random.choice(name) + " will buy")
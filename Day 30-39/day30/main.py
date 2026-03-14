# try :
#     file = open("file.txt")
#     dictionary = {"key":"value"}
#     print(dictionary["k"])
# except FileNotFoundError:
#     fiel = open("file.txt","w")
#     fiel.write("key")
#     print("File Not Found")
# except KeyError as k :
#     print(f"Key {k} Not Found")

fruits = ["apple", "banana", "cherry"]

def makepie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + "pie")

makepie(4)
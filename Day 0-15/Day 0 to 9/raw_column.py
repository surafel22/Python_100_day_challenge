row_1 = ["⬛","⬛","⬛"]
row_2 = ["⬛","⬛","⬛"]
row_3 = ["⬛","⬛","⬛"]

map = [row_1,row_2,row_3]
print(f"{row_1}\n{row_2}\n{row_3}") 
position = input("where do you want to put the treasure ")
hori = int(position[0])
ver = int(position[1])
selected_row = map[ver-1]
selected_row[hori-1] = "X"
print(f"{row_1}\n{row_2}\n{row_3}")

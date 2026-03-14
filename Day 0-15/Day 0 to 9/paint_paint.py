import math
def area_of_wall(height,width):
    area = width * height
    print(f"your wall area is {area} sq meters")
    num = math.ceil(area/5)
    print(f"u need to have {num}cans of paints for ur wall")

    

area_of_wall(height=float(input("how much is ur wall height")),width=float(input("how much is ur wall width")))

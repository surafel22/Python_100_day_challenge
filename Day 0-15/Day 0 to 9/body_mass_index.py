print("Body mass index calculator")
height = float(input("Enter your height in centi meter = "))
weight = float(input("Enter your weight in kg = "))
body_mass_index = weight / (height / 100) ** 2
bmi = "{:.2f}".format(body_mass_index)

if body_mass_index < 18.5 :
    print("you're under weight")
elif 25 > body_mass_index >= 18.5 :
    print("You are normal weight")
elif 30 > body_mass_index >= 25:
    print("You are over weight")
elif body_mass_index >= 30:
    print("You are obese")
    
print(type(bmi))

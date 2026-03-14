print("Welcome to the tip calculator ")
bill = float(input("What was the total bill $"))
tip = int(input("How much tip you would like to give 10 ,12 ,15 "))
people = int(input("How much people to split the bill with "))
total = bill * (1 + tip / 100)
bill_per_person = total / people
#final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"each person should pay $ {final_amount}")


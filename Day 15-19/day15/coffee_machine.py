MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO : 1. print all resource available
def calculator():
    print("please insert coins ")
    quarters = int(input("How many quarters : "))
    dimes = int(input("How many dimes : "))
    nickles = int(input("How many nickles : "))
    pennies = int(input("How many pennies : "))
    total_dollar = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if choosen_word == "espresso":
        espresso = MENU["espresso"]
        if total_dollar < espresso["cost"] :
            print("Sorry, you don't have enough money")
        elif total_dollar > espresso["cost"]  :
            print("Sure here is ur ☕ coffee enjoy !")
            print(f"Take ur change {total_dollar - espresso["cost"]} dollars ")
        else:
            print("Sure here is ur ☕ coffee enjoy !")
    if choosen_word == "cappuccino":
        cappucino = MENU["cappuccino"]
        if total_dollar < cappucino["cost"] :
            print("Sorry, you don't have enough money")
        elif total_dollar > cappucino["cost"] :
            print("Sure here is ur ☕ coffee enjoy !")
            print(f"Take ur change {total_dollar - cappucino["cost"]} dollars ")
        else:
            print("Sure here is ur ☕ coffee enjoy !")
    if choosen_word == "latte":
        latte = MENU["latte"]
        if total_dollar < latte["cost"] :
            print("Sorry, you don't have enough money")
        elif total_dollar > latte["cost"] :
            print("Sure here is ur ☕ coffee enjoy !")
            print(f"Take ur change {total_dollar - latte["cost"]} dollars ")
        else:
            print("Sure here is ur ☕ coffee enjoy !")

def resource_manager():
    if choosen_word == "espresso":
        espresso = MENU["espresso"]["ingredients"]
        resources["water"] -= espresso["water"]
       # resources["milk"] -= espresso["milk"]
        resources["coffee"] -= espresso["coffee"]
    if choosen_word == "cappuccino":
        cappuccino = MENU["cappuccino"]["ingredients"]
        resources["water"] -= cappuccino["water"]
        resources["coffee"] -= cappuccino["coffee"]
        resources["milk"] -= cappuccino["milk"]
    if choosen_word == "latte":
        latte = MENU["latte"]["ingredients"]
        resources["water"] -= latte["water"]
        resources["coffee"] -= latte["coffee"]
        resources["milk"] -= latte["milk"]

again = True
while again :
    choosen_word = input("What would you like? (espresso/latte/cappuccino): ").lower()






    if choosen_word == "report":
        print(f"water {resources["water"]} ml"
              f"\ncoffee {resources["coffee"]} ml"
              f"\nmilk {resources["milk"]} ml")
    elif choosen_word == "espresso":
        espresso = MENU["espresso"]["ingredients"]
        if espresso["water"] > resources["water"] or espresso["coffee"] > resources["coffee"]:
            print("Sorry, not enough resources ")
    elif choosen_word == "cappuccino":
        cappuccino = MENU["cappuccino"]["ingredients"]
        if cappuccino["water"] > resources["water"] or cappuccino["coffee"] > resources["coffee"] or cappuccino["milk"] > resources["milk"]:
            print("Sorry, not enough resources ")
    elif choosen_word == "latte":
        latte = MENU["latte"]["ingredients"]
        if latte["water"] > resources["water"] or latte["milk"] > resources["milk"] or latte["coffee"] > resources["coffee"]:
            print("Sorry, not enough resources ")
    elif choosen_word == "off":
        again = False
    calculator()
    resource_manager()


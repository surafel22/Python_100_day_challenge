from menu import Menu , MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

is_machine_on = True

while is_machine_on:
    order_item = input(f"What would you like? ({coffee_menu.get_items()}): ")
    if order_item == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_item == "off":
        is_machine_on = False
    elif coffee_maker.is_resource_sufficient(coffee_menu.find_drink(order_item)):

        if money_machine.make_payment(coffee_menu.find_drink(order_item).cost):

            coffee_maker.make_coffee(coffee_menu.find_drink(order_item))













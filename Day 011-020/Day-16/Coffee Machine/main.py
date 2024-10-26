from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu, coffee_maker, money_machine = Menu(), CoffeeMaker(), MoneyMachine()

while True:
    user = input(f"What do you want ({menu.get_items()}): ")
    if user == "nothing":
        break
    elif user == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

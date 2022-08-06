from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    choices = menu.get_items()
    
    user_input = input(f"What would you like? ({choices}): ")

    if user_input == 'off':
        break

    elif user_input == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
#det här skitet behöver göras om helt.

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

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

money = 0


while True:
    
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'off':
        break

    elif user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: ${'{:.2f}'.format(money)}")
    
    elif resources['water'] >= MENU[user_input]['ingredients']['water']:
        if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            print("Please insert coins.")
            pennys = int(input("How many pennys?: "))
            pennys = penny * pennys

            nickels = int(input("How many nickles?: "))
            nickels = nickel * nickels

            dimes = int(input("How many dimes?: "))
            dimes = dime * dimes

            quarters = int(input("How many quarters?: "))
            quarters = quarter * quarters

            total = pennys + nickels + dimes + quarters
            money += total

            print(f"${'{:.2f}'.format(total)}")
            print(f"${'{:.2f}'.format(money)}")

        coffee_cost = MENU[user_input]['cost']
        change = round(total - coffee_cost, 2)

        if money >= coffee_cost:
            if resources['water'] >= MENU[user_input]['ingredients']['water'] and resources['coffee'] >= MENU[user_input]['ingredients']['coffee']:
                if user_input == 'latte' or user_input == 'cappuccino':
                    money -= coffee_cost
                    resources['water'] -= MENU[user_input]['ingredients']['water']
                    resources['milk'] -= MENU[user_input]['ingredients']['milk']
                    resources["coffee"] -= MENU[user_input]['ingredients']['coffee']
                
                elif user_input == 'espresso':
                    money -= coffee_cost
                    resources['water'] -= MENU[user_input]['ingredients']['water']
                    resources['coffee'] -= MENU[user_input]['ingredients']['coffee']
                    
                money = total - change
                change_1 = total - money
                money = total - change_1
                print("debug",money)
                print(f"Here is ${change_1} in change.")
                print(f"Here is your {user_input}.")
            else:
                print("Not enough ingredients.")
        else:
            money = total - money
            print("Not enough money. Refunded.")
    else:
        print("Sorry. Not enough resources.")
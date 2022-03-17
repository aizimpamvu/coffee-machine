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


# TODO 4: Check resources sufficient?
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be mafe, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


# TODO 5: Process coins.
def process_coin():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins:")
    total = int(input("How many quarters:")) * 0.25
    total += int(input("How many dimes:")) * 0.1
    total += int(input("How many nickles:")) * 0.05
    total += int(input("How many pennies:")) * 0.01
    return total


# TODO 6: Check transaction successful?

def is_transaction_sucessful(money_received, drink_cost):
    """Return True when the payment is accepted. or False if Money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 7: Make Coffee
def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} 🍵 Enjoy")


profit = 0
is_machine_on = True
# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):
while is_machine_on:
    user_choice = input("Prompt user by asking “What would you like? (espresso/latte/cappuccino):").lower()

    # if user_choice=="espresso" :
    #     if re
    # elif user_choice=="latte":
    #     #choice
    # elif user_choice=="cappuccino":
    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
    if user_choice == "off":
        is_machine_on = False
        print("Machine is turned off bye!!!")
    # TODO 3: Print report.
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_choice == "latte" or user_choice == "capuccino" or user_choice == "espresso":
        drink = MENU[user_choice]
        is_resource_sufficient(drink["ingredients"])
        payment = process_coin()
        if is_transaction_sucessful(payment, drink["cost"]):
            make_coffe(user_choice, drink["ingredients"])
    else:
        print("We don't have that on menu, try again!!")

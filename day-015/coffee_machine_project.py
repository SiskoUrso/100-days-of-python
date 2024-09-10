
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

coffee_machine_power = True 

profit = 0

def coin():
    """
    Asks the user to input the number of coins they want to insert.
    
    Returns:
        tuple: A tuple of four integers, representing the number of quarters, dimes, nickles and pennies inserted.
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return quarters, dimes, nickles, pennies

def coin_processor(quarters, dimes, nickels, pennies):
    """
    Process the coins inserted by the user.
    
    Parameters:
    quarters (int): The number of quarters inserted.
    dimes (int): The number of dimes inserted.
    nickels (int): The number of nickels inserted.
    pennies (int): The number of pennies inserted.
    
    Returns:
        float: The total amount of money inserted, or False if the money is not enough.
    """
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if total < MENU[user_input]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - MENU[user_input]["cost"], 2)
        print(f"Here is ${change} in change.")
    return total

def resource_check(order_ingredients):
    """
    Check if there are enough resources to make the drink.

    Parameters:
    order_ingredients (dict): A dictionary of ingredients and their quantities.

    Returns:
        bool: True if there are enough resources, False otherwise.
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    """
    Make the coffee and update the resources and profit.

    Parameters:
    drink_name (str): The name of the drink to make.
    order_ingredients (dict): A dictionary of ingredients and their quantities.

    Returns:
        None
    """
    global profit
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    profit += MENU[drink_name]["cost"]

while coffee_machine_power:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit: .2f}")

    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if resource_check(MENU[user_input]["ingredients"]):
            print(f"The cost is ${MENU[user_input]['cost']: .2f}.")
            coins = coin()
            user_coins = coin_processor(coins[0], coins[1], coins[2], coins[3])
            if user_coins:
                if user_coins >= MENU[user_input]["cost"]:
                    make_coffee(user_input, MENU[user_input]["ingredients"])
    elif user_input == "off":
        print(f"Powering off. Money earned: ${profit: .2f}.")
        coffee_machine_power = False


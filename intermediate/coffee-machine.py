from os import name, system

drinks = [{"name": "espresso☕", "price": 2.5, "water": 100, "milk": 100, "coffee": 100}, {
    "name": "latte☕", "price": 3.75, "water": 100, "milk": 100, "coffee": 100}, {"name": "cappuccino☕", "price": 4.15, "water": 100, "milk": 100, "coffee": 100}]

available_resources = {"water": 500, "milk": 400, "coffee": 400, "money": 0}


def ask_money():
    quaters = float(input("No. of quaters. : "))*0.25
    dimes = float(input("No. of dimes. : "))*0.10
    nickles = float(input("No. of nickles. : "))*0.05
    pennies = float(input("No. of pennis. : "))*0.01
    return quaters + dimes + nickles + pennies


def check_money(money_given, drink):
    if money_given >= drinks[drink]["price"]:
        return True
    else:
        return False


def calculate_change(money_given, drink):
    return money_given - drinks[drink]["price"]


def check_resources(drink, available_resources):
    water = drinks[drink]["water"]
    milk = drinks[drink]["milk"]
    coffee = drinks[drink]["coffee"]
    if available_resources["water"] >= water and available_resources["milk"] >= milk and available_resources["coffee"] >= coffee:
        return True
    else:
        return False


def use_resources(drink, available_resources):
    available_resources["water"] -= drinks[drink]["water"]
    available_resources["milk"] -= drinks[drink]["milk"]
    available_resources["coffee"] -= drinks[drink]["coffee"]
    available_resources["money"] += drinks[drink]["price"]


def check_scarce_resource(drink, available_resources):
    if available_resources["water"] < drinks[drink]["water"]:
        print("Not enough water.Money Refunded.")
    elif available_resources["milk"] < drinks[drink]["milk"]:
        print("Not enough milk.Money Refunded.")
    elif available_resources["coffee"] < drinks[drink]["coffee"]:
        print("Not enough coffee.Money Refunded.")


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def make_drink(drink):
    clear()
    money_given = ask_money()

    if check_money(money_given, drink):
        change = round(calculate_change(money_given, drink), 2)
        if change > 0:
            print(f"Here is {change}$ in change.")
        if check_resources(drink, available_resources):
            use_resources(drink, available_resources)
            print(f"Enjoy your {drinks[drink]['name']}.")
        elif not check_resources(drink, available_resources):
            check_scarce_resource(drink, available_resources)
    else:
        print("Not given enough money.Money Refunded ")


def print_report():
    print(f"Water: {available_resources['water']}ml")
    print(f"Milk: {available_resources['milk']}ml")
    print(f"Coffee: {available_resources['coffee']}g")
    print(f"Money: {available_resources['money']}$")


want_more = True


while want_more:
    drink_choice = input(
        "What type of drink do you need ? (espresso,latte,cappuccino): ")
    if drink_choice == "report":
        print_report()
    elif drink_choice == "espresso":
        make_drink(0)
    elif drink_choice == "latte":
        make_drink(1)
    elif drink_choice == "cappuccino":
        make_drink(2)
    elif drink_choice == "close":
        want_more = False

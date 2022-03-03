CURRENCY = {
    "Quarter":0.25,
    "Dime":0.10,
    "Nickel":0.05,
    "Penny": 0.01, 
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

water = 300
milk = 200
coffee = 19
money = 0

def coffee1(data):
  if water < MENU[data]["ingredients"]["water"]:
    print("running low on water")
  elif coffee < MENU[data]["ingredients"]["coffee"]:
    print("Sry Less coffee")
  elif milk < MENU[data]["ingredients"]["milk"]:
    print("Sry less cow")
  else:
      return  False

def coins(data):
    global total
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    
    if total >= MENU[data]["cost"]:
      change = float("{:.2f}".format(total - 1.5))
      print(f"Here is your change {change} , And your Warm {data} coffee")
    else:
      print("less money")


condition = True
while condition == True:
    
    condition1 = True
    while condition1 == True:
        data = input("What would you like? (espresso/latte/cappuccino): ")
        if data == "report":
            print(f"""
            water = {water}
            milk = {milk}
            coffee = {coffee}
            money = {money}
            """)

        else:
            coffee1(data)
            condition1 = False

    if data =="espresso":
        coffee1(data)
        coins(data)
        water = water - MENU[data]["ingredients"]["water"]
        coffee = coffee - MENU[data]["ingredients"]["coffee"]
        money = money + 1.5
    elif data == "latte":
        coffee1(data)
        coins(data)
        water = water - MENU[data]["ingredients"]["water"]
        coffee = coffee - MENU[data]["ingredients"]["coffee"]
        milk = milk - MENU[data]["ingredients"]["milk"]
        money = money + 2.5
    elif data == "cappuccino":
        coffee1(data)
        coins(data)
        water = water - MENU[data]["ingredients"]["water"]
        coffee = coffee - MENU[data]["ingredients"]["coffee"]
        milk = milk - MENU[data]["ingredients"]["milk"]
        money = money + 3.0


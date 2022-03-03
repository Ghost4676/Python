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

water1 = 300
milk1 = 200
coffee1 = 100
money1 = 0


def coins():
    global total
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))

    total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)




condition = True
while condition == True:
    
    condition1 = True
    while condition1 == True:
        data = input("What would you like? (espresso/latte/cappuccino): ")
        if data == "report":
            print(f"""
            water = {water1}
            milk = {milk1}
            coffee = {coffee1}
            money = {money1}
            """)

        else:
            condition1 = False
      

    # quarters = float(input("How many quarters? "))
    # dimes = float(input("How many dimes? "))
    # nickles = float(input("How many nickles? "))
    # pennies = float(input("How many pennies? "))

    # total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)

    # espreso , latee , cuppichino
    if data =="espresso":
        if water1 >= 50:
            if coffee1 >= 18:
                coins()
                if total >= 1.5:
                    change = float("{:.2f}".format(total - 1.5))
                    print(f"Here is your change {change} , And your Warm coffee")
                    water1 = water1 - 50
                    coffee1 = coffee1 - 18
                    money1 = money1 + 1.5
                else:
                    print("less money, u broke")
            else:
                print("Less coffee")
        else:
            print("Less water")

    elif data == "latte":
        if water1 >= 200:
            if coffee1 >= 24:
                if milk1 >= 150:
                    coins()
                    if total == 2.5:
                        print("Here is your awesome coffee")
                        water1 = water1 - 200
                        coffee1 = coffee1 - 24
                        milk1 = milk1 - 150
                        money1 = money1 + 2.5
                    elif total > 1.5:
                        change = float("{:.2f}".format(total - 2.5))
                        print(f"Here is your change {change} , And your Warm LATTE coffee")
                        water1 = water1 - 200
                        coffee1 = coffee1 - 24
                        milk1 = milk1 - 150
                        money1 = money1 + 2.5
                    else:
                        print("less money, u broke")
                else:
                    print("Less Milk")
            else:
                print("Less coffee")
        else:
            print("Less water")

    elif  data == "cappuccino":
        if water1 >= 250:
            if coffee1 >= 24:
                if milk1 >= 100:
                    coins()
                    if total == 3.0:
                        print("Here is your awesome coffee")
                        water1 = water1 - 250
                        coffee1 = coffee1 - 24
                        milk1 = milk1 - 100
                        money1 = money1 + 3.0
                    elif total > 1.5:
                        # change = total - 3.0
                        change = float("{:.2f}".format(total - 3.0))
                        print(f"Here is your change {change} , And your Warm Cappuccino coffee")
                        water1 = water1 - 250
                        coffee1 = coffee1 - 24
                        milk1 = milk1 - 100
                        money1 = money1 + 3.0
                    else:
                        print("less money, u broke")
                else:
                    print("Less Milk")
            else:
                print("Less coffee")
        else:
            print("Less water")














        # Make the report with the default values

    elif data =="off":
        print("Turning off Machine")
        condition = False









# User Input
# Check for the resources for that coffee (if else)
# Coin Input
# Add and check if less then the value of coffee
# if more ,return change else print less money


# reduce the content from the actual value and add the cost to money



# 4 if statement with report,espresso,cappucinno,off

#repeat
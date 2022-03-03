import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

list1 = []
list2 = []

def randcho():
    list1.append(random.choice(cards))
for i in range(0,2):
    randcho()


print(f"Your cards: {list1}, current score: {sum(list1)}")

list2.append(random.choice(cards))
print(f"Computer first card: {list2}")

condition = True
while condition == True:
    card_continue = input("Continue 'y' or 'n' ?  ")

    if card_continue == "y" and sum(list1) < 21:
        
        randcho()
        if sum(list1) > 21:
            print(f"Your cards: {list1}, current score: {sum(list1)}")
            condition = False
            print(list1)
            print("You Loose")

    elif sum(list1) == 21:
        print(list1)
        print("BlackJACK you WIN")
        condition = False
    

    elif card_continue == "n" and sum(list2) <= 21:
        list2.append(random.choice(cards))
        condition1 = True
        while condition1 == True:
            if sum(list1) <= sum(list2) and sum(list2) <= 21:
                print("PCWON")
                condition1 = False
                condition = False
            elif sum(list2) > 21:
                print("You Win")
                print(list2)
                condition1 = False
                condition = False
        

        
        print(list2)

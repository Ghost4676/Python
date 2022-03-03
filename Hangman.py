import random


word_list = ["ardvark", "baboon", "camel"]
chosen_word = (random.choice(word_list))

print(chosen_word)
delta = input("Guess a letter: ")
print(list(chosen_word))


lives = 6
list1 = []

for xx in range(len(chosen_word)):
    if chosen_word[xx] == delta:
        list1.append(delta)
    else:
         list1.append("_")

print(list1)

list2 = []
for aaa in range(len(chosen_word)):
    list2.append("_")
# print(list2)

if list1 == list2:
    lives = lives - 1
    print(f"You have {lives} lives left")
else:
    print("")


while list1 != list(chosen_word):
    delta = input("Guess a letter: ")
    for xx in range(len(chosen_word)):
        if chosen_word[xx] == delta:
            # print(delta)
            list1[xx] = delta
    

    
    print(list1)
print("You Win")
        


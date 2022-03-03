import random

rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

listt = ["ROCK","PAPER","SCISSOR"]

w = listt[rps]

print("\nYou choose " + listt[rps])
print("")


y = random.randint(0 , 2)
#print(y)
z = listt[y]

print("COMPUTER CHOOSE " + z)
print("")

if rps == 0 and y == 0:
    print("DRAW")
elif rps == 0 and y ==1:
    print("Paper wraps rock : COMPUTER WINS")
elif rps == 0 and y ==2:
    print("Rock destroys scissor : YOU WIN")

elif rps == 1 and y == 0:
    print("Paper covers Rock : YOU WINS")
elif rps == 1 and y ==1:
    print("DRAW")
elif rps == 1 and y ==2:
    print("scissor cuts paper : COMPUTER WINS")

elif rps == 2 and y == 0:
    print("Rock destroys scissor : COMPUTER WINS")
elif rps == 2 and y ==1:
    print("scissor cuts paper : YOU WIN")
elif rps == 2 and y ==2:
    print("DRAW")

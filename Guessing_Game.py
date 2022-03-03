
import random

r = random.randint(1 ,100)
print(f"The random number is {r}")

a = 0
def subs():
  return a - 1 

c = input("easy or hard ")
if c == "easy":
  a = 10
else:
  a = 5

condition = True
while a!= 0 and condition == True:
  print(f"You have {a} tries left\n")

  d = int(input("Make the guess "))

  if r > d:
    print("Too Low")
    a = subs()
  elif r < d:
    print("Too high")
    a = subs()
  elif r == d:
    print("You Won")
    condition = False

if a == 0:
  print("Lose")










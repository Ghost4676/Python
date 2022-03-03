import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


password = ""
for x in range(0 , nr_letters):
    y = random.randint(0 , 51)
    z = letters[y]
    password = z + password
print(password)
    



for a in range(0 , nr_numbers):
    b = random.randint(0,9)
    c = numbers[b]
    password = c + password
print(password)




for q in range(0 , nr_symbols):
    r = random.randint(0,8)
    # print(r)
    s = symbols[r]
    password = s + password
print(password)



print()

sr = ''.join(random.sample(password, len(password)))
print(f"Here is your password: {sr}")

###################################
# or to convert list to string

###################################
# password = ""
# list1 = [a,b,c,d]

# for char in list1:
#     password = password + char
# print(password)


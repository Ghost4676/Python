alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(text_fun,space_fun):
  n = ""
  m = 0
  for i in text_fun:
    m = alphabet.index(i)
    if alpha == "decode":
      m = m - space_fun
    else:
      m = m + space_fun
    n = n + alphabet[m]
  print("")
  print(f"The {alpha}d output is {n}\n")

from art import logo
print(logo)
conduct =True 
while conduct == True:

  alpha = input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
  text = input("Input your password\n").lower()
  space = int(input("Type the shift number\n"))

  space = space%26
  cipher(text_fun=text,space_fun=space)
  xx = input("Do you want to continue 'yes' or no ? ")
  if xx == "no":
    conduct = False

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


alpha = input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
text = input("Input your password\n").lower()
space = int(input("Type the shift number\n"))

space = space%26

def encrypt(text_fun,space_fun):
    n = ""
    m = 0
    
    for i in text_fun:
        m = alphabet.index(i)
        m = m + space_fun
        n = n + alphabet[m] 
    print(n)

def decrypt(text_fun,space_fun):
    p = ""
    q = 0
    
    for i in text_fun:
        q = alphabet.index(i)
        q = q - space_fun
        p = p + alphabet[q] 
    print(p)

if alpha == "encode":

    encrypt(text_fun=text,space_fun=space)
else:
    decrypt(text_fun=text,space_fun=space)

# class User:
#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.name = username
#         self.followers = 0
#         self.following = 0
    
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1

# user1 = User("123","Marshal")
# user2 = User("444","hathway")

# user1.follow(user2)

# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)
######################################################
#Error detection
######################################################

# try:
#     print("delta1")
#     a_dict = {"key": "value"}
#     print(a_dict["abcd"])
# except NameError:   # will check for Nameerror in try and print output
#     print("name error")
# except KeyError as error_message: # will check for keyerror in try save it in error_msg and will print below
#     print(f"the key {error_message} does not exist")
# else:  #only gets executed if try is successfull
#     print("hellow")

# if height >3: # This is called when we want a certain desired output and not beyone a value
#     raise ValueError("Human height should not be over 3 meters.")


####################################

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

condition = True
while condition == True:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("please enter letter")
    else:
        condition = False
print(output_list)
condition = False
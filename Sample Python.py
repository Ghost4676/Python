

# print ("Welcome to the tip calculator.")

# Bill = float(input("What was the total Bill? $ "))
# Tip = int(input("What percent tip would you like to give? 10, 12, or 15 ? "))
# Split = int(input("How many people to split the bill ? "))

# Tipp = float(((Tip/Bill) * 100 ) + Bill) 
# Splitt = (round(Tipp/Split ,2))

# print(Tipp)
# print(f"Each person should pay: $ {Splitt}")

#############################################################################


# water_level = float(input("water_level : ? "))
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")

#############################################################################

# number = int(input("Which number you wat to check? "))

# a = number % 2
# if a == 0:
#     print("Even")
# else:
#     print("Odd")

#############################################################################

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))

# BMI = round(weight/(height * height))
# print(BMI)
# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30:
#     print(f"Your BMI is {BMI}, you are Slightely overweight.")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are obese.")    
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")


##############################################################################


# Year = int(input("Which Year do you want to check? "))

# if Year % 4 == 0:
#     if Year % 100 == 0:
#         if Year % 400 == 0:
#             print("Leap year1")
#         else:
#             print("nonleap1")
#     else:
#         print("leap22")
#     # elif Year % 100 != 0:
#     #     print("leap2")

# else:
#     print(f'Year {Year} is a NON LEAP3 year')


###############################################################################

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ? ")
# add_pepperoni = input("Do you want pepperoni? Y or N ? ")
# extra_cheese = input("Do you want extra cheese? Y or N ? ")


# if size == 'S':
#   bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill = bill + 2
#     else:
#         bill = bill + 3
# if extra_cheese == "Y":
#     bill = bill + 1

    
# print(f"Your final bill is ${bill}")

#####################################################################

# print("Welcome to Love Calculator")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# ## TRUE LOVE

# n1 = name1.lower()
# n2 = name2.lower()

# n3 = n1 + n2

# T = n3.count("t")
# R = n3.count("r")
# U = n3.count("u")
# E = n3.count("e")

# L = n3.count("l")
# O = n3.count("o")
# V = n3.count("v")
# E = n3.count("e")

# n4 = str(T + R + U + E)
# n5 = str(L + O + V + E)

# n6 = int((n4) + (n5))

# if n6 < 10 or n6 > 90:
#     print (f"Your score is {n6}, you are like coke and mentos")
# elif n6 > 40 and n6 < 50:
#     print (f"your score is {n6}, you are alright together")
# else:
#     print(f"Your score is {n6}")

###################################################################


# import random

# r = random.randint(0 ,1)
# if r == 0:
# 	print("Tails")
# else:
# 	print("Heads")

###################################################################
# import random
# from random import shuffle
# names_string = input("Give me everybody's names , seperated by a comma. ")
# names = names_string.split(", ")

# x = len(names)
# print(x)

# y = random.randint(0 , x-1 )
# z = names[y]

# print(z)

##################################################################

# row1 = ["🤔","1","🤔"]
# row2 = ["🤔","2","🤔"]
# row3 = ["🤔","3","🤔"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the Treasure ? ")

# h = int(position[0])
# v = int(position[1])

# sr = map[v -1]
# sr[h -1] = "X"


# print(f"{row1}\n{row2}\n{row3}")

################################################

# Fruits = ["apple","mango","pear"]

# for x in Fruits:
#     print(x)

################################################
# TO FIND AVERAGE HEIGHT AMONG LIST OF PEOPLE
################################################
# student_heights = input(" Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # print(type(student_heights))

# ht = 0
# for x in student_heights:
#     ht = ht + x    
# print(ht)

# htt = 0
# for xx in student_heights:
#     htt = htt + 1
    
# print(htt)

# average_height = round(ht/htt)
# print(average_height)


# ##########
# PROGRAM TO print THE HIGHEST NUMBER
# ##########

# student_scores = input("Input a list of student scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# yy = 0
 
# for lstv in student_scores:
#     if lstv > yy:
#         yy = lstv
#         print(lstv)

# print(f"The Highest score in the calss is: {yy}")

#################################################
# PROGRAM TO ADD EVEN NUMBERS IN RANGE OF 1-100
#################################################

# null = 0

# for numbers in range(0 , 101, 2):
#     null = null + numbers
# print(null)

###############################################
# FIZZ BUZZ
###############################################


# for number in range(0,20):

#     if number % 3 == 0:
#         if number % 5 ==0:
#             print("Fizzbuzz")
#         else:
#             print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#           print(number)
        
        

        
# a = ['aa','bb','cc']
  

# for x in range(len(a)):
#     print (a[x], end="")

#############################
# List to string
#############################        
# a = ['aa','bb','cc']

# bb = ""
# for hell in a:
#     bb = bb + hell
#     print(bb)
# print(bb)
 
 #########################################


# def my_function():
#     print("Hellow World")
#     print("Hi")
# my_function()

#########################################

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def Jump(): 
#     turn_left()
#     move()
#     turn_right()

# def rotate(): 
#     turn_left()
#     turn_left()
    


# while at_goal() != True:
    
#     if wall_in_front() != True:
#         if wall_on_right() == True:
#             move()
#         elif wall_on_right() != True:
#             move()
#             turn_right()
            
#     elif wall_in_front() == True:
#             if wall_on_right() == True:
#                 Jump()
#             elif wall_on_right() != True:
#                 turn_left()
#                 if wall_in_front() != True:
#                     move()
#                     turn_right()
#                 else:
#                     turn_left()
           
###############################################
# or
###############################################

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
        
    
###########################################################################


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while not at_goal():

#     if wall_on_right() != True:
#         turn_right()
#         move()
      
#     elif front_is_clear() == True:
#         move()
    
#     else:
#         turn_left()


  ######################################################################
# EXTRA check if needed 
######################################################################
# delta = input("Guess a letter: ")


# print("")
# for x in chosen_word:
#     if x == delta:
#         # print("Right")
#     # else:
#         # print("Wrong")


###########################################################

# import random


# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = (random.choice(word_list))

# print(chosen_word)
# delta = input("Guess a letter: ")
# print(list(chosen_word))


# lives = 6
# list1 = []

# for xx in range(len(chosen_word)):
#     if chosen_word[xx] == delta:
#         list1.append(delta)
#     else:
#          list1.append("_")

# print(list1)

# list2 = []
# for aaa in range(len(chosen_word)):
#     list2.append("_")
# # print(list2)

# if list1 == list2:
#     lives = lives - 1
#     print(f"You have {lives} lives left")
# else:
#     print("")

# list3 = []

# bb = 1
# a = 1
# b = 1 
# while list1 != list(chosen_word):
#     delta = input("Guess a letter: ")
    
#     for xx in range(len(chosen_word)):
#         if chosen_word[xx] == delta:
#             # print(delta)
#             list1[xx] = delta

#     if chosen_word[xx] != delta:
#       lives = lives -1
#       print(lives)
#       if lives == 0:
#         list1 = list(chosen_word)
#         print("You Loose")
#     print(list1)

# print("You Win")

####################################################################

# def greet(name):
#     print(f"My name is {name}")
#     print(f"Hellow {name}")
# # Here name is the Parameter and Darshan is the Argument

# greet("Darshan")

####################################################################

# def Greet_with(name, location):
#     print(f"Hellow {name}")
#     print(f"What is it like in {location}")

# Greet_with(location ="Mumbai",name="Darshan")

# ###################################################

# Height and weidth using Functions
# ###################################################
# #Write your code below this line 👇
# import math
# def paint_calc(height, width, cover):
#   NOC = (height*width  / cover)
#   print(int(math.ceil(NOC)))


# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

###########################################################

# PRIME AND NON PRIME

##########################################################
# #Write your code below this line 👇
# def prime_checker(number):

#   is_prime = True
#   for x in range(2,number-1):
#     if number%x == 0:
#       is_prime= False
#   if is_prime == True:
#     print("Its a Prime number")
#   else:
#     print("Its a non prime number")
      

# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

########################################################

# databet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# plain_text = "hello"

# b = ""
# n = ""

# for i in range(len(plain_text)):
#   b = databet.index(plain_text[i])
  
#   n = n + (databet[b + 5])

# print(n)


###################################################
# Dictionary code to give value to the score

###################################################

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇

# for grade in student_scores:
#   if student_scores[grade] <= 70:
#     student_grades[grade] = "Fail"
#   elif student_scores[grade] <= 80:
#     student_grades[grade] = "Acceptable"
#   elif student_scores[grade] <= 90:
#     student_grades[grade] = "Exceed EXP"
#   else:
#         student_grades[grade] = "Out"


# # 🚨 Don't change the code below 👇
# print(student_grades)

###############################################################
# Highest Number in dictionary

# data = {
#   "Heat": 32, "fire":44, "water": 25, "snow":88,
# }

# n = 0
# x = ""
# for i in data:
#   if data[i] > n:
#     n = data[i]
#     x = data[i]
# print(x)



  # print(data[i])

##############################################################

# Functions with output


# def format_name(f_name,l_name):
#   formatted_f = f_name.title()
#   formatted_l = l_name.title()
#   return f"The first name is {formatted_f} and the last name is {formatted_l}"


# test = format_name("darshan","PATEL")
# print(test)

##############################################################

# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "Invalid"
#   formatted_f = f_name.title()
#   formatted_l = l_name.title()
#   return f"{formatted_f} {formatted_l}"

# # print(format_name(input("darshan"),input("patel")))


# main = format_name(input("Darshan"),input("patel"))
# print(main)

#################################################################
# Leap year and month

# def is_leap(year,month):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year,month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year,month) == False:
#     print(month_days[month - 1])
#   elif is_leap(year,month) == True and month ==2:
#     print("29")
#   else:
#     print(month_days[month - 1])

#   # if is_leap(year,month) == True and month == 2:
#   #   return 29
#   # return month_days[month - 1]

  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

##############################################################
# import random
# list1 = [1,2,3]
# # list2 = []

# # lis2 = list2.append(random.choice(list1))

# # print(list2)
# # print(lis2)

# print(sum(list1))

##############################################################

# enemy = 2

# def in_en():
#   print(enemy)
#   return enemy + 1

# enemy = in_en()
# print(enemy)


# def carl():
#   print("Hellow word")

# x = input("testing  ")

# x()

################################################################
# Guessing Game
################################################################
# r = 30
# a = 0
# def subs():
#   return a - 1 

# c = input("easy or hard ")
# if c == "easy":
#   a = 10
# else:
#   a = 5

# condition = True
# while a!= 0 and condition == True:
#   print(f"You have {a} tries left\n")

#   d = int(input("Make the guess "))

#   if r > d:
#     print("Too Low")
#     a = subs()
#     # print(f"You have {a} tries")
#   elif r < d:
#     print("Too high")
#     a = subs()
#     # print(f"You have {a} tries")
#   elif r == d:
#     printt("You Won")
#     condition = False

# if a == 0:
#   printt("Lose")


#######################################


# contacts = {
#   "James":{"ph": 124253,"email":"asfasfada",}
# }

# print(contacts["James"]["ph"])

######################################3

# water = 100

# def reduce():
#   # global water
#   water = water - 20
#   print(water)

# reduce()
# print(water)

#####################################

# enemies = 1 

# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# enemies = increase_enemies()
# print(enemies)

######################

# from random import randint
# dice_imgs = ["1","2","3","4","5","6"]
# dice_num = randint(0,len(dice_imgs) -1 )
# print(dice_imgs[dice_num])

# year = int(input("Whats your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial")
# elif year >= 1994:
#   print("you are a Gen Z")


# a = 0
# b = 0
# pages = int(input("no of page"))
# word = int(input("no of word"))
# total = pages * word
# print(total)

# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,13])

# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)


# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#             "milk": 0,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# water = 300
# milk = 50
# coffee = 24


# def coffee1(data):
#   if water < MENU[data]["ingredients"]["water"]:
#     print("running low on water")
#     return  water - 10
#   elif coffee < MENU[data]["ingredients"]["coffee"]:
#     print("Sry Less coffee")
#   elif milk < MENU[data]["ingredients"]["milk"]:
#     print("Sry less cow")
    
  

# data = input("coffee name ? ")
# coffee1(data)




# if data == "espresso":
#   coins()





# def coins(data):
#     global total
#     quarters = float(input("How many quarters? "))
#     dimes = float(input("How many dimes? "))
#     nickles = float(input("How many nickles? "))
#     pennies = float(input("How many pennies? "))
#     total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    
#     if total >= MENU[data]["cost"]:
#       change = float("{:.2f}".format(total - 1.5))
#       print(f"Here is your change {change} , And your Warm {data} coffee")
#     else:
#       print("less money")

    


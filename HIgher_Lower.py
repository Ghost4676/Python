# from art import logo1 ,vs
# print(logo1)
import random
from game_data import data

score = 0

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a" #meaning if guess = a return True else false
    else:
        return guess == "b"

game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    #print(vs)
    print(f"With B: {format_data(account_b)}.")

    guess = input("Who has more followers A or B ?").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]


    is_correct = check_answer(guess, a_follower_count,b_follower_count)


    if is_correct:  #is_correct = true
        score +=1
        print(f"You are right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score} ")
        game_should_continue = False
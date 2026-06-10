
import random
from art import logo,vs
from game_data import data
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    acc_country = account["country"]
    return f"{account_name}, {account_descr},from {acc_country}"
account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)
print(logo)
print(f"compare A:{format_data(account_a)}")
print(f"{vs}who has the most followers?")
print(f"compare B:{format_data(account_b)}X")

game=True
lives=0
while game==True:

    guess=input("Enter your guess: A or B : ").lower()
    if guess=="a":
        if account_a["follower_count"]>account_b["follower_count"]:
            lives+=1
            print(f"Score: {lives}")
            print("You guessed right!!")
            print(f"Compare A:{format_data(account_a)}")
            account_b=random.choice(data)
            print(f"{vs}who has the most followers?")
            print(f"compare B:{format_data(account_b)}")
        else:
            print("You guessed wrong!!")
            game=False
    elif guess=="b":
        if account_a["follower_count"]<account_b["follower_count"]:
            lives += 1
            print(f"Score: {lives}")
            print("You guessed right!!")
            print(f"Compare A:{format_data(account_b)}")
            account_b=random.choice(data)
            print(f"{vs}who has the most followers?")
            print(f"compare B:{format_data(account_b)}")
        else:
            print("You guessed wrong!!")
            game=False
    else:
        print("Type only A or B")
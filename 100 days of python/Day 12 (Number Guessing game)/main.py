import random
from art import logo
print(logo)

CHOICE=(random.randint(1,100))
print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")
lives=0
if difficulty=='easy':
    lives=10

elif difficulty=='hard':
    lives=5

win=False
def guess():
    global win
    global lives
    print(f"You have {lives} attempts to guess the number.")
    user_ans=int(input("make a guess:"))
    if user_ans==CHOICE:
        print(f"You guessed the number!👌🥳{CHOICE}")
        win=True
    elif user_ans<CHOICE:
        print("Too low!")
        lives-=1
        if lives==0:
            print("You ran out of lives!")
            print(f"The number was {CHOICE}")
    elif user_ans>CHOICE:
        print("Too high!")
        lives-=1
        if lives==0:
            print("You ran out of lives!")
            print(f"The number was {CHOICE}")
while not lives==0 and win==False:
    guess()

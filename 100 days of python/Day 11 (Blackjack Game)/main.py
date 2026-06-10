import random
from art import logo
print(logo)
def play():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal_card(user_card1, computer_card1):
        first_card = random.choice(cards)
        second_card = random.choice(cards)
        user_card1 += [first_card, second_card]

        computer_card1 += [computer_1card, computer_2card]

        deals=[user_card1, computer_card1]
        return deals
    computer_1card = random.choice(cards)
    computer_2card = random.choice(cards)
    user_card = []
    computer_card = []
    deal_card(user_card, computer_card)



    ask = input("Do you want to play blackjack? (y/n) ")


    def add_card():
        user_card.append(random.choice(cards))
        computer_card.append(random.choice(cards))

        return user_card, computer_card

    def win():
        print("You won!")
    def lose():
        print("You lost!")
    def draw():
        print("draw")
    def bust():
        print("you bust")
    def com_res():
        print("computer overwent")
    def blackjack():
        print("blackjack")
    def com_blkjk():
        print("computer blackjack")

    def print_stat():
        print(f"your cards:{user_card},Total={sum(user_card)}")

        print(f"computers first card: {computer_1card}")
    if ask == "y":
        cont=False
    else:
        cont=True
    def compare():
        if sum(user_card) == sum(computer_card):
            draw()
        elif sum(user_card) > 21:
            bust()
        elif sum(user_card) == 21:
            blackjack()
        elif sum(computer_card) == 21:
            com_blkjk()
        elif sum(computer_card) > 21:
            com_res()
            win()
        elif sum(user_card) > sum(computer_card):
            win()
        else:
            lose()

        play()
    while not cont:

        print_stat()
        shou = input("Type 'y' to get another card, type 'n' to pass: ")


        if shou == "n":
            print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
            print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
            compare()

        elif shou == "y":

            add_card()
            print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
            print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
            compare()
            play()

play()


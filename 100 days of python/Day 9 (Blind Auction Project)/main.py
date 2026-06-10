from art import logo
print(logo)


dictionary={}

cont="yes"
while cont=="yes":
    name=input("What is your name?")
    bid=int(input("What is your bid?"))
    dictionary[name]=bid
    cont = input("is there anyone else?Yes or No?").lower()
    if cont=="yes":
        print("\n"*20)
        print(logo)
    elif cont=="no":
        winner=(max(dictionary))
        print(f'The winner is {winner}'
              f' with a bid of ${dictionary[winner]}')




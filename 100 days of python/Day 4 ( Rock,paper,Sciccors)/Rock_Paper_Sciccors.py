import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
play_list = [rock, paper, scissors]
num = int(input("type 0 for rock, 1 for paper, 2 for scissors:?"))
if num > 2:
    print("invalid character")
else:
    print("you chose",play_list[num])
    computer_choice = random.randint(0,2)
    print("computer chose",play_list[computer_choice])
    if num == computer_choice:
        print("draw")
    elif computer_choice == 0 and num == 1:
        print("you win")
    elif computer_choice == 2 and num == 0:
        print("you win")
    elif computer_choice == 1 and num == 2:
        print("you win")
    else:
        print("lost")


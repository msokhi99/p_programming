'''
Rock Paper Scissors.
'''

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

optList=[rock,paper,scissors]
userChoice=int(input("Choose: 0->Rock, 1->Paper, 2->Scissors "))
compChoice=random.randint(0,2)
if userChoice==0 and compChoice==0:
    print(f"You chose\n{optList[0]}\n Computer Chose:\n {optList[0]}\nIt is a draw.")
elif userChoice==0 and compChoice==1:
    print(f"You chose\n{optList[0]}\n Computer Chose:\n {optList[1]}\nYou lose.")
elif userChoice==0 and compChoice==2:
    print(f"You chose\n{optList[0]}\n Computer Chose:\n {optList[2]}\nYou win.")
elif userChoice==1 and compChoice==0:
    print(f"You chose\n{optList[1]}\n Computer Chose:\n {optList[0]}\nYou win.")
elif userChoice==1 and compChoice==1:
    print(f"You chose\n{optList[1]}\n Computer Chose:\n {optList[1]}\nIt is a draw.")
elif userChoice==1 and compChoice==2:
    print(f"You chose\n{optList[1]}\n Computer Chose:\n {optList[2]}\nYou lose.")
elif userChoice==2 and compChoice==0:
    print(f"You chose\n{optList[2]}\n Computer Chose:\n {optList[0]}\nYou lose.")
elif userChoice==2 and compChoice==1:
    print(f"You chose\n{optList[2]}\n Computer Chose:\n {optList[1]}\nYou win.")
elif userChoice==2 and compChoice==2:
    print(f"You chose\n{optList[2]}\n Computer Chose:\n {optList[2]}\nIt is a draw.")

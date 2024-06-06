'''
Treasure Map.
'''

print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
      ''')
print("\n")
print("Welcome to Treasure Isalnd. Your mission is to find the treasure !")
userChoiceOne=str(input("Choose an option: Left or Right - "))
if userChoiceOne=="left" or userChoiceOne=="Left":
    userChoiceTwo=str(input("You survived and now have approached a river. Choose an option: Swim or Wait - "))
    if userChoiceTwo=="wait" or userChoiceTwo=="Wait":
        userChoiceThree=str(input("You survived and now have approached 3 different colored doors. What door do you wish to go through - Choose an option: Red, Yellow or Blue - "))
        if userChoiceThree=="Red" or userChoiceThree=="red":
            print("You were burned by a fire. Game Over.")
        elif userChoiceThree=="Yellow" or userChoiceThree=="yellow":
            print("You Win !")
        elif userChoiceThree=="Blue" or userChoiceThree=="blue":
            print("You were eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("You were attacked by a trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")

import random
import numberGuessingGameLogo

print(numberGuessingGameLogo.welcomeLogo)

def welcomeMsg():
    print("Welcome to the Number Guessing Game:\nI am thinking of a number between 1 and 100.")

def getUserChoice():
    tempChoice=str(input("Choose a difficulty level: (E)-> Easy or (H)-> Hard: "))
    return tempChoice

def computerNumber():
    tempCompGuess=random.randint(1,101)
    return tempCompGuess

def getUserLives(fUserChoice):
    tempUserLives=0
    if fUserChoice=="E" or fUserChoice=="e":
        tempUserLives=10
    else:
        tempUserLives=5
    return tempUserLives

def getUserGuess():
    tempUserGuess=int(input("Guess a number: "))
    return tempUserGuess

def compareNum(fUserGuess,fCompGuess):
    if fUserGuess==fCompGuess:
        print("You guessed the correct number.")
        return True
    elif fUserGuess>fCompGuess:
        print("Your guess is too high.")
        return False
    else:
        print("Your guess is too low.")
        return False

def restartProgram():
    tempRestart=str(input("Do you want to play again: (Y) -> Yes or (N) -> No: "))
    if tempRestart=="Y" or tempRestart=="y":
        guessingGame()
    elif tempRestart=="N" or tempRestart=="n":
        print("Exiting Program.")

def guessingGame():
    welcomeMsg()
    numberToGuess=computerNumber()
    userChoice=getUserChoice()
    userLives=getUserLives(userChoice)

    while userLives>0:
        userGuess=getUserGuess()
        result=compareNum(userGuess,numberToGuess)
        if result==True:
            break
        else:
            userLives-=1
            print(f"You have {userLives} attemps remaining.")
    restartProgram()

guessingGame()

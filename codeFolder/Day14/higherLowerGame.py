import random 
import gameData
import gameLogo
import os

def clear_screen():
    if os.name=='nt':
        os.system('cls')

print(gameLogo.gameLogo)

def randomChoiceOne():
    tempChoiceOne=random.randint(0,len(gameData.userDataForGame)-1)
    return tempChoiceOne

def randomChoiceTwo():
    tempChoiceTwo=random.randint(0,len(gameData.userDataForGame)-1)
    return tempChoiceTwo

def printCompareA(fRandomChoice):
   print(f"Compare A: {gameData.userDataForGame[fRandomChoice]["name"]}, a {gameData.userDataForGame[fRandomChoice]["description"]}, from {gameData.userDataForGame[fRandomChoice]["country"]}.")

def printCompareB(fRandomChoice):
    print(f"Compare B: {gameData.userDataForGame[fRandomChoice]["name"]}, a {gameData.userDataForGame[fRandomChoice]["description"]}, from {gameData.userDataForGame[fRandomChoice]["country"]}.")

def getUserInput():
    tempInput=str(input("Who has the most followers: (A) or (B): "))
    return tempInput

choiceOne=randomChoiceOne()
choiceTwo=randomChoiceTwo()
currentScore=0

def compareFollowers(fUserInput):
    global choiceOne
    global choiceTwo
    global currentScore
    tempA=gameData.userDataForGame[choiceOne]["follower_count"]
    tempB=gameData.userDataForGame[choiceTwo]["follower_count"]
    if fUserInput=="A":
        if tempA>tempB:
            choiceTwo=randomChoiceTwo()
            currentScore+=1
            print(f"Current Score: {currentScore}")
            return
        elif tempA<tempB:
            return False
    elif fUserInput=="B":
        if tempA>tempB:
            return False
        elif tempB>tempA:
            choiceOne=choiceTwo
            choiceTwo=randomChoiceTwo()
            print(f"Current Score: {currentScore}")
            currentScore+=1
            return

def getCurrentScore():
    global currentScore
    print(f"Your Current Score: {currentScore}")

def restartGame():
    global choiceOne
    global choiceTwo
    global currentScore
    tempRestart=str(input("Do you want to play again: (Y) -> Yes or (N) -> No "))
    if tempRestart=="Y" or tempRestart=="y":
        choiceOne=randomChoiceOne()
        choiceTwo=randomChoiceTwo()
        currentScore=0
        clear_screen()
        higherLowerGame()
    elif tempRestart=="N" or tempRestart=="n":
        print("Exiting Program .... ")

def higherLowerGame():
    global choiceOne
    global choiceTwo
    gameStatus=True
    while gameStatus==True:
        getCurrentScore()
        if choiceOne==choiceTwo:
            choiceOne=randomChoiceOne()
            choiceTwo=randomChoiceTwo()
        printCompareA(choiceOne)
        print(gameLogo.vsLogo)
        printCompareB(choiceTwo)
        userInput=getUserInput()
        result=compareFollowers(userInput)
        clear_screen()
        if result==False:
            print(f"Final Score: {currentScore}")
            gameStatus=False
    restartGame()

higherLowerGame()

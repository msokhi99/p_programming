import coffeeMachineData

print(coffeeMachineData.asciiLogo)

QUARTER=0.25
DIME=0.10
NICKEL=0.05
PENNY=0.01

def dispReport(fResources):
    for keys in fResources:
        print(f"{keys} : {fResources[keys]} ml")

def dispMenuGetUserInput():
    tempInput=int(input("COFFEE MENU: \n(1) -> Espresso -- (2) -> Latte -- (3) -> Cappucino -- (4) -> Exit (5) -> Report - "))
    return tempInput

def checkResources(fResources,fMainMenu,fUserInput):

    if fUserInput==4:
        return False
    
    if fUserInput==5:
        dispReport(coffeeMachineData.currentResources)
        coffeeMachine()

    for keyOne in fMainMenu[fUserInput]["ingredients"]:
        while fResources[keyOne]<fMainMenu[fUserInput]["ingredients"][keyOne]:
            userContinue=int(input(f"You need to add {fMainMenu[fUserInput]["ingredients"][keyOne]-fResources[keyOne]} ML more {keyOne}. Press (1) -> Add {keyOne} or (2) -> Exit - "))
            if userContinue==1:
                userAdd=addMore(keyOne)
                fResources[keyOne]=fResources[keyOne]+userAdd
            else:
                return False

    for keyOne in fMainMenu[fUserInput]["ingredients"]:
        if fResources[keyOne]>=fMainMenu[fUserInput]["ingredients"][keyOne]:
            return True  
           
def addMore(fKeyOne):
    tempAdd=int(input(f"Add {fKeyOne} - "))
    return tempAdd

def getMoney():
    tempQuarter=int(input("QUARTERS -> "))
    tempDime=int(input("DIMES -> "))
    tempNickel=int(input("NICKELS -> "))
    tempPenny=int(input("PENNIES -> "))
    tempMoney=round(((tempQuarter*QUARTER)+(tempDime*DIME)+(tempNickel*NICKEL)+(tempPenny*PENNY)),2)
    return tempMoney

def checkMoney(fUserMoney,fMainMenu,fUserInput):
    while fUserMoney<fMainMenu[fUserInput]["cost"]:
        userContinue=int(input(f"You need ${fMainMenu[fUserInput]["cost"]-fUserMoney} more. Press (1) -> Add Money or (2) -> Exit - "))
        if userContinue==1:
            tempAdd=getMoney()
            fUserMoney=fUserMoney+tempAdd
        else:
            print("Thank you for using the coffee machine.")
            return False
    
    return True

def returnChange(fUserMoney,fMainMenu,fUserInput):
    if fUserMoney>=fMainMenu[fUserInput]["cost"]:
        changeToReturn=round(fUserMoney-fMainMenu[fUserInput]["cost"],2)
    return changeToReturn

def makeCoffee(fResources,fMainMenu,fUserInput):
    for keyOne in fMainMenu[fUserInput]["ingredients"]:
        if fResources[keyOne]>=fMainMenu[fUserInput]["ingredients"][keyOne]:
            fResources[keyOne]=fResources[keyOne]-fMainMenu[fUserInput]["ingredients"][keyOne]

def makeCoffeeAgain():
    tempInput=int(input("(1) -> Make another coffee (2) -> Exit Machine - "))
    if tempInput==1:
        coffeeMachine()
    else:
        print("Exiting Machine.")

def coffeeMachine():
    userInput=dispMenuGetUserInput()
    result=checkResources(coffeeMachineData.currentResources,coffeeMachineData.mainMenu,userInput)
    if result==True:
        userMoney=getMoney()
        resultTwo=checkMoney(userMoney,coffeeMachineData.mainMenu,userInput)
        if resultTwo==True:
            makeCoffee(coffeeMachineData.currentResources,coffeeMachineData.mainMenu,userInput)
            userChange=returnChange(userMoney,coffeeMachineData.mainMenu,userInput)
            print(f"Your change -> ${userChange}")
            print(f"Enjoy your coffee.")
            makeCoffeeAgain()
    else:
        print("Exiting Program.")

coffeeMachine()

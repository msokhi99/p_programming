import calculatorLogo

resultList=[]

def addNum(numOne,numTwo):
    return numOne+numTwo
def subNum(numOne,numTwo):
    return numOne-numTwo
def mulNum(numOne,numTwo):
    return numOne*numTwo
def divNum(numOne,numTwo):
    if numTwo==0:
        print("Undefined")
        numTwo=float(input("Enter a non zero input: "))
    return numOne/numTwo

calculatorOperations={
    "+":addNum,
    "-":subNum,
    "*":mulNum,
    "/":divNum,
}

print(calculatorLogo.logo)
userNumOne=float(input("Enter a number: "))
print("\n")
for key in calculatorOperations:
    print(key)
userChoice=input("\nChoose an operation: ")
userOperation=calculatorOperations[userChoice]
userNumTwo=float(input("\nEnter a number: "))
result=userOperation(userNumOne,userNumTwo)
resultList.append(result)
print(f"\n{userNumOne}{userChoice}{userNumTwo}={resultList[-1]}")

programStauts=True

while programStauts==True:
    userChoiceTwo=str(input("\nPress (Y) to continue calculation with the previous result or (N) to begin a new calculation or (Q) to quit the program: "))
    if userChoiceTwo=="Y" or userChoiceTwo=="y":
        print("\n")
        for key in calculatorOperations:
            print(key)
        userChoice=input("\nChoose an operation: ")
        userOperation=calculatorOperations[userChoice]
        userNumThree=int(input("Enter a number: "))
        prevResult=result
        result=userOperation(resultList[-1],userNumThree)
        resultList.pop(-1)
        resultList.append(result)
        print(f"\n{prevResult}{userChoice}{userNumThree}={resultList[-1]}")
    elif userChoiceTwo=="N" or userChoiceTwo=="n":
        resultList.clear
        userNumOne=float(input("Enter a number: "))
        print("\n")
        for key in calculatorOperations:
            print(key)
        userChoice=input("\nChoose an operation: ")
        userOperation=calculatorOperations[userChoice]
        userNumTwo=float(input("\nEnter a number: "))
        result=userOperation(userNumOne,userNumTwo)
        resultList.append(result)
        print(f"\n{userNumOne}{userChoice}{userNumTwo}={resultList[-1]}")
    elif userChoiceTwo=="Q" or userChoiceTwo=="q":
        programStauts=False
        print("Exiting Program ....")

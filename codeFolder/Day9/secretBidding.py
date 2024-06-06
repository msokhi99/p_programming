import biddingLogo
import os
print("SECRET AUCTION")

print(biddingLogo.hammerLogo)

biddersDict={}

def clear_screen():
    if os.name=='nt':
        os.system('cls')

def makeDict(fName,fBid):
    biddersDict[fName]=fBid

def makeComparison(fDict):
    tempMax=0
    tempName=""
    for key in fDict:
        if fDict[key]>tempMax:
            tempMax=fDict[key]
            tempName=key
    
    print(f"{tempName} made the highest bid of $ {tempMax}")

def getUserName():
    tempName=str(input("Name -> "))
    return tempName
def getUserBid():
    tempBid=float(input("Bid -> $ "))
    return tempBid
def moreUsers():
    tempChoice=str(input("More Users -> (Y) or (N) "))
    return tempChoice

programStatus=True

while programStatus==True:
    makeDict(getUserName(),getUserBid())
    userChoice=moreUsers()
    clear_screen()
    if userChoice=="Y":
        pass
    elif userChoice=="N":
        programStatus=False
        makeComparison(biddersDict)

print(biddersDict)

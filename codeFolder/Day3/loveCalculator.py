'''
Love Calculator.
'''

nameOne="Prince William"
nameTwo="Kate Middleton"
nameOne=nameOne.lower()
nameTwo=nameTwo.lower()
checkFor="True"
checkFor=checkFor.lower()
checKForTwo="Love"
checkForTwo=checKForTwo.lower()

countOne=0
countTwo=0
countThree=0
countFour=0

for x in nameOne:
    for y in checkFor:
        if x==y:
            countOne+=1
for x in nameTwo:
    for y in checkFor:
        if x==y:
            countTwo+=1
totalCountOne=countOne+countTwo;

for x in nameOne:
    for y in checkForTwo:
        if x==y:
            countThree+=1
for x in nameTwo:
    for y in checkForTwo:
        if x==y:
            countFour+=1

totalCountTwo=countThree+countFour;

loveScore= int(str(totalCountOne)+str(totalCountTwo))
if(loveScore<10 or loveScore>90):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore>=40 and loveScore<=60:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}")

'''
Highest Score.
'''

allScore=input().split()
allScore=[int(score) for score in allScore]
tempMax=0
for x in allScore:
    if x>tempMax:
        tempMax=x

print(f"Highest Score: {tempMax}")
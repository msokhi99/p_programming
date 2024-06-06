'''
Updated Treasure Map.
'''

listOne=[" "," "," "]
listTwo=[" "," "," "]
listThree=[" "," "," "]

mapGrid=[listOne,listTwo,listThree]

print(f"{listOne}\n{listTwo}\n{listThree}")

userLoc=str(input("Where do you want to place the treasure on the map - "))
colNum=userLoc[0]
rowNum=int(userLoc[1])
print(type(rowNum))
print(type(colNum))
if colNum=="A":
    mapGrid[rowNum][0]="X"
elif colNum=="B":
    mapGrid[rowNum][1]="X"
elif colNum=="C":
    mapGrid[rowNum][2]="X"

print(f"{listOne}\n{listTwo}\n{listThree}")
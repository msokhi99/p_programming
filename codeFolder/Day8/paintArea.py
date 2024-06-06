import math

def numPaintCans(wallHeight, wallWidth):
    coveragePerCan=5
    numCans=((wallHeight*wallWidth)/coveragePerCan)
    return math.ceil(numCans)

totalPaintCansRequired=numPaintCans(wallHeight=2,wallWidth=4)
print(totalPaintCansRequired)
studentScore={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

def convertScoreToGrades (scoreDict):
    convertedDict={}
    for key in scoreDict:
        if scoreDict[key]>=91 and scoreDict[key]<=100:
            convertedDict[key]="Outstanding"
        elif scoreDict[key]>=81 and scoreDict[key]<=90:
            convertedDict[key]="Exceeds Expectations"
        elif scoreDict[key]>=71 and scoreDict[key]<=80:
            convertedDict[key]="Acceptable"
        elif scoreDict[key]<=70:
            convertedDict[key]="Fail"
    return convertedDict

updatedDict=convertScoreToGrades(studentScore)
print(updatedDict)
'''
Life In Weeks.
'''

print("Enter your age: ")
userAge=int(input())
numOfWeeksInOneYear=52
maxNumOfWeeks=90*numOfWeeksInOneYear;
numOfWeeksLeftForUser=maxNumOfWeeks-(userAge*numOfWeeksInOneYear)
print(f"You have {numOfWeeksLeftForUser} weeks left.")
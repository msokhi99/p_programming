'''
BMI Calculator
'''

print("Enter your weight: ")
userWeight=float(input())
print("Enter your height: ")
userHeight=float(input())
bmiResult=int(userWeight/(userHeight ** 2));
print(f"Your BMI with {userWeight} and {userHeight} is: {bmiResult}")
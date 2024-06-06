'''
Updated BMI.
'''

userHeight=float(input("Enter your height: "))
userWeight=float(input("Enter your weight: "))
bmiIndex=round(float(userWeight/(userHeight ** 2)),2)
if bmiIndex<18.5:
    print(f"Your BMI index is {bmiIndex} and you are underweight.")
elif bmiIndex>=18.5 and bmiIndex<25:
    print(f"Your BMI index is {bmiIndex} and you are overweight.")
elif bmiIndex>=25 and bmiIndex<30:
    print(f"Your BMI index is {bmiIndex} and you are slightly overwight.")
elif bmiIndex>=30 and bmiIndex<35:
    print(f"Your BMI index is {bmiIndex} and you are obese.")
else:
    print(f"Your BMI index is {bmiIndex} and you are clinically obese.")
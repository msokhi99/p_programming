'''
Tip Calculator.
'''

print("TIPPING CALCULATOR: ")
print("Enter total bill amount (including taxes): ")
totalBill=float(input())
print("Enter tipping percentage (10,12 or 15): ")
tipPercentage=int(input())
print("Enter the number of people splitting the bill: ")
splitBill=int(input())
billForEachPerson=round(totalBill/splitBill,2)
tipForEachPerson=round(billForEachPerson*(tipPercentage/100),2)
totalForEachPerson="{:.2f}".format(billForEachPerson+tipForEachPerson)
print(f"Each person should pay ${totalForEachPerson}.")
'''
Swap 2 variables.
'''

print("Enter the first item: ")
varA=input()
print("Enter the second item: ")
varB=input()

print(f"Value of varA: {varA} and value of varB: {varB} before switching.")

tempVar=varA
varA=varB
varB=tempVar

print(f"Value of varA: {varA} and value of varB: {varB} after switching.")
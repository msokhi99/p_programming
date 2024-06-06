'''
Password generator.
'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("PASSWORD GENERATOR ")
numLetters=int(input("How many letters do you want in your password - "))
numNumbers=int(input("How many numbers do you want in your password - "))
numSymbols=int(input("How many symbols do you want in your password - "))

generatedPass=[]

for i in range(1,numLetters+1):
    generatedPass.append(letters[random.randint(0,len(letters)-1)])
for i in range(1, numNumbers+1):
    generatedPass.append(numbers[random.randint(0,len(numbers)-1)])
for i in range(1, numSymbols+1):
    generatedPass.append(symbols[random.randint(0,len(symbols)-1)])

random.shuffle(generatedPass)

print("Generated Password: ", *generatedPass,sep="")
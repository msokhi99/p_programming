'''
Adding Even Numbers.
'''

userInput=int(input())
sum=0
for x in range(1,userInput+1):
    if x%2==0:
        sum=sum+x

print(f"Total: {sum}")
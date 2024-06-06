def primeCheck(numOne):
    prime=bool
    primeList=[1,numOne]
    allFactors=[]
    for i in range(1,numOne+1):
        if(numOne%i==0):
            allFactors.append(i)
        if allFactors==primeList:
            prime=True
        else:
            prime=False

    return prime

for i in range(1,1001):
    print(f"{i} -> {primeCheck(i)}")
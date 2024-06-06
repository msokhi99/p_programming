'''
Pizza Order.
'''

print("Thank you for choosing Python Pizza Deliveres !")
pizzaSize=str(input("What kind of pizza do you want: (S), (M) or (L) "))

if pizzaSize=="S":
    addPepForSmall=str(input("Add Pep: (Y) or (N) "))
    addExtraCheese=str(input("Add extra cheese: (Y) or (N) "))
    if addPepForSmall=="Y" and addExtraCheese=="Y":
        totalPrice=18
        print(f"Your final bill is ${totalPrice}")
    elif addPepForSmall=="Y" and addExtraCheese=="N":
        totalPrice=17
        print(f"Your final bill is ${totalPrice}")
    elif addPepForSmall=="N" and addExtraCheese=="Y":
        totalPrice=16
        print(f"Your final bill is ${totalPrice}")
    else:
        totalPrice=15
        print(f"Your final bill is ${totalPrice}")
elif pizzaSize=="M" or pizzaSize=="L":
    addPepForMedLarge=str(input("Add Pep: (Y) or (N) "))
    addExtraCheese=str(input("Add extra cheese: (Y) or (N) "))
    if pizzaSize=="M":
        if addPepForMedLarge=="Y" and addExtraCheese=="Y":
            totalPrice=24
            print(f"Your final bill is ${totalPrice}")
        elif addPepForMedLarge=="Y" and addExtraCheese=="N":
            totalPrice=23
            print(f"Your final bill is ${totalPrice}")
        elif addPepForMedLarge=="N" and addExtraCheese=="Y":
            totalPrice=22
            print(f"Your final bill is ${totalPrice}")
        else:
            totalPrice=20
            print(f"Your final bill is ${totalPrice}")
    else:
        if addPepForMedLarge=="Y" and addExtraCheese=="Y":
            totalPrice=29
            print(f"Your final bill is ${totalPrice}")
        elif addPepForMedLarge=="Y" and addExtraCheese=="N":
            totalPrice=28
            print(f"Your final bill is ${totalPrice}")
        elif addPepForMedLarge=="N" and addExtraCheese=="Y":
            totalPrice=26
            print(f"Your final bill is ${totalPrice}")
        else:
            totalPrice=25
            print(f"Your final bill is ${totalPrice}")
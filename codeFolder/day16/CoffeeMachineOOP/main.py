from menu import MenuItem,Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

dispMenu=Menu()
menuItems=dispMenu.get_items()
userCoffee=str(input(f"{menuItems}"))
userCoffee=dispMenu.find_drink(userCoffee)
newCoffee=CoffeeMaker()
if newCoffee.is_resource_sufficient(userCoffee)==True:
    coffeeToMake=MenuItem
    processMoney=MoneyMachine()
    userPay=processMoney.process_coins()
    processMoney.make_payment(userCoffee.cost)
    newCoffee.make_coffee(userCoffee)
else:
    print("Sorry")

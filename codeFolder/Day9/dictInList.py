travelLog=[
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lillie","Dijon"],
    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    },
]

def addToTravelLog(country, visits, cities):
    travelLog.append({"country":country, "visits":visits, "cities":cities})
    print(travelLog)

def getCountry():
    tempCountry=str(input("Enter country: "))
    return tempCountry
def getVisits():
    tempVisits=int(input("Total visits: "))
    return tempVisits
def getListOfCities():
    tempList=str(input("Enter Cities: ")).split()
    return tempList

addToTravelLog(getCountry(), getVisits(), getListOfCities())
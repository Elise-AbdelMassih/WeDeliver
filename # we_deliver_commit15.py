# we_deliver_commit15.py

#Defining the Driver class to store information about each driver
class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city

#Defining the City class to store information about each city
class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

#Predefined list of Driver objects
drivers = [
    Driver("ID001", "Max Verstappen", "Akkar"),
    Driver("ID002", "Charles Leclerc", "Saida"),
    Driver("ID003", "Rami Mansour", "Jbeil"),
    Driver("ID004", "Karim Saad", "Zahle"),
    Driver("ID005", "Fadi Chamoun", "Bcharre"),
    Driver("ID006", "Roy Daher", "Batroun"),
    Driver("ID007", "Wissam Homsi", "Sour"),
    Driver("ID008", "Anthony Nassar", "Jounieh"),
    Driver("ID009", "Imad Karam", "Tripoli"),
    Driver("ID010", "Jihad Khalil", "Jezzine")

]

#Predefined list of city names
cities= [
    City("Akkar"),
    City("Saida"),
    City("Jbeil"),
    City("Zahle"),
    City("Bcharre"),
    City("Batroun"),
    City("Sour"),
    City("Jounieh"),
    City("Tripoli"),
    City("Jezzine")
]

cityDict = {}
for city in cities:
    cityDict[city.name] = city

cityDict["Akkar"].neighbors = {"Tripoli": cityDict["Tripoli"], "Bcharre": cityDict["Bcharre"]}
cityDict["Tripoli"].neighbors = {"Akkar": cityDict["Akkar"], "Bcharre": cityDict["Bcharre"]}
cityDict["Jbeil"].neighbors = {"Batroun": cityDict["Batroun"], "Zahle": cityDict["Zahle"]}
cityDict["Zahle"].neighbors = {"Saida": cityDict["Saida"], "Jbeil": cityDict["Jbeil"]}
cityDict["Bcharre"].neighbors = {"Tripoli": cityDict["Tripoli"], "Jounieh": cityDict["Jounieh"]}
cityDict["Batroun"].neighbors = {"Jbeil": cityDict["Jbeil"], "Tripoli": cityDict["Tripoli"]}
cityDict["Sour"].neighbors = {"Saida": cityDict["Saida"], "Jezzine": cityDict["Jezzine"]}
cityDict["Jounieh"].neighbors = {"Bcharre": cityDict["Bcharre"], "Zahle": cityDict["Zahle"]}
cityDict["Saida"].neighbors = {"Zahle": cityDict["Zahle"], "Sour": cityDict["Sour"]}
cityDict["Jezzine"].neighbors = {"Saida": cityDict["Saida"], "Sour": cityDict["Sour"]}



#To display the main menu
def firstMenu():
    print("Hello! Please enter:")
    print("1. To go to the drivers' menu")
    print("2. To go to the cities' menu")
    print("3. To exit the system")

    menuNb = input()
    return menuNb

#Function to view all drivers in the system
def viewAllDrivers(drivers):
    if drivers == []:
        print("No drivers available at the moment.")

    else:
        for d in drivers:
            print(f"{d.worker_id}, {d.name}, {d.start_city}")


#Function to add a new driver to the system
def addDriver(drivers, cities):
    dName = input("Enter driver's name: ")
    ddName=dName.lower()   #Converting driver's name to lowercase for case insensitivity
    sCity = input("Enter driver's start city: ")
    ssCity=sCity.lower()   #Converting start city to lowercase for case insensitivity

    #Converting each city name to lowercase for case insensitivity
    lowerCities=[]
    for c in cities:
        lCity=c.lower()
        lowerCities.append(lCity)

    if ssCity not in lowerCities:
        print(f"{sCity} is not available")
        answer = input("Do you want to add it to the database? Please answer by yes or no :")

        if answer.lower() == "yes":
            cities.append(sCity)
            print(f"{sCity} added.")

        else:
            print("Driver not added as start city is unavailable.")
            return
        
    for d in drivers:
        if d.name.lower() == ddName and d.start_city.lower() == ssCity:
            print(f"Driver {dName} with start city {sCity} is already added")
            return
        

    #Generating a unique ID for the new driver
    dId=f"ID{len(drivers) + 1:03}"

    #Creating a new Driver object and adding it to the list of drivers
    newDriver = Driver(dId, dName, sCity)
    drivers.append(newDriver)
    print(f"Driver {newDriver.name}, ID: {dId} was added successfully")

#To display the drivers menu
def driversMenu():
    print("\nDRIVERS' MENU")
    print("Enter:")
    print("1. View all drivers")
    print("2. Add a driver")
    print("3. Go back to main menu")

    menuNb = input()

    if menuNb == "1":
        viewAllDrivers(drivers)
    elif menuNb == "2":
        addDriver(drivers, cities)
    elif menuNb == "3":
        firstMenu()
    else:
        print("Invalid number. Please enter 1, 2, or 3.")


#Function to view all cities in the program
def showCities(cities):
    if len(cities) == 0:
        print("No cities available at the moment.")

    else:
        print("List of all cities:")
        for c in cities:
            print(c)

def printCityNeighbors(cityDict, cities):
    inputCity = input("Enter a city name: ").strip()
    lCity = inputCity.lower()

    found = False
    for city in cities:
        if lCity == city.name.lower():
            found = True
            break

    if not found:
        print(f"City '{inputCity}' not found.")
        return
    
    oCity = None
    for c in cities:
        if c.name.lower() == lCity:
            oCity = c
            break

    if oCity:
        print(f"Neighbors of {city.name}:")
        for i, j in oCity.neighbors.items():
            print(i)
    

printCityNeighbors(cityDict, cities)
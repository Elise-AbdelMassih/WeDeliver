# we_deliver_commit8.py

class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city

class City:
    def __init__(self, name):
        self.name = name

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

cities= ["Akkar", "Saida", "Jbeil", "Zahle", "Bcharre", "Batroun", "Sour", "Jounieh", "Tripoli", "Jezzine"]

def firstMenu():
    print("Hello! Please enter:")
    print("1. To go to the drivers' menu")
    print("2. To go to the cities' menu")
    print("3. To exit the system")

    menuNb = input("Enter your choice: ")
    return menuNb

def viewAllDrivers(drivers):
    if drivers == []:
        print("No drivers available at the moment.")

    else:
        for d in drivers:
            print(f"{d.worker_id}, {d.name}, {d.start_city}")


def addDriver(drivers, cities):
    dName = input("Enter driver's name: ")
    ddName=dName.lower()
    sCity = input("Enter driver's start city: ")
    ssCity=sCity.lower()

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
        
    dId=f"ID{len(drivers) + 1:03}"

    newDriver = Driver(dId, dName, sCity)
    drivers.append(newDriver)
    print(f"Driver {newDriver.name}, ID: {dId} was added successfully")


addDriver(drivers, cities)
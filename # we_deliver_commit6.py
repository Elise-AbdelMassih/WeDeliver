# we_deliver_commit6.py

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
    Driver("ID004", "Karim Saad", "Jbeil"),
    Driver("ID005", "Fadi Chamoun", "Jbeil"),
    Driver("ID006", "Roy Daher", "Jbeil"),
    Driver("ID007", "Wissam Homsi", "Jbeil"),
    Driver("ID008", "Anthony Nassar", "Jbeil"),
    Driver("ID009", "Imad Karam", "Tripoli"),
    Driver("ID010", "Jihad Khalil", "Jbeil")

]


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


viewAllDrivers(drivers)

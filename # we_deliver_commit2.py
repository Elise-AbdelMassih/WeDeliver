# we_deliver_commit2.py

class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city

class City:
    def __init__(self, name):
        self.name = name


print("Hello! Please enter:")
print("1. To go to the drivers' menu")
print("2. To go to the cities' menu")
print("3. To exit the system")

menuNb = input("Enter your choice: ")
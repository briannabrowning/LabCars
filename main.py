# create the base Vehicle class to store the data about each

class Vehicle:
    def __init__(self, make, miles, price):    # initalize it
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False       # set engine_on to false

    # adding methods
    def start_engine(self):
        print("Starting engine")     # print a messgae
        engine_on = True             # sets engine_on to true

    def make_noise(self):
        print("Beep beep!")

# create a dervied class from Vehicle named Truck
class Truck(Vehicle):
    def __init__(self, make, miles, price):  # initalize it
        self.make = make
        self.miles = miles
        self.price = price
        self.cargo = False          # set cargo to false

    # adding methods
    def load_cargo(self):
        print("Loading the truck bed...")
        cargo = True                # sets cargo to true

# create a derived class from Vehicle named Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):      # initialize it
        self.make = make
        self.miles = miles
        self.price = price
        self.top_speed = top_speed
    # override methods
    def make_noise(self):
        print("Vroom vroom!")


# create 3 instances of both subclasses & store in appropriate lists
t1 = Truck("Toyota",1000, "$3000")
t2 = Truck("Ford", 20000, "5000")
t3 = Truck("Chevy", 5000, "20000")

b1 = Motorcycle("Harley", 0, "$50000", 300)
b2 = Motorcycle("Ducati", 1000, "$50000", 250)
b3 = Motorcycle("Honda", 20000, "$50000", 240)

# create 2 lists: bikes & trucks
trucks = [t1, t2, t3]
bikes = [b1, b2, b3]

# ask user input what they want to view, bikes or trucks
while True:
    choice = input("Would you like to view bikes or trucks? (b/t) ")
    if choice == "t":
        for i in trucks:
            print(f"{i.make}: with {i.miles}, costs {i.price}")
            i.make_noise()
    elif choice == "b":
        for i in bikes:
            print(f"{i.make} with {i.miles} and a top speed of {i.top_speed} costs {i.price}")
            i.make_noise()

    else:
        choice = input("Invalid choice. Please enter b or t ")

# ask user if they want to compare a vechicle
# empty list vehicles_to_compare to fill with users selections
vehicles_to_compare = []
while True:
    compare = input("Would you like to comapre one of the vechicles? y/n ")
    if compare == "y";
        choose_compare = int(input("Which vechicle would you like to compare? (please list number) "))

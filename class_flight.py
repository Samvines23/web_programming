class flight():
    def __init__(self, capacity):
        self.capacity = capacity    #max capacity of flight
        self.passengers = []   # empty list of passangers which can be populated later
    
    def add_passenger(self, name):
        if len(self.passengers) == self.capacity:    # can also be written as if not self.open_seats
            return False
        else:
            self.passengers.append(name)   #this function adds the passenger's name to the flight class
            return True

    def open_seats(self):
        return (self.capacity - len(self.passengers))   #returns the number of seats left

flight = flight(3)
print(flight.passengers)
print(flight.capacity)
print(flight.open_seats())
flight.add_passenger("Wank")
print(flight.open_seats())
flight.add_passenger("Gimp")
print(flight.open_seats())
people = ["Lewis", "Steve", "Sarah", "Turd","twat"]

for person in people:
    success = flight.add_passenger(person)
    if success == True:
        print(f"{person} added to flight")
    else:
        print(f"unsuccessful, {person} not added to flight")

print(len(flight.passengers))
print(flight.passengers)
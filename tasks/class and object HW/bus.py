class Bus:
    def __init__(self, brand, seats):
        self.brand = brand
        self.seats = seats

    def drive(self):
        print(self.brand, "bus is driving")

bus1 = Bus("Volvo", 50)
bus2 = Bus("Tata", 40)
bus3 = Bus("Ashok Leyland", 45)
bus4 = Bus("Mercedes", 55)
bus5 = Bus("Eicher", 35)

bus_list = [bus1, bus2, bus3, bus4, bus5]

print("----- Bus Details -----")
for bus in bus_list:
    if bus.seats >= 40:
        print("Brand:", bus.brand, "| Seats:", bus.seats)

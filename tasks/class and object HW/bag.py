class Bag:
    def __init__(self, color, capacity):
        self.color = color
        self.capacity = capacity

    def carry(self):
        print("The", self.color, "bag is used to carry items")

bag1 = Bag("Black", 20)
bag2 = Bag("Blue", 25)
bag3 = Bag("Red", 15)
bag4 = Bag("Green", 30)
bag5 = Bag("White", 10)

bag_list = [bag1, bag2, bag3, bag4, bag5]

print("----- Bag Details -----")
for bag in bag_list:
    if bag.capacity >= 20:
        print("Color:", bag.color, "| Capacity:", bag.capacity)

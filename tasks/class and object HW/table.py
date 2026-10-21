class Table:
    def __init__(self, material, shape):
        self.material = material
        self.shape = shape

    def use(self):
        print("The", self.shape, "table is used for studying")

table1 = Table("Wood", "Rectangle")
table2 = Table("Glass", "Square")
table3 = Table("Plastic", "Round")
table4 = Table("Metal", "Rectangle")
table5 = Table("Wood", "Square")

table_list = [table1, table2, table3, table4, table5]

print("----- Table Details -----")
for table in table_list:
    if table.material == "Wood":
        print("Material:", table.material, "| Shape:", table.shape)

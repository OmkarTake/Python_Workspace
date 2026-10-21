class Mobile:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def call(self):
        print("Calling using", self.brand, "mobile")

mobile1 = Mobile("Samsung", "8GB")
mobile2 = Mobile("Apple", "6GB")
mobile3 = Mobile("OnePlus", "12GB")
mobile4 = Mobile("Vivo", "8GB")
mobile5 = Mobile("Redmi", "4GB")

mobile_list = [mobile1, mobile2, mobile3, mobile4, mobile5]

print("----- Mobile Details -----")
for mobile in mobile_list:
    if mobile.ram in ["8GB", "12GB"]:
        print("Brand:", mobile.brand, "| RAM:", mobile.ram)

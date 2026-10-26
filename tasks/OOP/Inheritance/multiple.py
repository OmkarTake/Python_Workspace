class Husband:
    def cash(self):
        print("My cash is yours")

    def car(self):
            print("DAD Tata Nexon")
class wife:
    def jwellery(self):
        print("My gold is yours")

    def car(self):
        print(" Mumma Tata nexon")

class child(Husband, wife):
    def happy(self):
        print("Everything is mine")

    
jay = child()
jay.car()
jay.cash()
jay.jwellery()
print(child.__mro__)  # Method resoluttion order
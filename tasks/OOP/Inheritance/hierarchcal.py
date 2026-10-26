class p1:
    def m1(self):
        print("p[arent of all  method m1")


class C1(p1):
    def m2(self):
        print(" child method p1")


class C2(p1):
    def m3(self):
        print("Child method p1")

class C3(p1):
    def m4(self):
        print("Third child of p1")

jay = C1()
veeru = C2()
basanti = C3()
jay.m1()
veeru.m1()
basanti.m1()
print(veeru.__mro__)  # Method resoluttion order
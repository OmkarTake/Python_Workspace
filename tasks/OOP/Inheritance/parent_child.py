class GP:
    def m1(self):
        print("Grandparent method m1")


class P(GP):
    def m2(self):
        print("Parent method m2")


class C(P):
    def m3(self):
        print("Child method m3")


jay = C()

jay.m1()
jay.m2()
jay.m3()
print(jay.__mro__)  # Method resoluttion order
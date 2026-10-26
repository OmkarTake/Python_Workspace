class Student:

    def __init__(self, r, nm):
        self.__roll = r
        self.__name = nm

    def change_name(self,nr):
        self.__roll = nr

    def  display(self):
        print(self.__roll)

s1 = Student(21,"Omkar")
s1.display()
print(s1.__roll)

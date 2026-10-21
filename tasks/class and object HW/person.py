class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name, "and my age is", self.age)

person1 = Person("Rahul", 22)
person2 = Person("Amit", 25)
person3 = Person("Priya", 21)
person4 = Person("Sneha", 24)
person5 = Person("Rohan", 23)

person_list = [person1, person2, person3, person4, person5]

print("----- Person Details -----")
for person in person_list:
    if person.age >= 23:
        print("Name:", person.name, "| Age:", person.age)

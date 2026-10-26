class Person:
    def person_details(self):
        print("This is a person")


class Student(Person):
    def student_details(self):
        print("This person is a student")


class Teacher(Person):
    def teacher_details(self):
        print("This person is a teacher")


class Sports(Student):
    def sports_details(self):
        print("Student participates in sports")


class Research(Teacher):
    def research_details(self):
        print("Teacher performs research")


# Multiple inheritance
class StudentTeacher(Sports, Research):
    def student_teacher_details(self):
        print("This person is both student and teacher")


# Object creation
obj = StudentTeacher()

obj.person_details()
obj.student_details()
obj.teacher_details()
obj.sports_details()
obj.research_details()
obj.student_teacher_details()
print(obj.__mro__)  # Method resoluttion order
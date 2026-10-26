class Student:
    def __init__(self, name, rollno, marks, email, course):
        self.__name = name
        self.__roll_no = rollno
        self.__marks = marks
        self.__email = email
        self.__course = course

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

s1 = Student("Omkar",101,85,"omkar@gmail.com","Python full Stack")
print("-----------  Original Student Details --------")
print(f"Name : {s1.get_name()}")
print(f"Roll No : {s1.get_roll_no()}")
print(f"Marks : {s1.get_marks()}")
print(f"Email : {s1.get_email()}")
print(f"Course : {s1.get_course()}")

print("--------- Updated Student Details ------------")
s1.set_name("Rahul")
print("Name : ",s1.get_name())
s1.set_roll_no(102)
print(f"Roll No : {s1.get_roll_no()}")
s1.set_marks(92)
print(f"Marks : {s1.get_marks()}")
s1.set_email("Rahul@gmail.com")
print(f"Email : {s1.get_email()}")
s1.set_course("Java Full Stack")
print(f"Course : {s1.get_course()}")



def login_validation(usr,pwd,eml):
    #username = input("Enter username: ")
    #password = input("Enter password: ")
    #email = input("Enter email: ")

    if len(usr) <= 3:
        print("Invalid username: Must contain more than 3 characters")

    elif len(pwd) < 8 or not any(i.isdigit() for i in pwd):
        print("Invalid password: Must have at least 8 characters and one number")

    elif "@" not in eml :
        print("Invalid email: Must contain @ and .")

    else:
        print("Your entered data is correct!")

login_validation("Omkar","Omkar1234","Omkar@123")

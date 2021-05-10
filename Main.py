import csv

def login():
    valid_usernames = []
    valid_passwords = []

    username = str(input("Username: "))
    password = str(input("Password: "))

    with open("Credentials.csv", "r") as csv_file:
        reader  = csv.reader(csv_file)
    
        next(reader)

        for line in reader:
            valid_passwords.append(line[1])

    with open("Credentials.csv", "r") as csv_file:
        reader1 = csv.reader(csv_file, delimiter = ",")
    
        next(reader1)

        for line in reader1:
            valid_usernames.append(line[0])

    if username in valid_usernames:
        if password in valid_passwords:
            print("Login Success!")

    else:
        print("Login Failed")
        print("Username/Password is invalid")

def register():
    username = input(str("Please Enter New Username: "))
    user_password = input(str("Please Enter New Password: "))

    add_row = [username, user_password]

    with open('Credentials.csv', 'a+', newline = "\n") as writer_obj:
        writer1 = csv.writer(writer_obj)
        writer1.writerow(add_row)

loginorreg = input("Would you like to login or register?")

if loginorreg.lower() == "register":
    register()

elif loginorreg.lower() == "login":
    login()

else:
    print("Please tpe 'login' or 'register'")

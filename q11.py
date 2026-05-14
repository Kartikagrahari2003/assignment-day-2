# Predefined valid usernames and corresponding passwords Checker

x = {}

def add_user():
    username = input("Enter your user name: ")
    password = input("Enter your password: ")

    if username not in x:
        x[username] = password
        print("User added successfully...")
    else:
        print("Username already exists...")

def search():
    username = input("Enter your user name: ")
    password = input("Enter your password: ")

    if username in x and x[username] == password:
        print("Login successful...")
    else:
        print("Wrong username or password...")

# Main Program
while True:
    print("\n1. Add User")
    print("2. Login")
    print("3. Exit")

    choose = int(input("Enter your choice: "))

    if choose == 1:
        add_user()

    elif choose == 2:
        search()

    elif choose == 3:
        print("Program Ended...")
        break

    else:
        print("Invalid Choice...")
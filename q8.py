# You are building a registration system that only accepts email addresses from a certain domain (e.g. "gmail.com")

a = {}

name= input("Enter your name : ")
email = input("Enter your e mail : ")
find = "@gmail.com"

if find in email:
    a[name] = email
    print("Congratulation..... Added name and email suscessfully....")
else:
    print("Email is invalid")

print(a)




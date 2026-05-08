# Retirement Age Calculator 
print("Retirement Age Calculator ")
x = int(input("Enter your age:::"))

if x <=65:
    x= 65 -x
    print(f"You have {x} left to retirement....")
else:
    print("Your age is more than 65 years....You are useless person for our company.... get lost...")
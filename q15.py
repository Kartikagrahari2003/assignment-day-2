# Tax Calculation for Car Purchase 

print("Tax calculator on car😊")
print("You have options to choose:::")
print("""
a. Mahindra 
b. Audi 
c. Jagur
d. Mercedge
""")
chosse=input("Choose your car ::: ").lower()

if chosse == "mahindra":
    price = int(input("Enter your budget in lakhs ::: "))
    if price >= 7 and price <= 10:
        tax= (price* 0.05)+ price
        print(f"You have choose {chosse}... Car's price after tax {tax} lakhs..")
    elif price < 7 or price > 10:
        print(f"We don't have car in this {price} lakhs price, Sorry...")

elif chosse == "audi":
    price = int(input("Enter your budget in lakhs ::: "))
    if price >= 10 and price <= 15:
        tax= (price* 0.1)+ price
        print(f"You have choose {chosse}... Car's price after tax {tax} lakhs..")
    elif price < 10 or price > 15:
        print(f"We don't have car in this {price} lakhs price, Sorry...")

elif chosse == "jagur":
    price = int(input("Enter your budget in lakhs ::: "))
    if price >= 15 and price <= 25:
        tax= (price* 0.25)+ price
        print(f"You have choose {chosse}... Car's price after tax {tax} lakhs..")
    elif price < 15 or price > 25:
        print(f"We don't have car in this {price} lakhs price, Sorry...")

elif chosse == "mercedge":
    price = int(input("Enter your budget in lakhs ::: "))
    if price >= 20 and price <= 25:
        tax= (price* 0.3)+ price
        print(f"You have choose {chosse}... Car's price after tax {tax} lakhs..")
    elif price < 20 or price > 25:
        print(f"We don't have car in this {price} lakhs price, Sorry...")





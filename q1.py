# write a program that takes input for the cost price and selling price of an item. 

print("Profit loss calculator for shopkeeper")

x= float(input("Enter the cost price:::"))
y= float(input("Enter the selling price:::"))

# Calculating profit 
if y>=x:
    z = y - x
    a= (z/x)*100
    print(f"You are in profit...\nProfit = {z}\nProfit percentage is{a}%")
else:
    z = x-y
    a= (z/x)*100
    print(f"You are in loss...\nLoss = {z}\nLoss percentage is{a}%")

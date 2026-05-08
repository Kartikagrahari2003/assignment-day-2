# q1
print("Profit loss calculator for shopkeeper")

b = int(input("Enter number of items ::: "))
x = float(input("Enter the cost price ::: "))
y = float(input("Enter the selling price ::: "))

# Total prices
cp = b * x
sp = b * y

# Calculating profit/loss
if sp > cp:
    z = sp - cp
    a = (z / cp) * 100

    print(f"You are in profit...")
    print(f"Profit = {z}")
    print(f"Profit percentage is {a}%")

elif cp > sp:
    z = cp - sp
    a = (z / cp) * 100

    print(f"You are in loss...")
    print(f"Loss = {z}")
    print(f"Loss percentage is {a}%")

else:
    print("No profit no loss")
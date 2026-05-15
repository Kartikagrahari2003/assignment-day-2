data = {}

print("Library Charge Calculator 😊")

apna = input("Enter your name ::: ")

date = int(input("Kitne dino ke liye chahiye ::: "))

books = []

num = int(input("Kitni books borrow kar rahe ho ::: "))

for i in range(num):
    book = input(f"Enter name of book no {i+1} ::: ")
    books.append(book)

# price calculation
if date > 0 and date <= 5:
    price = date * 2 * num

elif date > 5 and date <= 10:
    price = date * 3 * num
  
elif date > 10 and date <= 15:
    price = date * 4 * num

else:
    price = date * 5 * num

data[apna] = books

print(f"You have borrowed {data[apna]}")
print(f"Payable amount is {price}")

# file open
file = open("librarydata.txt", "a")

# data save
file.write(f"Name: {apna}\n")
file.write(f"Books: {books}\n")
file.write(f"Days: {date}\n")
file.write(f"Price: {price}\n")
file.write("----------------------\n")

# file close
file.close()

print("Data saved in librarydata.txt")

    
    





# Create a javascript program to calculate a student's grade based on their marks. 

name = input("Enter student name : ")
marks = int(input("Enter your marks : "))

# Grade Calculation
if 90 <= marks <= 100:
    grade = "A"

elif 80 <= marks <= 89:
    grade = "B"

elif 70 <= marks <= 79:
    grade = "C"

elif 60 <= marks <= 69:
    grade = "D"

elif 50 <= marks <= 59:
    grade = "E"

elif 0 <= marks <= 49:
    grade = "F"

else:
    grade = "Invalid"

# Output
if grade != "Invalid":

    print(f"Student Name : {name}")
    print(f"Marks : {marks}")
    print(f"Grade : {grade}")

    # Save data in file
    with open("Marksgrade.txt", "a") as f:
        f.write(f"Name : {name}\n")
        f.write(f"Marks : {marks}\n")
        f.write(f"Grade : {grade}\n")
        f.write("----------------------\n")

    print("Data saved successfully in Marksgrade.txt")

else:
    print("Invalid marks! Please enter marks between 0 and 100.")               
                

    
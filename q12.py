# .Employee Salary Based on Experience. 

employee= {}

name= input("Enter your name :::: ")
exp = int(input("Enter your experince ::: "))
sallary = 8000
employee[name]= exp

file = open("employee.txt", "a")
if employee[name]>= 10 and employee[name]<=15 :
    a= (f"{name} you have more than {employee[name]} years... You are a Senior Employee and your sallary is {sallary}  ")
    print(a)
    file.write(a + "\n")
elif employee[name] > 15:
    sallary += 5000
    a = (f"{name} you have more than {employee[name]} years... You are a Senior Employee and your salary is {sallary}")
    print(a)
    file.write(a + "\n")
else:
    print("You have less than 10 years of exp...")
file.close

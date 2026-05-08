# : Bank Loan Approval System
print("Bank Loan Approval System")
x= int(input("Enter your age :::"))

if x>=18 and x <= 60:
    income= float(input("Enter your monthly income : "))
    if income >= 25000:
        credit = float(input("Enter your credit score :::"))
        if credit>= 700:
            debit= float(input("Enter your outstanding debts :::"))
            if debit<=10000:
                print("Loan Approved")
            else:
                print("High debit... Loan rejected")
        else:
            print("Low creadit score... Loan rejected")
    else:
        print("Low income... Loan rejected")
else:
    print("Age is too low or high....... Loan rejected")




# Students Interview Eligibility Checker 
print("Students Interview Eligibility Checker")

score= float(input("Enter your Acadmic marks in precentage ::: "))
if score>= 60:
    atten= float(input("Enter your Acadmic attendence in precentage ::: "))
    if atten >= 75:
        extra= input("KAbhi kuch extra carriculam activity kre hai.... y/n :::")
        if extra== "y":
            print("App interview ke liye eligible for interview")
        else:
            print("App mumbai anhi aa sakte.... Interview ke liye... App ne koi bhi carriculam activity nahi ki hai")
    else:
        print("App ki attendence kam hai...... You are rejected...")
else:
    print("Low percentage... try again next time...")


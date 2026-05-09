x={}

y= int(input("No of sub :::"))

for i in range(y):
    subjects = input("Enter your subject::")
    marks = int(input("Emter marks:::"))
    
    x.update({subjects: marks})

for subject, mark in x.items():
    print(f"Subject : {subject} : Marks : {mark}")

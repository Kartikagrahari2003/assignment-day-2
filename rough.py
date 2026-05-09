# # Validating Email Domain 

# x= {
#         "name" : ["a", "b", "c","d"],
#         "age" : [10,12,13,14],
#         "subjects" : {
#             "phy" : 75,
#             "maths" : 55,
#             "hindi" : 76,
#         }
# }

# # print(type(x))

# # print(x, end="/n")

# # x["name"] = input("Enter your name:::") # Overwrite 
# # x["age"] = int(input("Enter your age"))
# # print(x)

# # print(x.keys())
# # print(list(x.keys()))
# # print(len(list(x.keys())))
# # print(x.values())
# # print(x.items())
# # print(x.get("name"))
# # print(x.get("subjects"))

# # y = list(x.items())
# # print(y[1]) # indivisual list ke item ko print krne ke liye dict me

# x.update({"City" : "Delhi"}) # New dict update in existing dict

# print(x)
#  duplicate keys are not allowed
# __________________________________________

# x = {1, 2, 3, 4}

# print(x)
# print(type(x))

# Create an empty set

# x = {}
# y = set() # empty set

# print(type(x))
# print(type(y))

# _______________________ Set method____

# 1. set.add(el) add element _______ set are muteable but valued are immutable
#  2. set.remove(el) 
#  3. set.clear(el) 
#  4. set.pop(el) remove a random value
#  5. set.union(set2) combine both set values and return new
#  6. seet.intersection(set2) combine commen value and return new.
# y.add(1)
# y.add(2)
# y.add(3)
# y.add(4)
# y.add(5)

# print(y)

# y.remove(2)
# print(y)

# y.clear()


# print(len(y))

#  5. set.union(set2) combine both set values and return new

# set1= {1,2,3,4,5}
# set2= {4,5,6,7,8,9}

# y = set1.union(set2)
# print(y)
# #  6. seet.intersection(set2) combine commen value and return new.

# print(set1.intersection(set2))

# dict= {
#     "cat": "A samll animal",
#     "table": ("A" , "B")
# }

# print(dict)

# x= {
#     "p", "j", "cp", "p", "js", "j","p","p","j","cp","c"
# }

# print(len(x))

x={}

y= int(input("No of sub :::"))

for i in range(y):
    subjects = input("Enter your subject::")
    marks = int(input("Emter marks:::"))
    
    x.update({subjects: marks})

for subject, mark in x.items():
    print(f"Subject : {subject} : Marks : {mark}")





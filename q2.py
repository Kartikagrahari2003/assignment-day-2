#  Write a script to analyze cricket stats for a team. 

print("Run calculator")
x=int(input("Enter the number of players:::"))

run= 0
avg=0
for i in range(1,x+1):
    y= int(input(f"Enter Run of player {i} ::: "))
    run = run + y
avg= run/x
print(f"Total run: {run}")
print(f"Average run : {avg}")
# Solved
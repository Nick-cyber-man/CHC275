print("1. New Player")
print("2. Returning Player")
Option = input("Are you a new or returning memeber?")

file = open("Accounts.txt","r")
buffer = file.readlines()

print(buffer)
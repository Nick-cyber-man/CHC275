file = open("Accounts.txt","r")
buffer = file.readlines()

print("1. New Player")
print("2. Returning Player")
option = input("Are you a new or returning memeber?")

check = False
if option == "1":
    Accountnames = []
    Passwords = []
    Balances = []
    
    
    accountname = input("What would you like your account name to be?")
    password = input("What would you like the password for the account to be?(has to be 5 numbers in length)")
    Balance = input("How much money do you want in your account?")
    
    if accountname.isalpha() and password.isnumeric() and len(password) < 5:
        Accountnames.append(accountname)
        Passwords.append(password)
        Balances.append(Balance)

    else:
        print("This password is too long and or short, make sure it is 5 numbers long")

    check = True

    

    
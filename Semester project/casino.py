file = open("Accounts.txt","r")
buffer = file.readlines()
Accountnames = []
Passwords = []
Balances = []
for line in buffer:
    line = line.strip()
    line = line.split(",")
    Accountnames.append(line[0])
    Passwords.append(line[1])
    line[2] = int(line[2]) 
    Balances.append(line[2]) 
file.close()     

print("1. New Player")
print("2. Returning Player")
option = input("Are you a new or returning memeber?")

check = False
if option == "1":

    
    accountname = input("What would you like your account name to be?")
    if accountname in Accountnames:
        print("This account already exists")
    else:
        password = input("What would you like the password for the account to be?(has to be 5 numbers in length)")
        Balance = input("How much money do you want in your account?")

        if accountname.isalpha() and password.isnumeric() and len(password) == 5:
            Accountnames.append(accountname)
            Passwords.append(password)
            Balances.append(Balance)
            file = open("Accounts.txt", "a")
            line = f"{accountname},{password},{Balance}\n"
            file.write(line)
            file.close()
            print (f"Your Account name is: {accountname}, The password to your account is:{password}, Your starting balance is: {Balance}")
        else:
                print("This password is too long and or short, make sure it is 5 numbers long")
 
if option == "2":
    notcheck = False
    i = 0 
    pickedaccount = input("What account would you like to use?")
    pickedpassword = input("What is the password for this account?")

    while notcheck == False and i < len(Accountnames):
        
        if pickedaccount == Accountnames[i] and pickedpassword == Passwords[i]: 
            accountname = Accountnames[i]
            password = Passwords[i]
            Balance = Balances[i]
            notcheck == True
            print (f"Your Account name is: {accountname}, The password to your account is:{password}, Your starting balance is: {Balance}")
        i = i + 1
          
    check = True



    


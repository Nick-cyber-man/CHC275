#Alex Godat, Nick Zebeck
check = False
Accountnames = ["jake" , "mark" , "derek"]
Accountbalance = [100,200,300]
while check == False:
    print("Welcome to the bank")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Tranfer")
    print("4. List Accounts/Account Balance")
    print("5. add account")
    print("6. remove account")
    print("7. quit")
    option = input("What action would you like? ")

    if option == "1":
        x = input("how much would you like to Withdraw? ")
        y = input("Which account would you like to Withdraw from? ")
        x = int(x)
        index = Accountnames.index(y)
        Accountbalance[index] = Accountbalance[index] - x
        for i in range(len(Accountnames)):
            print(f"Bank Account {Accountnames[i]}. Accountbalance: {Accountbalance[i]}")
    elif option == "2":
        x = input("how much would you like to deposit? ")
        y = input("Which account would you like to deposit into? ")
        x = int(x)
        index = Accountnames.index(y)
        Accountbalance[index] = Accountbalance[index] + x
        for i in range(len(Accountnames)):
            print(f"Bank Account {Accountnames[i]}. Accountbalance: {Accountbalance[i]}")
    elif option == "3":
        x = input("how much would you like to transfer? ")
        x = int(x)
        y = input("Which account would you like to transfer money from? ")
        transfer = input("what account would you like to add money to? ")
        index = Accountnames.index(y)
        index2 = Accountnames.index(transfer)
        Accountbalance[index] = Accountbalance[index] - x
        Accountbalance[index2] = Accountbalance[index2] + x
        for i in range(len(Accountnames)):
            print(f"Bank Account {Accountnames[i]}. Accountbalance: {Accountbalance[i]}")
    elif option == "4":
        for i in range(len(Accountnames)):
            print(f"Bank Account {Accountnames[i]}. Accountbalance: {Accountbalance[i]}")
    elif option == "5":
        newaccount = input("what is the name of the new account you would like to add? ")
        Accountnames.append(newaccount)
        newbalance = input("What is the balance of the account that was added? ")
        Accountbalance.append(newbalance)
        for i in range(len(Accountnames)):
            print(f"Bank Account {Accountnames[i]}. Accountbalance: {Accountbalance[i]}")
    elif option == "6":    
        minusnames = input("What account would you like to remove? ")
        index = Accountnames.index(minusnames)
        Accountnames.pop(index)
        Accountbalance.pop(index)
        for i in range(len(Accountnames)):
            print(f"Bank Account {Accountnames[i]}. Accountbalance: {Accountbalance[i]}")
    elif option == "7":
        print("Have a nice day ")
        check = True


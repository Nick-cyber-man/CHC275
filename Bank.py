#Alex Godat, Nick Zebeck
check = False
Accountnames = ["jake" , "mark" , "derek"]
Accountbalance = [100,200,300]
while check == False:
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Tranfer")
    print("4. List Accounts/Account Balance")
    print("5. quit")
    option = input("What action would you like? ")

    if option == "1":
        print("option 1 ")
    elif option == "2":
       x = input("how much would you like to deposit? ")
       x = int(x)
    for deposit in Accountbalance:
        deposit = deposit + Accountbalance
    elif option == "3":
        print("option 3 ")
    elif option == "4":
        for i in range(len(Accountnames)):
            print(f"Bank Account {Accountnames[i]}. Accountbalance: {Accountbalance[i]}")
    elif option == "quit":
        check = True


#accountnames.index("mark") return 1
#accountnames.index(name) return whichever index the name they typed is in 

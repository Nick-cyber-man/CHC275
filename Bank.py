#Alex Godat, Nick Zebeck
check = False
Accountnames = []
Accountbalance = []
while check == False:
    print("Welcome to the Bank")
    option = input("Who are you? ")

    for i in range(len(Accountnames)):
        print(f"Bank Account {Accountnames[i]}. Accountbalance: {Accountbalance[i]}")
    

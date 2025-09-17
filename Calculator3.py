
check = False 
while check == False:
    print("welcome to calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    option = input("what operation would you like? ")

    if option == "1":
        x = input("what value of x would you like? ")
        y = input("what value of y would you like? ")
        x = int(x)
        y = int(y)
        print(x + y )
    elif option == "2":
        x = input("what value of x would you like? ")
        y = input("what value of y would you like? ")
        x = int(x)
        y = int(y)
        print(x - y)
    elif option == "3":
        x = input("what value of x would you like? ")
        y = input("what value of y would you like? ")
        x = int(x)
        y = int(y)
        print(x * y)
    elif option == "4":
        x = input("what value of x would you like? ")
        y = input("what value of y would you like? ")
        x = int(x)
        y = int(y)
        print(x / y)
        check = True
    
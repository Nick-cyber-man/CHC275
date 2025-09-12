print("welcome to calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option = input("what operation would you like? ")
x = input("what value of x would you like? ")
y = input("what value of y would you like? ")
x = int(x)
y = int(y)
if option == "1":
    print(x + y )
elif option == "2":
    print(x - y)
elif option == "3":
    print(x * y)
elif option == "4":
    print(x / y)
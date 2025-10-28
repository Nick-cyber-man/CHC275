x = "some value"
x = int(x)
print(x+5)

try:
    x = input("enter num 1: ")
    y = input("enter num 2: " )
    x = int(x)
    y = int(y)
    quotient = x/y
    print(quotient)
except ValueError:
    print("x and y must be numbers")
except ZeroDivisionError:
    print("y must be nonzero")
    
    
try:
    x = [1,2,3]
    y = input("enter num 2: " )
    x = int(x)
    y = int(y)
    quotient = x/y
    print(quotient)
except ValueError:
    print("x and y must be numbers")
except ZeroDivisionError:
    print("y must be nonzero")
except TypeError:
    print("variables must be intergers")
except Exception as e:
    print(e)
finally:
    print("thanks for using the calculator")
    
    
    
check = False 
try:
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
except ValueError:
    print("x and y must be numbers")
except ZeroDivisionError:
    print("y must be nonzero")
except TypeError:
    print("variables must be intergers")
except Exception as e:
    print(e)
    check = True
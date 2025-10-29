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
        try:
            x = input("what value of x would you like? ")
            y = input("what value of y would you like? ")
            x = int(x)
            y = int(y)
            print(x + y )
        except ValueError:
            print("x and y must be numbers")
        except ZeroDivisionError:
            print("y must be nonzero")
        except TypeError:
            print("variables must be intergers")
        except Exception as e:
            print(e)
    elif option == "2":
        try:
            x = input("what value of x would you like? ")
            y = input("what value of y would you like? ")
            x = int(x)
            y = int(y)
            print(x - y)
        except ValueError:
            print("x and y must be numbers")
        except ZeroDivisionError:
            print("y must be nonzero")
        except TypeError:
            print("variables must be intergers")
        except Exception as e:
            print(e)
    elif option == "3":
        try:    
            x = input("what value of x would you like? ")
            y = input("what value of y would you like? ")
            x = int(x)
            y = int(y)
            print(x * y)
        except ValueError:
            print("x and y must be numbers")
        except ZeroDivisionError:
            print("y must be nonzero")
        except TypeError:
            print("variables must be intergers")
        except Exception as e:
            print(e)
    elif option == "4":
        try:
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
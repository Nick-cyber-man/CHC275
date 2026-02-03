def add(x,y):
    return  x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y
    
def divide(x,y):
    return x/y

def pow(x,y):
    return x**y

def main():
    print("welcome to the Calculator")
    print("1.Addition")
    print("2.Subtract")
    print("3.Multiplication")
    print("4.Division")
    print("5.To the Power of")
    print("exit")
    option = input ("select you operatiion or type exit")
    if option == "1":
        num1=input("enter num1:")
        num2=input("enter num2:")
    try:
        num1 = int(num1)
        num2=int(num2)

    except Exception as e:
        print(e)
    finally:
        sum = add(num1,num2)
        print(f" your sum of num1 and num 2 is {sum}")
        
    if option == "2":
        num1=input("enter num1:")
        num2=input("enter num2:")
    try:
        num1 = int(num1)
        num2=int(num2)

    except Exception as e:
        print(e)
    finally:
        difference = subtract(num1,num2)
        print(f" your difference of num1 and num 2 is {difference}")
    if option == "3":
        num1=input("enter num1:")
        num2=input("enter num2:")
    try:
        num1 = int(num1)
        num2=int(num2)

    except Exception as e:
        print(e)
    finally:
        product = multiply(num1,num2)
        print(f" your product of num1 and num2 is {product}")
    if option == "4":
        num1=input("enter num1:")
        num2=input("enter num2:")
    try:
        num1 = int(num1)
        num2=int(num2)

    except Exception as e:
        print(e)
    finally:
        quotient = divide(num1,num2)
        print(f" your quotient of num1 and num 2 is {quotient}")
    if option == "5":
        num1=input("enter num1:")
        num2=input("enter num2:")
    try:
        num1 = int(num1)
        num2=int(num2)

    except Exception as e:
        print(e)
    finally:
        Power = pow(num1,num2)
        print(f" your powered of num1 and num 2 is {Power}")
    if option == "exit":
        pass
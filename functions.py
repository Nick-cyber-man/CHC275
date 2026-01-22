def foo():
    print("bar")
    
foo ()

def add5(num):
    num = num + 5
    print(num)
    
add5(8)
add5(4)

mynum = 10
add5(mynum)

def multiply(num1,num2):
    product = num1 * num2
    print(product)
    
multiply(3,5)
multiply(4,5)
multiply(4,"a")

def add(num1,num2):
    sum=num1+num2
    print(sum)
    
add(2,5)
add("hello","world")

def update(num1):
    num1 = num1 + 10
x = 5
update(x)
print(x)

mylist = [1,2,3,4]
print(mylist)
def update2(num5):
    num5.append(5)
    
update2(mylist)
print(mylist)


def foo(x):
    factor = 0.2
    print(factor)
    print(x*factor)

foo(5)
foo(100)

def updatebalance(money,change):
    money = money - change
    return money
print("return example")
balance = 500
print(balance)
balance = updatebalance(balance,200)
print(balance)
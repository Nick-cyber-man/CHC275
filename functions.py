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
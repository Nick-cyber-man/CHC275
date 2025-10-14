money = input("Enter your value: ")
money = int(money)

mystr = "hello"
for char in mystr:
    print(char)
    
for i in range(len(mystr)):
    print(mystr[i])
    
mystr = "         hello"
print(mystr)
mystr = mystr.strip()
print(mystr)

mystr = "         Hello"
mystr = mystr.strip().lower()
print(mystr)

money = "10a"
if money.isnumeric():
    money = int(money)
    val = money + 5
    print(val)
else:
    print("That is not a number! ")
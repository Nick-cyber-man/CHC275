x = input("what number would would you like? ")
x = int(x)
check = False
while check == False:
    if x == 1:
        check = True
        print((x))
    elif x % 2 == 1:
        x = x * 3 + 1
        print((x))
    elif x % 2 == 0:
        x = x / 2
        print((x))
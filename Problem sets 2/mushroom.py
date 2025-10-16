sizes = []
check = False
while check == False:
    print("1. add sizes ")
    print("2. stop " )
    option = input("what option would you like? ")
    if option == "1":
        size = input("What sizes are the mushroom? ")
        sizes.append(size)
    elif option == "2":
        for i in range(len(sizes)):
            print(sizes[i])
            check = True

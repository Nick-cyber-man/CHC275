Food = []
Prices = []
total = 0

file = open("food.txt" , "r")
buffer = file.readlines()

for line in buffer:
    line = line.strip().split(",")
    Food.append(line[0])
    line[1] = float(line[1])
    Prices.append(line[1])
check = False
while check == False:
    print("Welcome to the Grocery store checkout")
    print("1. add to cart")
    print("2. remove items")
    print("3. check-out")
    option = input("what service would you like? ")

    if option == "1":
        print(Food)
        print(Prices)
        try:
            x = input("what value corresponding to food and price would you like to add to your cart? ")
            x = int(x)
            y = input(f"How many {Food[x]} would you like? ")
            y = int(y)
            total = total + y * Prices[x]
        except Exception as e:
            print(e)

    if option == "2":
        try:
            x = input("what value corresponding to food and price would you like to remove to your cart? ")
            x = int(x)
            y = input(f"How many {Food[x]} would you like? ")
            y = int(y)
            total = total - y * Prices[x]
        except Exception as e:
            print(e)

    if option == "3":
        tax = total * 0.06
        cart = total + tax
        print(f"The value of your purchase is: {cart}")
        check = True
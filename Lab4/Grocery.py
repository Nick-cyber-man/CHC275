Food = []
Prices = []
total = 0
cart = []
quanities = []

file = open("food.txt" , "r")
buffer = file.readlines()

for line in buffer:
    line = line.strip().split(",")
    Food.append(line[0])
    line[1] = float(line[1])
    Prices.append(line[1])

print("Welcome to the Grocery store check-out")
print("1. add to cart")
print("2. remove items")
print("3. check-out")
option = input("what service would you like? ")

if option == "1":
    print(Food)
    print(Prices)
    option = input("what value corresponding to food/price would you like to add to your cart? ")
    try:
        option = int(option)
        Quanity = input(f"How many {Food[option]} would you like? ")
    except Exception as e:
        print(e)

    
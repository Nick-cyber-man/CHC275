products = {"oranges":0,"apples":5, "pears":10, "grapes":8}

print(f"oranges: {products["oranges"]}")

productsList = [0,5,10,8]
print(productsList[0])


productsList.pop(0)
print(productsList[0])


products["bananas"] = 15
print(f"bananas:{products["bananas"]}")

products["bananas"] = 10
print(f"bananas:{products["bananas"]}")

products[1] = 60
print(f"1:{products[1]}")

print(products)

for x in products:
    print(products[x])


test = {"john":60,"mark":75}    
average = 0
for grade in test.value():
    average += grade + 5
    
average = average/2
print(average)
print(sum(test.value()/len(test.values())))
print(test)

for name in test.keys():
    print(name)
    
testdict = {1:"hello",2:True,3:[1,2,3],4:{"foo";1,"bar":2}}
print(testdict)
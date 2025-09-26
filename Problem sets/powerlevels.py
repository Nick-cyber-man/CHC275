x = input("what is the power level of the hero?: ")
y = input("what is the power level of the monster?: ")
x = int(x)
y = int(y)
if x > y:
    print("Hero wins ")
elif x < y:
    print("Monster wins ")
elif x == y:
    print("tie")

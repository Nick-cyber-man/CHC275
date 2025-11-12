print("first days")

lastdays = open("stock numbers2.txt", "r")
msft1 = lastdays.readlines() [0]
lastdays.close()
print(msft1)

lastdays = open("stock numbers2.txt", "r")
AMZN1 = lastdays.readlines() [1]
lastdays.close()
print(AMZN1)

lastdays = open("stock numbers2.txt", "r")
NVDA1 = lastdays.readlines() [2]
lastdays.close()
print(NVDA1)
i=1
while (i<=5):
    print(i)
    i=i+1
print("last days")

firstdays = open("stock numbers.txt", "r")
msft2 = firstdays.readlines() [0]
firstdays.close()
print(msft2)

firstdays = open("stock numbers.txt", "r")
AMZN2 = firstdays.readlines() [1]
firstdays.close()
print(AMZN2)

firstdays = open("stock numbers.txt", "r")
NVDA2 = firstdays.readlines() [2]
firstdays.close()
print(NVDA2)
mean = sum(NVDA2)/len(2)

file = open("Day1.txt","r")
buffer = file.readlines()

msft = buffer[0].strip().split(",")
msft.pop(0)
print(msft)

amzn = buffer[1].strip().split(",")
amzn.pop(0)
print(amzn)

nvda = buffer[2].strip().split(",")
nvda.pop(0)
print(nvda)
for i in range(len(msft)):
    msft[i] = int(msft[i])
    amzn[i] = int(amzn[i])
    nvda[i] = int(nvda[i])

avgM1 = sum(msft)/len(msft)
avgA1 = sum(amzn)/len(amzn)
avgN1 = sum(nvda)/len(nvda)
print(f"The average of the staock on day one is: MSFT:{avgM1}, AMZN: {avgA1}, and NVDA:{avgN1}")

file = open("Day21.txt","r")
buffer = file.readlines()

msft = buffer[0].strip().split(",")
msft.pop(0)
print(msft)

amzn = buffer[1].strip().split(",")
amzn.pop(0)
print(amzn)

nvda = buffer[2].strip().split(",")
nvda.pop(0)
print(nvda)
for i in range(len(msft)):
    msft[i] = int(msft[i])
    amzn[i] = int(amzn[i])
    nvda[i] = int(nvda[i])

avgM2 = sum(msft)/len(msft)
avgA2 = sum(amzn)/len(amzn)
avgN2 = sum(nvda)/len(nvda)
print(f"The average of the stock on day one is: MSFT:{avgM2}, AMZN: {avgA2}, and NVDA:{avgN2}")

Buys = []
if avgM1 < avgM2:
    Buys.append("MSFT")
if avgN1 < avgN2:
    Buys.append("NVDA")
if avgA1 < avgA2:
    Buys.append("AMZN")


Report = open("Report.txt", "w")
Buys[-1] = Buys[-1].append(",")
Report.writelines(Buys)
Report.close()

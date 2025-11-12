
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

Report = "Stock report.txt"
file = open(Report,"w")
line0 = f"Microsoft average 1: {avgM1}, Microsoft average 2: {avgM2}\n"
line1 = f"Amazon average 1: {avgA1}, Amazon average 2: {avgA2}\n"
line2 = f"Nvidia average 1: {avgN1}, Nvidia average 2: {avgN2}\n"
line3 = f"You should buy these stocks: {Buys}"
Buffer = [line0,line1,line2,line3]
file.writelines(Buffer)
file.close()

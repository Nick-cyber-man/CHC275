
file = open("Day1.txt","r")
buffer = file.readlines()
msft = buffer[0].strip().split(",")
msft.pop(0)
print(msft)

amzn = buffer[0].strip().split(",")
amzn.pop(0)


#avg = sum(grades)/len(grades)
#line = f"the average GPA on {date} is {avg}"
#file.close()
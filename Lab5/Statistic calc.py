import math



def getList():
    check = False
    intergerslist = []
    while check == False:
        statlist = input("What are the intergers you would like to use in you list, when done type stop? ")
        try:
            statlist = int(statlist)
            intergerslist.append(statlist)
        except Exception as e:
            if statlist == "stop":
                return intergerslist



def printMenu():
    print("1.Min")
    print("2.Max")
    print("3. Mean")
    print("4.Median")
    print("5. Standard Deviation")
    print("6. Clear list")



def getMin(userList):
    min = userList[0]
    for num in userList:
        if min > num:
            min=num
    return min

def getmean(userList):
    sum=0
    for num in userList:
        sum=num+sum
    mean=sum/len(userList)
    return mean
        
def getmedian(userList):
    userList = sorted(userList)
    y = len(list)

    if y % 2 == 1:
        mid=y/2
        return list[mid]
    else:
        mid = (y // 2) - 1
        mid2 = y // 2
        z=(list[mid]+ list[mid2])/2
        return z

def getmax(userList):
    max = userList[0]
    for num in userList:
        if max < num:
            max=num
    return max

def getSTdDev(userList):
    sse = 0
    mean = getmean(userList)
    for num in userList:
        sse=sse+(num-mean)**2
    sse=sse/len(userList)
    return math.sqrt(sse)

def main():
    enter=getList()
    check = False
    while check == False:
        printMenu()
        option=input("what function would you like to do? type quit to quit")
        if option == "1":
            ans=getMin(enter)
            print(f"The minimum is {ans}")
        if option == "2":
            ans = getmax(enter)
            print(f"the maximum is {ans}")
        if option == "3":
            ans = getmedian(enter)
            print(f"The median is {ans}")
        if option == "4":
            ans = getmean(enter)
            print(f"The mean is {ans}")
        if option == "5":
            ans = getSTdDev(enter)
            print(f"The Standard deviation is {ans}")
        if option =="quit":
            check = True


if __name__ == "__main__":
    main()
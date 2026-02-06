import math
import test


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
    option = input("What statistic would you like to do on the list? ")
    return option


def getMin(userList):
    pass




def main():
    test.foo()
    print("Welcome to the Statistics Calculator")
    mynums= getList()
    print(mynums)


if __name__ == "__main__":
    main()
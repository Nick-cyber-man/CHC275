def makelist():  
    nums = []
    check = False
    while check == False:
        print("1")
        print("quit")
        option = input("what option do you want?")
        if option == "1":
            x = input("What numbers would you like?")
            x = int(x)
            nums.append(x)
        elif option == "quit":
            check =True
    return(nums)
list1 = makelist()
print(list1)
list2 = makelist()
print(list2)
      

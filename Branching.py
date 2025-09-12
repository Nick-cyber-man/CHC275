x = 10
if x % 2 == 1:
    print(f"{x} is divisible be 2 ")
    print("test")
else:
    print("This is not a part of the if statement")

x = 10
if x % 5 == 0:
    print(f"{x} is divisible by 5")
elif x % 2 == 0 :
    print(f"{x} is divisible by 2")
else:
    print(f"{x} is not divisible by 5 or 2")

x = 10
if x > 5 and x > 15:
    print(f"{x} is greater than 5 and 15")
    
if x > 5 or x > 15:
     print(f"{x} is greater than 5 or 15")
     
year = input("enter your year: ")
if year == "freshman":
    print("your grade level is 9 ")
elif year == "sophmore":
    print("your grade level is 10 ")
elif year == "junior":
    print("you grade level is 11 ")
elif year == "senior":
    print("you grade level is 12 ")

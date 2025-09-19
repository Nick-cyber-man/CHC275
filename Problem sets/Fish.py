print("what kind of fish do you have? ")
print("1. carnivorous")
print("2. saltwater")
print("3. community")
fish = input("what kind of fish do you have? ")
if fish == "carnivorous":
    print("too bad")
elif fish == "saltwater":
    print("you're a fancy fish owner")
elif fish == "community":
    print("you should get more than one")
else:
    print("I dont think thats a kind of fish")
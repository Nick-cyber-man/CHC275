option = input("Enter a list of nums seperated by spaces ")
print(option)

names = option.split()
print(names)

bitstream = "1010101011010101010110110you"
msg = bitstream.split("0110101")
print(msg)


mystr = "Hello#How#Are#You"
msg = mystr.split("#")
print(msg)

space = " "

fruits = ["apples" , "oranges" , "pears" , "mangos"]

combined = space.join(fruits)
print(combined)

combined = " ".join(fruits)
print(combined)

sum = 4 + 5
print(sum)

str1 = "Hello"
str2 = "World"
concat = str2 + str1
print(concat)

print("Welcome to the Palindrome detector" )
palindrome = input("What word would you like to detect?" ).strip().lower().split()
palindrome = "".join(palindrome)
reverse = ""

for char in palindrome:
    reverse = char + reverse 
if palindrome == reverse:
    print("Thats a palindrome")
else:
    print("Thats not a palindrome")
print("Welcome to the Palindrome detector" )
palindrome = input("What word would you like to detect?" )
reverse = ""

for i in range(len(palindrome)):
    for char in palindrome:
        reverse = palindrome + char
        print(reverse)
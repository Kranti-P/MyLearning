def palindrome_check(str):
    char = ""
    for i in str:
        char = i + char #The sequence is important here. If u do "char + i" then it is wrong
    print("Reverse is: ", char)
    return(char)

str=input("Enter a string: ")
print("Original String is: ",str)
reverse_String = palindrome_check(str)
if(str==reverse_String):
    print("It's a palindrome")
else:
    print("it's not a palindrome :( ")
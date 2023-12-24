original_string = 'NEETEENA'
def palindrome(original_String):
    reverse= ''.join(reversed(original_String))
    print("Reverse is: ", reverse)

    if(original_String==reverse):
        print("It's a palindrome")
    else:
        print("Not a palindrome")

palindrome(original_string)
str = input ("Enter a string: ")
if(str == str.capitalize()):
    print("Your String is in Capital Case")
elif (str.isupper() == True):
    print("Your String is in Upper Case")
elif(str.islower() == True):
    print ("Your string is in lower case")
else:
    print("End of program")
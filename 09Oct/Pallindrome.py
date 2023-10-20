str=input("Enter a string: ")
reversed_string = str[::-1] #slicing method reverses string starting from-1 index
str2= "".join(reversed(str)) #inbuilt function reversed() that can reverse # a string
# or any iterable, but it returns a reversed iterator. To convert the iterator back to a string,
# you can use the join() method.

#User can use either method mentioned in step 2 or step 3 to reverse a string
if(str==str2):
    print("It's a pallindrome!")
else:
    print("Not a pallindrome :( ")

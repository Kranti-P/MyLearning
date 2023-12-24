str=input("enter a string: ")
count = 0
for i in str.lower():
    ls=['a', 'i', 'e','o','u']
    if i in ls:
        count=count+1
    else:
        pass
print("count is: ", count)
str = input("Enter a string: ")
d = {} #Initiate Empty Dicionary

for i in (str.lower()): #Traverse through each character of string. String converted into lowercase
    d[i] = d.get(i, 0) + 1 #d.get(i,0) gives ith element value if it is not present it returns 0 by default. And we are adding 1 as an increment

for k,v in d.items(): #Print the result
    print("Letter {} is repeated {} times: ".format(k,v))

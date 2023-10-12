ls = [1,2,3,4,5,6,7]
print(ls.__len__())  #Prints Length
print("Length Function: ", len(ls))
print(sum(ls))
ls1= ['ABC', True, 123, None]
ls1.insert(1,2222)
print(ls1)
y=ls1.count(1) #Here 1 is counted as boolean True because in ls1, true is stored as boolean
print(y) #Hence this is giving output as 1 even though 1 value is not present in the list
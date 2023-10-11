ls = [11,12,23,71,11,90]
ls.append(10) #Adds element at the end of list
print(ls)
ls1= [11,123,125,1]
ls = ls+ls1 # merges 2 lists into one
print(ls)
ls.pop() #Removed last element of the list
print(ls)
ls.sort() # sorts in ascending order
print(ls)
ls.sort(reverse= True) # sorts in descending order
if(11 in ls): #IN function is checking if 11 exists in list
    print("11 exists in list")
else: print ("Doesnt exist")
print(ls)
y=ls.count(11) #Counts the number of occurances of an element
print("11 is releated ", y, 'times')
ls2=[]
ls2.extend(ls)
print("ls2 is copy of ls:" ,ls2)
ls2.reverse()
print("reverse ls2 is :", ls2)
print("ls2 elements sum:", sum(ls2)) #Gives the sum of list elements
#ls.clear() # clears all the elements in the list
#print(ls)

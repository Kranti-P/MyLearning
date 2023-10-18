#Write a Python function that takes a list as input and returns a dictionary
# where keys are unique elements from the list, and
# values are the number of times they appear in the list

i = int(input("Enter how many items list you want: "))
ls=[]
j=0
while j<i:
    str=input("Enter list item :")
    ls.append(str)
    j+=1
print("list is:", ls)
d={}
for k in ls:
    d[k]=d.get(k,0)+1
print("Final List: " , d)

ls = []
i=1
while i < 6:
    x=int(input("Enter element in list: "))
    ls.append(x)
    i+=1
print(ls)
ls[0], ls[-1] = ls[-1], ls[0] #Interchanging first and last character of list
print(ls)
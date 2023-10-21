x = int(input("Enter the number of elements in the list-1: "))
y = int(input("Enter the number of elements in the list-2: "))
z = int(input("Enter the number of elements in the list-3: "))

ls1=[int(input("Enter elements of ls1: ")) for a in range(x)]
ls2=[int(input("Enter elements of ls2: ")) for a in range(y)]
ls3=[int(input("Enter elements of ls3: ")) for a in range(z)]
print(ls1, ls2, ls3)
ls4=[]

for i in ls1:
    if i in ls2 and i in ls3:
        ls4.append(i)
print("Common Elements in all 3 lists = ", ls4)
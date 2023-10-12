Str = input("Enter a quote that you like: ")
ls = Str.split()
for i in ls:
    print(i.__len__())

print("----------------------n")

Str2= "sample string with while loop"
print(Str2)
ls2 = Str2.split()
print(len(ls2))
i=0
ls3 = []
while i<len(ls2):
    ls3.append(ls2[i].__len__())
    i=i+1
print("Program Ended", ls3)
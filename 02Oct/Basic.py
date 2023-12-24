print("Hi"*3) #Prints Hi 3 times
n=10
#Range Function
for i in range(n): # default range starts from 0 to n-1
    print(i)

#18Oct:
#break: breaks the loop at particular condition
#pass: sort of skips that particular if condition but continues the loop
#continue: continues the loop

var1= '765'
print(list(var1))

num= [10,20,30,40,50]
print(num[1:4])

print(1+True)
a = (10,20,30)
b = (40,)
print(a+b)

a="Hello"
b="Hello"
print(f"a is b: {a is b}")
print(f"a==b: {a==b}")

print(f"value of a = {a}")

ls=[1,2,3,4,5]
result=ls[1:4:2]
ls2=[1,2,3,2,3]
print(ls!=ls2)
print(result)

tp1= (1,2,3,4)
tp2= (1,2,4,3)
print(tp1 < tp2)

i=j=[3]
print(i, j)
i+=j
print(i,j)

s1= {}
s2= {1,2,3}
print(type(s1), type(s2))

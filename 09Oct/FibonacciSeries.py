x = int(input("Give a number: "))
a, b = 0, 1
# for i in range(x): gives first x fibonacci numbers
while (a < x):  # gives fibo numbers upto the x
    print(a, end=' ')
    a, b = b, a + b

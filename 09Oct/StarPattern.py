x = int(input("Enter the number of lines in star pattern: "))
i = 1
while i <= x:
    print("* " * i)
    i = i + 1

print("-----------------------------------------")
y = int(input("Enter the number of lines in inverse star pattern: "))
i = 1
while i <= y:
    print("* " * y)
    y = y - 1

print("-----------------------------------------")
y = int(input("Enter the number of lines in 12335 pattern: "))
i = 1
while (i <= y):
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
print("End!")

print("-----------------------------------------")
y = int(input("Enter the number of lines in 54321 pattern: "))
i = 1
while (y >= i):
    j = y
    while j >= i:
        print(j, end=" ")
        j -= 1
    print()
    y -= 1
print("End!")

print("-----------------------------------------")
y = int(input("Enter the number of lines in pyramid pattern: "))
i=0
while i <= y: # i=5
    print(" " * (y-i), end=' ')
    print("*" * (i+1), end='')
    i += 1

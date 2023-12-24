num = 12345
sum = 0
while num != 0:
    digit = num % 10
    sum = sum + digit
    num = int(num / 10)  # this is basically = num//=10. Only num/10 fives decial results.
print(sum)

str = input("Enter a word: ")
d = {}
for i in str.split(' '):
    d[i] = d.get(i, 0) + 1

for k,v in d.items():
    print("Word {} is repeated {} times.".format(k,v))
#Count the number of words in a file
fh=open('sample.txt')
str=fh.read()
print(str)
ls=[]
for word in str.split():
    ls.append(word)
print("Count of words = ", len(ls))
fh.close()
fh=open('wordoccurance.txt')
str=fh.read()
ls=[]
for i in str.split():
    ls.append(i)
dir={}
for i in ls:
    dir[i]=dir.get(i,0)+1

for k,v in dir.items():
    print("{} is appeared {} times".format(k,v))

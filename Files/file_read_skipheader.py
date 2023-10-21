fh=open('test.csv','r') #'r' for read mode, 'w' for write and 'a' for append
# for i in fh:
#     print(i) #it will read first line or csv header as well
# fh.close()
print("***********************************************")
# next(fh) #it will skip the 1st line or header and continue to print other lines
# for j in fh:
#     print(j)
# fh.close()

print("***********************************************")
next(fh) #it will skip the 1st line or header and continue to print other lines
for k in fh:
    #print(k.split(",")) #this prints output with \n which is not desired
    print(k.strip().split(",")) #Strip function removed leading and trailing spaces
fh.close()


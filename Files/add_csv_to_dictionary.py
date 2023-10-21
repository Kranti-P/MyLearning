#Print CSV File as a list of dictionary
import csv
fh=open('test.csv')
# ls=[]
# dict_reader = csv.DictReader(fh)
# for i in dict_reader:
#     ls.append(i)
# print(ls)
# fh.close()

#Print each line of CSV File as dictionary
reader= csv.DictReader(fh)
for i in reader:
    print(i)
fh.close()
def sum_of_elements(ls):
    # temp=0
    # i=0
    # while i<len(ls):
    #     temp=temp+ls[i]
    #     i+=1
    return sum(ls)

x= int(input("How Many Elements you want to have in list? "))
# ls=[]
# while(x>=1):
#     i=int(input("Enter Element in the list: "))
#     ls.append(i)
#     x-=1
ls=[int(input("Enter Element in the list: ")) for i in range(x)]  #Rather than using any loop for taking input from user n times, u can use this
summation = sum_of_elements(ls)
print("Sum of list Elements = ", summation)
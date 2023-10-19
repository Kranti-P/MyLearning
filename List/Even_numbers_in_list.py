def even_number(ls):
    # i=0
    # while(i<len(ls)):
    #     if ls[i]%2==0:
    #         print(ls[i])
    #     else: pass
    #     i+=1
    even_nums = [num for num in ls if num % 2 == 0]
    print(*even_nums)

x=int(input("How many elements are there in ur list? "))
ls=[int(input("Enter element of list: ")) for a in range(x)]
even_number(ls)
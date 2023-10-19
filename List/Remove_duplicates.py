def remove_duplicates(ls):
    ls2 = []
    for num in ls:
        if num not in ls2:
            ls2.append(num)
    print(ls2)

x=int(input("How many elements in the list? "))
ls= [int(input("Enter element in list: ")) for n in range(x)]
remove_duplicates(ls)
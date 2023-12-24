def remove_duplicates(ls):
    ls2 = []
    for num in ls:
        if num not in ls2:
            ls2.append(num)
    print("Removed duplicates using for loop on list: ", ls2)


def remove_duplicates_using_Set(ls):
    unique_list = list(set(ls))
    #print(type(unique_list))
    print("Removed duplicates using set: ", unique_list)


x = int(input("How many elements in the list? "))
ls = [int(input("Enter element in list: ")) for n in range(x)]
remove_duplicates(ls)
remove_duplicates_using_Set(ls)

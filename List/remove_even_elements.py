def remove_even_elements_from_list(ls):
    ls1 = []
    for i in ls:
        if i % 2 == 0:
            pass
        else:
            ls1.append(i)
    print("Original List: ", ls)
    print("Even Elements removed from list: ", ls1)


ls = [10, 11, 13, 15, 23, 24, 22, 20]
remove_even_elements_from_list(ls)

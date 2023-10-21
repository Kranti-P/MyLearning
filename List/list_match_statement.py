# from unittest import case

def sum_of_elements():
    y = int(input("How many elements you want to have in your list? "))
    ls = [int(input("Enter List Elements:")) for i in range(y)]
    print("Sum of your list elements= ", sum(ls))


def largest_element_in_list():
    y = int(input("How many elements are there in your list? "))
    ls = [int(input("Enter List Element: ")) for i in range(y)]
    ls.sort()
    print("Largest element from your list is: ", ls[-1])


def remove_duplicates_from_list():
    z = int(input("How many elements in your list ?"))
    print(type(z))
    ls = [int(input("Enter list element: ")) for i in range(z)]
    ls1 = []
    for i in ls:
        if i not in ls1:
            ls1.append(i)
    print("Unique List of Elements is: ", ls1)


def palindrome_check():
    str = input("Enter a string: ")
    str_reverse = str[::-1]
    if str == str_reverse:
        print("String is a palindrome ")
    else:
        print("String is NOT a palindrome ")


def common_elements_in_2_lists():
    v = int(input("How many elements are in list 1? "))
    ls1 = [int(input("Enter element for list1: ")) for i in range(v)]
    w = int(input("How many elements are in list 2? "))
    ls2 = [int(input("Enter elements for list2: ")) for i in range(w)]
    ls3 = []
    for i in ls1:
        if i in ls2:
            ls3.append(i)
    print("Common Elements in both lists are: ", ls3)


print("\n 1. Enter 1 for Sum of All Elements\n "
      "2. Enter 2 for largest element in the list\n "
      "3. Enter 3 for remove duplicates\n "
      "4. Enter 4 for Palindrome check \n "
      "5. Enter 5 for common elements in 2 lists")
x = int(input("Enter your choice Here: "))

if x not in range(1, 6):
    print("Sorry! You have entered wrong choice! ")
else:
    match x:
        case 1:
            sum_of_elements()
        case 2:
            largest_element_in_list()
        case 3:
            remove_duplicates_from_list()
        case 4:
            palindrome_check()
        case 5:
            common_elements_in_2_lists()
        case _:
            print("You are in default option ")
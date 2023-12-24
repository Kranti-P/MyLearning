from collections import OrderedDict

d = {1: 'a', 3: 'asa', 2: 'abc', 4: 'asa', 'd': 'adasd'}

op = 'd' in d
print(op)

list_of_keys_in_dict = list(d.keys())
print(list_of_keys_in_dict)
keys_sort = sorted(list_of_keys_in_dict)  # Sorts the keys
keys_sort = sorted(list_of_keys_in_dict, reverse=True)  # Reverses the keys
# keys_sort_rev = list(reversed(list_of_keys_in_dict)) #Reverse does not work with abcd alphabets
print(keys_sort)
#print(keys_sort_rev)  # Keys in reverrse order
print(d)

print(d.items())  # Set of items

# OrderedDict
#od = OrderedDict()  # Remembers insertion order


list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

set1 = set(list1)
set2 = set(list2)

unique_to_list1 = [item for item in list1 if item not in set2]
unique_to_list2 = [item for item in list2 if item not in set1]

result = unique_to_list1 + unique_to_list2
print(result)  # Output: [2, 2, 5]

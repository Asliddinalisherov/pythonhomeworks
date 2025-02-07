list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
set1 = set(list1)
set2 = set(list2)

forlist1 = [item for item in list1 if item not in set2]
forlist2 = [item for item in list2 if item not in set1]

forlist1.extend(forlist2)
print(forlist1)

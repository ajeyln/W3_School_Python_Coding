ilist1 = input("Write Key element with space ")
list1 = ilist1.split(" ")
ilist2 = input("Write Value element with space ")
list2 = ilist2.split(" ")
print(list1)
print(list2)
idict={list1[i]:list2[i] for i in range(len(list1))}
"""for key in ilist1:
    for value in ilist2:
        idict[key] = value
        break"""
print(idict)

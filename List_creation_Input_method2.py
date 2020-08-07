ilist = input("Write key and Value with space (Eg: Name Mike): ")
list1 = ilist.split(" ")
dict1 = {list1[i]:list1[i+1] for i in range(0,len(list1),2)}
print(dict1)
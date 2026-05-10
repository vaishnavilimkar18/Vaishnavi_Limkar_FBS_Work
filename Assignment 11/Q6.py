 
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

union_list = []


for i in list1:
    if i not in union_list:
        union_list = union_list + [i]


for i in list2:
    if i not in union_list:
        union_list = union_list + [i]

print("Union List =", union_list)
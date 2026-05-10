# Easy program to merge two lists and sort them

list1 = [30, 10, 50]
list2 = [20, 40, 15]


new_list = list1 + list2


for i in range(len(new_list)):
    for j in range(i + 1, len(new_list)):
        if new_list[i] > new_list[j]:
            temp = new_list[i]
            new_list[i] = new_list[j]
            new_list[j] = temp

print("Sorted List =", new_list)
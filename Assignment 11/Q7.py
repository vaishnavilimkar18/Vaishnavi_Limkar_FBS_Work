# Python Program to find intersection of two lists

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

intersection_list = []

for i in list1:
    if i in list2:
        intersection_list = intersection_list + [i]

print("Intersection List =", intersection_list)
# Program to create duplicate of a list


li = [10, 20, 30, 40, 50]

duplicate_list = [20,10,50,60,20]

for i in li:
    duplicate_list = duplicate_list + [i]

print("Original List =", li)
print("Duplicate List =", duplicate_list)
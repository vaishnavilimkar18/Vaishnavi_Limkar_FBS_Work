# Program to remove duplicates from list


li = [10, 20, 30, 20, 40, 10, 50]

new_list = []

for i in li:
    found = 0

    for j in new_list:
        if i == j:
            found = 1

    if found == 0:
        new_list = new_list + [i]

print("Original List =", li)
print("List after removing duplicates =", new_list)
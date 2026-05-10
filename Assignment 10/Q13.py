# Program to remove even numbers from list


li = [10, 15, 20, 25, 30, 35, 40]

new_list = []

for i in li:
    if i % 2 != 0:
        new_list = new_list + [i]

print("Original List =", li)
print("List after removing even numbers =", new_list)
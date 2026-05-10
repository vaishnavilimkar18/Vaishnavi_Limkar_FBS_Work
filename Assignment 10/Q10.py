# Program to remove all occurrences of a given element


li = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter element to remove: "))

new_list = []

for i in li:
    if i != num:
        new_list = new_list + [i]

print("Original List =", li)
print("List after removing element =", new_list)
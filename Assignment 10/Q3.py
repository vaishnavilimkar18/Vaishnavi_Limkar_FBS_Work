# Program to find second largest element in a list


li = [10, 45, 20, 80, 60, 75]

largest = li[0]
second_largest = li[0]

for i in li:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest element =", second_largest)
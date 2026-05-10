# Program to check element is present in list or not


li = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter element to search: "))

count = 0

for i in li:
    if i == num:
        count = count + 1

if count > 0:
    print(num, "is present in the list")
    print("It is present", count, "times")
else:
    print(num, "is not present in the list")
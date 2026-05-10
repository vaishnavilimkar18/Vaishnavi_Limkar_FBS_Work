# Program to separate even and odd elements into two lists

n = int(input("Enter number of elements: "))

li = []


for i in range(n):
    ele = int(input("Enter element: "))
    li = li + [ele]

even_list = []
odd_list = []


for i in li:
    if i % 2 == 0:
        even_list = even_list + [i]
    else:
        odd_list = odd_list + [i]

print("Original List =", li)
print("Even Elements List =", even_list)
print("Odd Elements List =", odd_list)

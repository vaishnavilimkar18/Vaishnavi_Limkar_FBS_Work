# Program to print numbers divisible by m and n


li = [10, 15, 20, 30, 40, 60, 75]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print("Numbers divisible by", m, "and", n, "are:")

for i in li:
    if i % m == 0 and i % n == 0:
        print(i)
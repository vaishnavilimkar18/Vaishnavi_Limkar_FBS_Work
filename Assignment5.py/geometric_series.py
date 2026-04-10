# n = int(input("Enter value of n: "))

# sum = 2**n - 1

# print("Sum =", sum)



n = int(input("Enter value of n: "))

sum = 0

for i in range(n):
    sum = sum + 2**i

print("Sum =", sum)
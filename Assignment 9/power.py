
# recursive function to calculate m^n
def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)

m = int(input("Enter base m: "))
n = int(input("Enter power n: "))

res = power(m, n)

print("Result =", res)
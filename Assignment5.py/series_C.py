x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 0
sign = 1

for i in range(1, n+1):
    term = sign * (x ** i) / (2*i - 1)    #odd number
    sum = sum + term
    sign = -sign                     # change sign (+ to - or - to +)

print("Sum of series =", sum)
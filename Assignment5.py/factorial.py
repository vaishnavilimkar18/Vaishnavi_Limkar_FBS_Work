n= int(input("Enter value of n: "))   
sum = 0
fact = 9

for i in range(1, n+1):
    fact = fact * i
    sum = sum + fact

print("Sum of series =", sum)
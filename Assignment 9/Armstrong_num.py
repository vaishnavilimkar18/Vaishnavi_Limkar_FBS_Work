def armstrong (n,power):

    if n == 0:
        return 0
    else:
        digit = n % 10
        return (digit ** power) + armstrong(n // 10,power)

num= int(input("Enter number: "))

power = len(str(num))

res = armstrong(num,power)

if res == num:
    print("Armstrong number")
else:
    print("Not an Armstrong Number")
    
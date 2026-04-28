# recursive function to reverse number
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse_number(n // 10, rev)


num = int(input("Enter a number: "))

res = reverse_number(num)

print("Reversed number =", res)
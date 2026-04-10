start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Numbers divisible by 7 and multiples of 5 are:")

for num in range(start, end + 1):
    if (num % 7 == 0 and num % 5 == 0):
        print(num)
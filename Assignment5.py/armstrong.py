start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end+1):
    temp = num
    sum = 0
    digits = len(str(num))
    
    while temp > 0:
        rem = temp % 10
        sum = sum + (rem ** digits)
        temp = temp // 10
    
    if num == sum:
        print(num)
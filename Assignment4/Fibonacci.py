n = int(input("Enter number :"))

a,b = 0,1

for i in range(n + 1):
    if a>n:
        break
    print(a,end =" ")
    a,b=b,a+b
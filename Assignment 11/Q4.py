

li = [10, 50, 20, 80, 40]


for i in range(len(li)):
    for j in range(len(li)-1):
        
        if li[j] > li[j+1]:
            
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp

print("Sorted List =", li)

print("Second Largest Number =", li[-2])
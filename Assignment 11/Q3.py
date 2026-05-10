

li = [[1, 5], [2, 3], [4, 1], [3, 2]]


for i in range(len(li)):
    for j in range(i + 1, len(li)):
        
        if li[i][1] > li[j][1]:
            
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

print("Sorted List =", li)
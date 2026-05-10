

li = ["apple", "kiwi", "banana", "grape", "mango"]

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        
        if len(li[i]) > len(li[j]):
            
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

print("Sorted List =", li)
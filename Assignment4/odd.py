start = int(input("Enter the start no :"))

end = int(input("Enter the end no :"))
print(f"The odd number from {start} to {end} are :=")
for i in range (start,end):
    if(i % 2 !=0):
        print(i)
     
     
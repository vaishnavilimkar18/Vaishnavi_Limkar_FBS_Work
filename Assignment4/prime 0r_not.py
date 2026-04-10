no = 7
if(no > 1):
    
    for i in range(2,7):
        if(no % i == 0):
          print(f"{no} is not prime number.")
        
    else:
       print(f"{no} is prime number.")
else:
   print("Number is greater then 1.")
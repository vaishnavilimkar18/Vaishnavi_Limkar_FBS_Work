import random
uid = "vaishnavi.11"
pas = "vaishu@11"
 
u = input("Enter User ID: ")
p = input("Enter Password: ")

if u == uid and p == pas:
    num = random.randint(1000,9999)
    print("Enter this number:",num)

    user_num = input("Enter number: ")

    if user_num == str(num):
     print("Success Login")
    else:
       print("wrong Captcha")
else:
   print("Wrong UserID or Password")






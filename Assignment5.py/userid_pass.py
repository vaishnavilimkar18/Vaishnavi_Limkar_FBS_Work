correct_id = "admin"
correct_pass = "1234"

for i in range(3):
    uid = input("Enter ID: ")
    pwd = input("Enter Password: ")
    
    if uid == correct_id and pwd == correct_pass:
        print("Login Successful")
        break
    else:
        print("Wrong ID or Password")
        
        if i == 2:
            print("Program Terminated")
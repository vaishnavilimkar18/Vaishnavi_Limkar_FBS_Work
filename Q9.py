Marathi = int(input("Enter marks of Marathi: "))
English= int(input("Enter marks of English: "))
Hindi = int(input("Enter marks of Hindi: "))
Science = int(input("Enter marks of Science: "))
Math = int(input("Enter marks of Math: "))

per = (Marathi + English + Hindi + Science + Math) / 5
print("percentage :",per)

if per >= 60:
    print("First Class")
elif per >= 50:
     print("Second class")
elif per >= 40:
     print("Second class")
else:
     print("Fail")
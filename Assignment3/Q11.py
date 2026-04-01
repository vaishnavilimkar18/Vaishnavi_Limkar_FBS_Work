total = 0
 
for i in range(5):
    age = int(input("Age:"))
    amt = float(input("Amount:"))

    if age < 12:
        amt = amt * 0.7
    elif age > 59:
        amt = amt*0.5
    else: 
        amt = amt
    total += amt
    print("Total:",total)
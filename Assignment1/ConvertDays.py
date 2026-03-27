total_days = int(input("Enter number of days:"))

years = total_days // 365
weeks = (total_days % 365)//7
days = (total_days % 365) % 7

print(f"years :{years}")
print(f"week :{weeks}")
print(f"days :{days}")

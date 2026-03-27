PrincipleAmount = int(input('Enter principle amount:'))
Rate = int((input('Enter Rate:')))
Time = int(input('Enter Time:'))

compound_interest = PrincipleAmount * (1 + Rate/100)**Time-PrincipleAmount

print("Compound Interest is :",compound_interest)
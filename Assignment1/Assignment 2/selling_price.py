costPrice = int(input("Enter cost price:"))
discount_percent = int(input("Enter discount %:"))

discount_amount = costPrice*(discount_percent/100)

selling_price = (costPrice*discount_amount)

print("selling price of book  is:",selling_price)
print("Discount amount of book is:",discount_amount)
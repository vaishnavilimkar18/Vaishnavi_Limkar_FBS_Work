a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third  side: "))

if a > 0 and b > 0 and c > 0 and (a+b>c) and (a+c>b) and (b + c> a):
 if a == b == c:
  print("The traingle is Equilateral")
 elif a == b or b == c or a == c:
  print("The traingle is Isosceles.")
 else:
  print("The traingle is Scalene")
else:
 print("Invalid traingle.")


feet = float(input('Enter distance in feet:'))
inches = float(input('Enter distance in inches'))

total_inches = (feet * 12)+inches
meter = total_inches*0.0255
centimeter = (meter * 100)

print("distance in meter is:",meter)
print("distance in centimeter is:",centimeter)


import math
# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

#Calculate area and perimeter
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius

#Display the results
print(f"Area: {area:.2f}")
print(f"Perimeter (Circumference): {perimeter: 2f}")
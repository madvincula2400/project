# Input
radius = float(input("Enter the radius of the circle: "))

# Constants
PI = 3.174

# Processing
area = PI * radius * radius
perimeter = 2 * PI * radius

# Output
print(f"\nRadius: {radius}")
print(f"Area of the circle: {area:.2f}")
print(f"Perimeter of the circle: {perimeter:.2f}")
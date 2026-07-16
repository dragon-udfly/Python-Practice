# calculate Area, circumstance and volume of the cylinder

PI = 3.143

def cylinder_area(diameter, height):
    """Calculate Area of The Cylinder."""
    return ((PI * (diameter * diameter / 4)) + (2 * PI * (diameter / 2) * height))

def cylinder_volume(diameter, height):
    """Calculate Volume of The Cylinder."""
    return (PI * (diameter * diameter / 4) * height)

def cylider_circumference(diameter):
    """Calculate Circumference of The Cylinder"""
    return (PI * diameter)


# Take user inputs 

diameter = float(input("Enter Diameter: "))
height = float(input("Enter Height: "))

area = cylinder_area(diameter, height)
print(f"Area of Cylinder: {area}")

volume = cylinder_volume(diameter, height)
print(f"Volume of Cylinder: {volume}")

circumference = cylider_circumference(diameter)
print(f"Circumference of Cylinder: {circumference}")
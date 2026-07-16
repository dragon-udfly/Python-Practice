# calculating area and volume of circle related objects

PI = 3.143


# Circle 
circle_diameter = 32.1
cirlce_circumstance = PI * (circle_diameter / 2)
circle_area = PI * (circle_diameter * circle_diameter / 4)

print(f"Circle Diameter: {circle_diameter}m")
print(f"Circle Circumstance: {cirlce_circumstance}m")
print(f"Cricle Area: {circle_area}m^2")

# Cylinder 
cylinder_diameter = 45.2
cylinder_height = 78.3
cylinder_area = (PI * (cylinder_diameter * cylinder_diameter / 4) + 2 * PI * (cylinder_diameter / 2) * cylinder_height)
cylinder_volume = PI * (cylinder_diameter * cylinder_diameter / 4) * cylinder_height
print(f"Cylinder Diameter {cylinder_diameter}m")
print(f"Cylinder Height: {cylinder_height}m")
print(f"Cylinder Area: {cylinder_area}m^2")
print(f"Cylinder Volume: {cylinder_volume}m^3")


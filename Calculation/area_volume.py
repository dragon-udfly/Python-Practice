# calculating area and volume of circle related objects

PI = 3.143


# Circle 
circle_diameter = 32.1
cirlce_circumstance = PI * (circle_diameter / 2)
circle_area = PI * (circle_diameter * circle_diameter / 4)

print(f"Circle Diameter: {circle_diameter}m")
print(f"Circle Circumstance: {cirlce_circumstance}m")
print(f"Cricle Area: {circle_area}m^2\n")

# Cylinder 
cylinder_diameter = 45.2
cylinder_height = 78.3
cylinder_area = (PI * (cylinder_diameter * cylinder_diameter / 4) + 2 * PI * (cylinder_diameter / 2) * cylinder_height)
cylinder_volume = PI * (cylinder_diameter * cylinder_diameter / 4) * cylinder_height
print(f"Cylinder Diameter {cylinder_diameter}m")
print(f"Cylinder Height: {cylinder_height}m")
print(f"Cylinder Area: {cylinder_area}m^2")
print(f"Cylinder Volume: {cylinder_volume}m^3\n")

# Sphere 
sphere_diameter = 32.2
sphere_area = PI * (sphere_diameter * sphere_diameter / 4)
sphere_volume = (4 * PI * (sphere_diameter / 2 * sphere_diameter / 2 * sphere_diameter / 2)) / 3
print(f"Sphere Diameter: {sphere_diameter}m")
print(f"Sphere Area: {sphere_area}m^2")
print(f"Sphere Volue: {sphere_volume}m^3\n")

# Cone 
cone_diameter = 45.3
cone_height = 90.2
cone_slope = 104.7 
cone_area = (PI * (cone_diameter / 2) * cone_slope + PI * (cone_diameter * cone_diameter / 4))
cone_volume = (PI * (cone_diameter * cone_diameter / 4) * cone_height) / 3
print(f"Cone Diameter: {cone_diameter}m")
print(f"Cone Height: {cone_height}m")
print(f"Cone Slope: {cone_slope}m")
print(f"Cone Area: {cone_area}m^2")
print(f"Cone Volume: {cone_volume}m^3")

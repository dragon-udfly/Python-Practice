class Box:
    """Blueprint for 3D box"""

    def __init__(self, height = 0.0, width = 0.0, length = 0.0):
        self.height = height 
        self.width = width 
        self.length = length

    def box_area(self):
        """Calculate area of the box."""
        return (4 * self.width * self.height)
    
    def box_volume(self):
        """Calculate volume of the box."""
        return (self.width * self.height * self.length)
    

# Creating Objects (instantiation)
box_one = Box(2.0, 3.0, 5.0)
box_two = Box(33.2, 12.0, 21.3)

box_one_area = box_one.box_area()
box_one_volume = box_one.box_volume()

print(f"Box One Area: {box_one_area}")
print(f"Box One Volume: {box_one_volume}")
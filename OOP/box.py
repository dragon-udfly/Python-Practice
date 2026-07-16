class Box:
    """Blueprint for 3D box"""

    def __init__(self, height = 0.0, width = 0.0, length = 0.0):
        self.__height = height 
        self.__width = width 
        self.__length = length

    # creating a getter
    @property
    def height(self):
        """Returns the height."""
        return self.__height
    
    # creating setter
    @height.setter
    def height(self, height):
        """Change height of the box."""
        self.__height = height

    @property 
    def width(self):
        """Return the width."""
        return self.__width
    
    @width.setter 
    def width(self, width):
        """Change width of the box."""
        self.__width = width

    @property 
    def length(self):
        """Returns the length."""
        return self.__length
    
    @length.setter 
    def length(self, length):
        """Change the length."""
        self.__length = length

    def box_area(self):
        """Calculate area of the box."""
        return (6 * self.__width * self.__height)
    
    def box_volume(self):
        """Calculate volume of the box."""
        return (self.__width * self.__height * self.__length)
    

# Creating Objects (instantiation)
box_one = Box(2.0, 3.0, 5.0)
box_two = Box(33.2, 12.0, 21.3)

box_one_area = box_one.box_area()
box_one_volume = box_one.box_volume()

print(f"Box One Area: {box_one_area}")
print(f"Box One Volume: {box_one_volume}")

box_two.height = 32.3
print(f"Height of Box Two: {box_two.height}")
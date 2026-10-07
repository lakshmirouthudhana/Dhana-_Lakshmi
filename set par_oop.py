'''
TASK 1: Convert to Hierarchical + public, private, classmethod, class variable
'''
class Square:
    # Class Variable
    shape_type = "2D Shape"
    total_shapes = 0

    def __init__(self, x):
        self.x = x  # public variable
        self.__color = "Red"  # private variable
        Square.total_shapes += 1

    # public method
    def display(self):
        print(f"Side: {self.x}, Color: {self.__color}")

    # private method
    def __get_color(self):
        return self.__color

    # method to access private
    def get_color(self):
        return self.__get_color()

    @classmethod  # classmethod
    def get_total(cls):
        return cls.total_shapes

    @classmethod  # classmethod
    def change_type(cls, new_type):
        cls.shape_type = new_type

    def area(self):
        print(f'Area of Square is {self.x**2}')

# Hierarchical - ONE Parent (Square), THREE Childs

# Child 1 - Rectangle
class Rectangle(Square):
    def __init__(self, y, x):
        super().__init__(x)
        self.y = y

    def area(self):  # Method Overriding
        super().area()
        print(f'Area of Rectangle is {self.x * self.y}')

# Child 2 - Triangle
class Triangle(Square):
    def __init__(self, base, height):
        super().__init__(base)
        self.height = height

    def area(self):
        print(f'Area of Triangle is {0.5 * self.x * self.height}')

# Child 3 - Cube (for class variable use)
class Cube(Square):
    def area(self):
        print(f'Area of Cube is {6 * self.x**2}')

# Output
print(f"Shape Type: {Square.shape_type}")
r1 = Rectangle(7, 8)
r1.area()
print("Color:", r1.get_color())
print("Total Shapes:", Square.get_total())

t1 = Triangle(10, 5)
t1.area()
'''

TASK 2: Real Time Scenario for Multiple Inheritance
'''
# Real Time Family Example

class Father:
    def __init__(self, father_name, father_property):
        self.father_name = father_name
        self.father_property = father_property

    def father_quality(self):
        print(f"Father {self.father_name} gives Property: {self.father_property}")

class Mother:
    def __init__(self, mother_name, mother_quality):
        self.mother_name = mother_name
        self.mother_quality = mother_quality

    def mother_quality_show(self):
        print(f"Mother {self.mother_name} gives Quality: {self.mother_quality}")

# Multiple Inheritance - Child has 2 Parents
class Child(Father, Mother):
    def __init__(self, father_name, father_property, mother_name, mother_quality, child_name):
        Father.__init__(self, father_name, father_property)
        Mother.__init__(self, mother_name, mother_quality)
        self.child_name = child_name

    def show_child(self):
        print(f"\nChild: {self.child_name}")
        self.father_quality()
        self.mother_quality_show()
        print(f"{self.child_name} has both Father and Mother qualities - Multiple Inheritance")

# Output
c1 = Child("Ramesh", "50 Lakhs", "Sita", "Kindness & Culture", "Rahul")
c1.show_child()

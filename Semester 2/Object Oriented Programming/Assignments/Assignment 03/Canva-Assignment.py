from abc import abstractmethod
class Outline:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape(object):
    def __init__(self , name , outline, background):
        self.name = name
        self.outline = outline
        self.background = background
    
    @abstractmethod
    def area(self):
        pass
    
    def __str__(self):
        return f"{self.name}, {self.outline}, {self.background}"

class Square(Shape):
    def __init__(self, name, outline, background, sl):
        super().__init__(name, outline, background)
        self.length = sl

    def __str__(self):
        return f"{super().__str__()}, {self.length}"
    
    def area(self):
        return self.length ** 2

class Rectangle(Square):
    def __init__(self, name, outline, background, length, width):
        super().__init__(name, outline, background, length)
        self.width = width

    def __str__(self):
        return f"{super().__str__()}, {self.width}"
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, name, outline, background, v1, v2, v3):
        super().__init__(name, outline, background)
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3

    def __str__(self):
        return f"{super().__str__()}, {self.vertex1} , {self.vertex2} , {self.vertex3}"

    def area(self):
        x1, y1 = self.vertex1.x, self.vertex1.y
        x2, y2 = self.vertex2.x, self.vertex2.y
        x3, y3 = self.vertex3.x, self.vertex3.y
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    
class Circle(Shape):
    def __init__(self, name, outline, background, r):
        super().__init__(name, outline, background)
        self.radius = r

    def __str__(self):
        return f"{super().__str__()},{self.radius}"
    
    def area(self):
        return 3.14*(self.radius**2)
    
class Oval(Shape):
    def __init__(self, name, outline, background, major_radius, minor_radius):
        super().__init__(name, outline, background)
        self.major_radius = major_radius
        self.minor_radius = minor_radius

    def area(self):
        return 3.14 * self.major_radius * self.minor_radius
    
    def __str__(self):
        return f"{super().__str__()},{self.major_radius},{self.minor_radius}"
    
class Canvas:
    def __init__(self, list=[]):
        self.list=list

    def __str__(self):
        out = ""
        for i in range(len(self.list)):
            out += f"{self.list[i].name}\t\t\t{self.list[i].outline}\t\t\t{self.list[i].background}\t\t\t{self.list[i].area()}\n"
        return out
    
def main():
    print(f"Name\t\t\tOutline\t\t\tBackground\t\tArea")
    shapes = [Square("Square1",True, "White", 4), 
              Square("Square2", True, "Grey", 7),
              Rectangle("Rect1", True, "Yellow", 4, 2),
              Rectangle("Rect2", True, "Green", 6, 2),
              Circle("Circle1", False, "Yellow", 2),
              Circle("Circle2", True, "White", 4),
              Triangle("Tri1", True, "Yellow", Point(0, 0), Point(3, 4), Point(6, 0)),
              Triangle("Tri2", True, "RED", Point(0, 1), Point(2, 4), Point(7, 1)),
              Oval("Oval1", True, "Green", 5, 3),
              Oval("Oval2", True, "Orange", 4, 2) ]
    z = Canvas(shapes)
    print(z)

if __name__ == "__main__":
    main()


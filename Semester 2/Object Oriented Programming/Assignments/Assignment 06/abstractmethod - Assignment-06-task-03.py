from abc import ABC, abstractmethod
import tkinter as tk

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def draw(self, canvas):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def draw(self, canvas):
        canvas.create_oval(200, 200, 200 + 2 * self.radius, 10 + 2 * self.radius, outline="purple")
    
    def __str__(self):
        return f"{self.name} - Area: {self.area()}, Perimeter: {self.perimeter()}"

class Oval(Circle):
    def __init__(self, name, major_radius, minor_radius):
        super().__init__(name, major_radius)
        self.major_radius = major_radius
        self.minor_radius = minor_radius

    def calculate_radius(self):
        return (0.5 * self.major_radius * self.minor_radius) / ((self.major_radius**2) + (self.minor_radius**2)) ** 0.5

    def area(self):
        return 3.14 * (self.major_radius / 2) * (self.minor_radius/2)

    def perimeter(self):
        return (2 * 3.14 * (((self.major_radius**2) + (self.minor_radius**2))/2) ** 0.5)
    
    def draw(self, canvas):
        canvas.create_oval(10, 10, 10 + 2 * self.major_radius, 10 + 2 * self.minor_radius, outline="black")


    def __str__(self):
        return f'{super().__str__()}, Radius: {self.calculate_radius()}'


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def draw(self, canvas):
        canvas.create_rectangle(300, 100, 100 + self.length, 10 + self.width, outline="blue")

    def __str__(self):
        return f"{self.name} - Area: {self.area()}, Perimeter: {self.perimeter()}"


class Square(Rectangle):
    def __init__(self, name, side_length):
        super().__init__(name, side_length, side_length)

    def area(self):
        return self.length * self.length  
    
    def perimeter(self):
        return 4 * self.length  
    def draw(self, canvas):
        canvas.create_rectangle(100, 100, 100 + self.length, 100 + self.length, outline="red")

    def __str__(self):
        return f"{self.name} - Area: {self.area()}, Perimeter: {self.perimeter()}"

def main():
    root = tk.Tk()
    root.title("Shapes Drawing")

    canvas = tk.Canvas(root, width=900, height=500)
    canvas.pack()

    circle = Circle("Circle", 200)
    rect = Rectangle("Rectangle", 90, 60)
    oval = Oval("Oval", 50, 100)
    sq = Square("Square", 100)

    shapes = [circle, rect, sq, oval]

    for shape in shapes:
        shape.draw(canvas)

    root.mainloop()


if __name__ == "__main__":
    main()

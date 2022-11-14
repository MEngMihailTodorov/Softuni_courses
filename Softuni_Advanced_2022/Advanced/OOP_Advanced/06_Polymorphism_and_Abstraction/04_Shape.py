from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return self.radius * pi * self.radius

    def calculate_perimeter(self):
        return self.radius * 2 * pi


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return (self.a + self.b) * 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

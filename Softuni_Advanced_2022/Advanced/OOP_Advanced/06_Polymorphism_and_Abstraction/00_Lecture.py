# Run time polymorphism
# Compile-Time polymorphism, or method overloading is not supported in python
# If a class has multiple methods with the same name, the method defined in the last will override all earlier
# iterations of the method.


class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()


a1 = ImageArea(7, 10)
a2 = ImageArea(10, 20)
a3 = ImageArea(20, 19)

# Abstraction - a class containing abstract methods, which are methods that are declared but contain no implementation and they need child classes to provide
# that implementation for them
# We implement abstraction by importing abc - ABC, abstractmethod


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

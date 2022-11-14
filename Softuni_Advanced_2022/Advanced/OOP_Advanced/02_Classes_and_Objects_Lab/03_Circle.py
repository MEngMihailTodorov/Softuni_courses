class Circle:
    pi = 3.14

    def __init__(self, radius: float):
        self.radius = radius
        self.pi = 3.14

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return round(self.radius ** 2 * self.pi, 2)

    def get_circumference(self):
        return round(self.radius * 2 * self.pi, 2)


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

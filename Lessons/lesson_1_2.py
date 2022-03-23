 class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * Circle.pi * self.radius

    def get_area(self):
        return Circle.pi * (self.radius ** 2)


circle_1 = Circle(4)
print(circle_1.get_circumference())
print(circle_1.get_area())

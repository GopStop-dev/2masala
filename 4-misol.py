from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def yuzasi(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...


class Rectangle(Shape):
    def __init__(self, kenglik, uzunlik):
        self.kenglik = kenglik
        self.uzunlik = uzunlik

    def yuzasi(self):
        return self.kenglik * self.uzunlik

    def perimeter(self):
        return 2 * (self.kenglik + self.uzunlik)


rectangle = Rectangle(5, 3)

print(rectangle.yuzasi())
print(rectangle.perimeter())


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def yuzasi(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


circle = Circle(4)

print(circle.yuzasi())
print(circle.perimeter())


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def yuzasi(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


triangle = Triangle(3, 4, 5)

print(triangle.yuzasi())
print(triangle.perimeter())

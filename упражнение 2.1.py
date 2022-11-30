class Shape:
    def __init__(self, width = 0, length = 0):
        self.width = width
        self.length = length
    def __str__(self):
        return str(self.width) + " " + str(self.length)

class Triangle(Shape): #подразумевается прямоугольный треугольник с катетами, равными ширине и длине соответственно
    def area(self):
        return self.width * self.length * 0.5

class Rectangle(Shape):
    def area(self):
        return self.width * self.length

a = Triangle(5, 4)
b = Rectangle(5, 4)

print(a.area())
print(b.area())
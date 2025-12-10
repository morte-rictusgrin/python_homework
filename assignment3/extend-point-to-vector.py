#Task 5: Extending a Class
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y       

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        distance = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return distance
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    


p1 = Point(10, 12)
p2 = Point(1, 15)
p3 = Point(1, 15)

print(p1)
print(p2)
print(p3)
print(p1 == p2)
print(p2 == p3)
print(p1.__eq__(p3))
print(str(p2))
print(p1.distance(p3))

v1 = Vector(5, 11)
v2 = Vector(22, 3)

print(v1)
print(str(v2))
print(v1 + v2)
print(v2.distance(v1))

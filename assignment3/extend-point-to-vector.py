import math

# Task 5
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("Distance can only be calculated between Points")
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Vector(Point):

    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    # Points
    p1 = Point(2, 3)
    p2 = Point(5, 7)
    p3 = Point(2, 3)

    print(p1)  # Point(2, 3)
    print(p2)  # Point(5, 7)

    print("p1 == p2:", p1 == p2)
    print("p1 == p3:", p1 == p3)

    print("Distance between p1 and p2:", p1.distance_to(p2))

    print("\n--- Vectors ---")

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print(v1)  
    print(v2)  

    v3 = v1 + v2
    print("v1 + v2 =", v3)

    print("v1 == Vector(1,2):", v1 == Vector(1, 2))
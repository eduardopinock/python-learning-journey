
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        return math.sqrt(dx**2 + dy**2)


# Creating two objects
p1 = Point(3, 4)
p2 = Point(6, 8)

# Printing the objects
p1.display()
p2.display()

# Calculating the distance
result = p1.distance(p2)

print("Distance between points:", result)

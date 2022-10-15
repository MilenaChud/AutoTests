from src.Figure import Figure
import math


class Triangle(Figure):
    NAME = "Triangle"

    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3
        if (self.a + self.b) <= self.c or (self.a + self.c) <= self.b or (self.b + self.c) <= self.a:
            raise ValueError("The triangle not exists")
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError("The triangle not exists with negative sides")

    def area(self):
        P_2 = (self.a + self.b + self.c) / 2
        area = math.sqrt(P_2 * (P_2 - self.a) * (P_2 - self.b) * (P_2 - self.c))
        return area

    def perimeter(self):
        P = self.a + self.b + self.c
        return P


triangle = Triangle(6, 6, 6)
print(triangle.area())

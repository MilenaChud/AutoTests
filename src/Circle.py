from src.Square import Square
from src.Figure import Figure


class Circle(Figure):
    NAME = "Circle"
    PI = 3.14

    def __init__(self, radius):
        self.r = radius
        if self.r <= 0:
            raise ValueError("The value can't be 0 or less than 0 - this not circle!")
        if self.r == "":
            raise ValueError("The value can't be empty")

    def area(self):
        area = self.PI * self.r * self.r
        return area

    def perimeter(self):
        L = 2 * self.PI * self.r
        return L

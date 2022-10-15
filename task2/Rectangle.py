from src.Figure import Figure


class Rectangle(Figure):
    NAME = "Rectangle"

    def __init__(self, first_side, second_side):
        self.a = first_side
        self.b = second_side
        if self.a <= 0 or self.b <= 0:
            raise ValueError("The value can't be 0 or less than 0")
        if self.a == "" or self.b == "":
            raise ValueError("The value can't be empty")

    def area(self):
        area = self.a * self.b
        return area

    def perimeter(self):
        L = (2 * self.a) + (2 * self.b)
        return L
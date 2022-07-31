from src.Figure import Figure

class Square(Figure):
    NAME = "Square"

    def __init__(self, side):
        self.a = side
        if self.a <= 0:
            raise ValueError("The value can't be 0 or less than 0")
        if self.a == "":
            raise ValueError("The value can't be empty")

    def area(self):
        area = self.a * self.a
        return area

    def perimeter(self):
        S = 4 * self.a
        return S

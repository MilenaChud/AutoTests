class Figure:
    NAME = None

    @property
    def area(self):
        return True

    @property
    def perimeter(self):
        return True

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("The figure not exists")
        return self.area + figure.area

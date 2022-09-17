from abc import abstractmethod


class Figure:
    name = None

    @property
    def area(self):
        pass

    @property
    def perimeter(self):
        pass

    def add_area(self, figure: 'Figure'):
        return self.area() + figure.area()

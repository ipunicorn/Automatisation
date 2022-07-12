from abc import abstractmethod


class Figure:
    name = None

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure: 'Figure'):
        return self.area() + figure.area()

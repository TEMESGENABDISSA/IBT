from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


    def describe(self):

        print(
            f"I am a shape with area {self.area()}"
        )


class Circle(Shape):

    def __init__(self,radius):

        self.radius = radius


    def area(self):

        return 3.14159 * self.radius ** 2



class Rectangle(Shape):

    def __init__(self,width,height):

        self.width = width
        self.height = height


    def area(self):

        return self.width*self.height



class Triangle(Shape):

    def __init__(self,base,height):

        self.base=base
        self.height=height


    def area(self):

        return 0.5*self.base*self.height



def total_area(shapes):

    return sum(
        shape.area()
        for shape in shapes
    )
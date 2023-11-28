#%%

from abc import ABC, abstractmethod
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    
    def ispolygon(self):
        return False


class Polygon(Shape):
    def ispolygon(self):
        return True

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): 
        return self.width * self.height 

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius**2 * math.pi

# %%

r = Rectangle(3.0, 4.0)
print(r.area())

#%%
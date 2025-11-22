#!/usr/bin/env python3
"""Task 01 - Shapes and Duck Typing"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle shape with radius"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Handle negative radius: just multiply by -1
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Handle negative radius similarly
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape with width and height"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


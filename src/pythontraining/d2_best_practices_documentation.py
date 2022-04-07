"""
Demo of documentation.
1) Module level
2) Function level
3) Class level
"""


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


print(multiply.__name__)
print(multiply.__doc__)


class Rectangle:
    """A class used to represent a rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height


rectangle = Rectangle(10, 20)

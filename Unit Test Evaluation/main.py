import unittest


# Define a Rectangle class.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


# Test based on unittest  module.

class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "Incorrect area")


# Run test

unittest.main()

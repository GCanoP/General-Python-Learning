# Code to be tested.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        if area >= 0:
            return area
        else:
            return "Error"

    def set_width(self, width):
        self.width = width

    def set_height(self):
        self.height = self.height


# Test function to be executed in PyTest.
def test_normal_case():
    rectangle = Rectangle(2, 3)
    assert rectangle.get_area() == 6, "Incorrect Area."


def test_zero_case():
    rectangle = Rectangle(0, 0)
    assert rectangle.get_area() == 0, 'Zero Value'


def test_negative_case():
    rectangle = Rectangle(2, -3)
    assert rectangle.get_area() == "Error", "Error Negative Values"

"""Jose Mauricio Hernandez Jimenez"""
"""GITI9071_E"""
"""Separamos las abstraciones en dos clases de herencia diferentes """
class DrawingAPIOne(object):
    """implementation-specific abstraction: concrete classs one"""

    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} whit radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """Implementation-specific abstraction: concrete class two"""

    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} whit radius {}!)".format(x, y, radius))


class Circle(object):
    """Implementation-independent abstraction: for example, therre could be a rectangle class!"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction take care of by another class: DrawinAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self):
        """Implementation-Independent"""
        self._radius *= percent


# Build the first Circle object using API one
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# Draw a circle
circle1.draw()
# Build the second Circle object using API Two
circle2 =Circle(2, 3, 4, DrawingAPITwo())
# Draw a circle
circle2.draw()
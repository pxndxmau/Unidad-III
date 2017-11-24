"""Jose Mauricio Hernandez Jimenez"""
"""GITI9071_E"""
"""Solucion de varios elementos de existencia de la clase jer¿rarquica"""
class House(object):  # The class being visited
    def accept(self, visitor):
        """Interface to accept a visitor"""
        # Triggers the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)  # Note that we have a reference to the House object is printed

    def work_on_electricity(self, electrician):
        print(self, "worked on by",
              electrician)  # Note that we have a reference to the electricity in the house object!

    def __str__(self):
        """Simply return the class name when the house object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""

    def __str__(self):
        """Simply return the class name when the visitor object is printed"""
        return self.__class__.__name__


class HvacSpeciaList(Visitor):  # Inherits from the parent class, Visitor
    """Concrete visitor: HVAC specialist"""

    def visit(self, house):
        house.work_on_hvac(self)  # note that the visitor now has a reference to the house object


class Electrician(Visitor):  # Inherits from the parent class, Visitor
    """Concrete visitor: electrician """

    def visit(self, house):
        house.work_on_electricity(self)  # note that the visitor now has a reference to the house object


# Create an HVAC specialist
hv = HvacSpeciaList()
# Create an electrician
e = Electrician()
# Create a house
home = House()
# let´s the house accept the HVAC specialist and work on the house by invoking the visit() method
home.accept(hv)
# let´s the house accept the electrician and work on the house by invoking the visit() method
home.accept(e)

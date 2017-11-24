"""Jose Mauricio Hernandez Jimenez"""
"""GITI9071_E"""
"""Se busca por multiples objetos o por el borde de dise{o"""
class Borg:
    """Borg class making class attributes global"""
    _shared_state = {}  # Attribute dictionary

    def __init__(self, SNMP="Simple Network Management Protocol", HTTP="Hyper Text Tansfer Protocol"):
        self.__dict__ = self._shared_state  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    """This class now shared all its attributes among its various instances"""

    # This essentially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)


# let´s create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Tansfer Protocol")
# Print the object
print(x)

# Let´s create another singleton object and if it refers to the same attribute dictionary by adding other acronym
y = Singleton(SNMP="Simple Network Management Protocol")
# Print the object
print(y)

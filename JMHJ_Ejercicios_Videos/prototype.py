"""Jose Mauricio Hernandez Jimenez"""
"""GITI9071_E"""
"""Se creo el ecenario de produccion donde se cero un prototipo instantaneo"""
import copy

class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an Object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """clone a registered object and update its attribute"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object('skylark', c)

c1 = prototype.clone('skylark')
print(c1)

"""Jose Mauricio Hernandez Jimenez"""
"""GITI9071_E"""
"""Se creo strategias de clases con nuevos componentes"""
import types # Import the types module


class Strategy:
    def __init__(self, function=None):
        self.name = "Default Strategy"
        # If a reference to a fuction is provided, replace the execute() method with the given fuction

    def execute(self):  # This gets replaced by another  version if another strategy is provided.
        """The defaut method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))


# Replacement method 2
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


# Let´s create our default strategy
s0 = Strategy()
# Let´s execute our default strategy
s0.execute()
# Let´s create the first varition of default strategy by providing a new behavior
s1 = Strategy(strategy_one)
# Let´s set its name
s1.name = "Strategy one"
# Let´s execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()

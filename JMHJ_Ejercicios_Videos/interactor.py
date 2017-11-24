"""Jose Mauricio Hernandez Jimenez"""
"""GITI9071_E"""
"""se creo un esenario donde iteramos basandonos en contruccion con insolucion interfaces y recomendacion"""
def count_to(count):
    """Our iterator implementation"""
    #Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funt"]

    #Our build-in in iterator
    #creayte a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    #Iterator thouggh our iterable list
    #Extract the German numbers
    #Put them in a generator called number
    for position, number in iterator:

        #returns a 'generation' containing numbers in german
        yield number

#Let´s test the generator returned by our iterator
for num in count_to(3):
    print("{}".format(num))

for num in count_to(4):
    print("{}".format(num))


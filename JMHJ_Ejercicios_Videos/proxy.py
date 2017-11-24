"""Jose Mauricio Hernandez Jimenez"""
"""GITI9071_E"""
"""Se creo un esenario donde se produce un artista donde se responsabilisa para la creacion de recursos intensos """
import time

class Producer:
    """define the 'resource-intensive' object to instantiate"""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    """Define the 'relative less resource-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if producer is available"""
        print("Artist checking if producer is available ....")

        if self.occupied == 'No':
            # If the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)
            # Make the producer meet the guest
            self.producer.meet()

        else:
            # Otherwise, don´t instantiate a producer
            time.sleep(2)
            print("Producer is busy!")

# Instantiate proxy
p = Proxy()

# Make the proxy: Artist producer until producer is available
p.produce()

# Change the state to 'occupied'
p.occupied = 'Yes'
# Make the producer producer
p.produce()
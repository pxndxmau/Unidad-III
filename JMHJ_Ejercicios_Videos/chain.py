"""Jose Mauricio Hernandez Jimenez"""
"""GITI9071_E"""
"""creamos susesor checamos el controlador de la peticion"""
class Handler: #abstract handler
    """Abstract Handler"""
    def __init__(self, successor):
        self._successor = successor#Define who is the next hadler

    def handle(self, request):
        handled = self._handle(request)#If handled, stop here

        #otherwisi, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): #Inherits form the abstract handler
    """Concrete handler"""
    def _handle(self, request):
        if 0 < request <= 10:#Provide a condition for handling
            print("request {} handled 1".format(request))
            return True #Indicates that the request has abstract handler

class DefaultHandler(Handler):# Inherits from the abstract handler
    """Default handler"""
    def _handle(self, request):
        """If there is no handler available"""
        #no condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True # Indicates that the request has been handled

class Client: #Using handlers
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))#create handlers and use them in a sequence you want
                                                            #Note that the default handler has no successor
    def delegate(self, requests): # Send your request one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)

#create a client
c = Client()
#Create request
request = [2, 5, 30]
#Send the request
c.delegate(request)
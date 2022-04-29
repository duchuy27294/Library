from SignalGenerator.SignalStrategy.Strategy import Strategy

class SignalGenerator(object):
    def __init__(self,strategy:Strategy = None):
        self.__strategy:Strategy = strategy

    def generate(self):
        return self.__strategy.generate()

    def setStrategy(self,strategy:Strategy):
        self.__strategy = strategy
    
    def getStrategy(self):
        return self.__strategy
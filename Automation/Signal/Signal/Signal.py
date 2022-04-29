from abc import ABC,abstractmethod

class Signal(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def getValue(self):
        pass
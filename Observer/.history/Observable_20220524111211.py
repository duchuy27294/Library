from abc import ABC,abstractmethod

class Observable(ABC):
    
    @abstractmethod
    def add(self,observer):
        pass

    @abstractmethod
    def remove(self,observer):
        pass

    @abstractmethod
    def getObserver(self,index):
        pass

    @abstractmethod
    def getObservers(self):
        pass
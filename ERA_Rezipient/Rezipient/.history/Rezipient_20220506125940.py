from abc import ABC,abstractmethod

class Rezipient(ABC):
    @abstractmethod
    def getInstrument(self,index:int):
        pass

    @abstractmethod
    def getInstrumentList(self):
        pass

    @abstractmethod
    def addInstrument(self,instrument):
        pass

    @abstractmethod
    def removeInstrument(self,instrument):
        pass
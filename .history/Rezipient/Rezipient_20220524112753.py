from abc import ABC,abstractmethod
from ..Observer import Observer

class Rezipient(Observer):
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
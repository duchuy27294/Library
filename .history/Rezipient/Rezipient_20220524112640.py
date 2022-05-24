from abc import ABC,abstractmethod
try:
    from ..Observer import Observer
except (ModuleNotFoundError,ImportError):
    from Lib.Observer import Observer

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
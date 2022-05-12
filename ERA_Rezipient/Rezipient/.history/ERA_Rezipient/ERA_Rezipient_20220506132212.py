from ERA_Rezipient.ERA_Rezipient_Interface import ERA_Rezipient_Interface
from Netzteil.DCNetzteil import DCNetzteil
from typing import List

class ERA_Rezipient(ERA_Rezipient_Interface):
    def __init__(self):
        self.__netzteil:List[DCNetzteil] = []

    def getInstrument(self,index:int):
        return self.getNetzteil(index)

    def getInstrumentList(self):
        return self.getNetzteilList()

    def addInstrument(self,instrument):
        bases = instrument.__class__.__bases__
        if 'DCNetzteil' in bases:
            self.addNetzteil(instrument)

    def removeInstrument(self,instrument):
        bases = instrument.__class__.__bases__
        if 'DCNetzteil' in bases:
            self.removeNetzteil(instrument)

    def getNetzteil(self,index):
        if index < len(self.__netzteil):
            return self.__netzteil[index]

    @abstractmethod
    def getNetzteilList(self):
        pass

    @abstractmethod
    def addNetzteil(self,netzteil):
        pass

    @abstractmethod
    def removeNetzteil(self,netzteil):
        pass
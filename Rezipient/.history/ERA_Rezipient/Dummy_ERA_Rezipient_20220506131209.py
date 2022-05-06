from ERA_Rezipient import ERA_Rezipient_Interface
from Netzteil.DummyNetzteil import DummyNetzteil
from typing import List

class Dummy_ERA_Rezipient(ERA_Rezipient_Interface):
    def __init__(self):
        self.__netzteil:List[DummyNetzteil] = []

    def getInstrument(self,index:int):
        return self.getNetzteil(index)

    def getInstrumentList(self):
        return self.getNetzteilList()

    def addInstrument(self,instrument):
        if instrument.__class__.__name__ == 'DummyNetzteil':
            if instrument not in self.__netzteil:
                self.addNetzteil(instrument)

    def removeInstrument(self,instrument):
        if instrument.__class__.__name__ == 'DummyNetzteil':
            if instrument in self.__netzteil:
                self.removeNetzteil(instrument)

    @abstractmethod
    def getNetzteil(self,index):
        pass

    @abstractmethod
    def getNetzteilList(self):
        pass

    @abstractmethod
    def addNetzteil(self,netzteil):
        pass

    @abstractmethod
    def removeNetzteil(self,netzteil):
        pass

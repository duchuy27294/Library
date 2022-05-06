from ERA_Rezipient.ERA_Rezipient_Interface import ERA_Rezipient_Interface
from Netzteil.DummyNetzteil import DummyNetzteil
from typing import List

class Dummy_ERA_Rezipient(ERA_Rezipient_Interface):
    count:int = 0

    def __init__(self,name = 'Rezipient'):
        self.__name = name
        self.__netzteil:List[DummyNetzteil] = []
        self.__path = self.__name + '.csv'
        Dummy_ERA_Rezipient.count += 1

    @classmethod
    def getCount(cls):
        return Dummy_ERA_Rezipient.count

    def size(self):
        return len(self.__netzteil)

    def getInstrument(self,index:int):
        return self.getNetzteil(index)

    def getInstrumentList(self):
        return self.getNetzteilList()

    def addInstrument(self,instrument):
        if instrument.__class__.__name__ == 'DummyNetzteil':
            self.addNetzteil(instrument)

    def removeInstrument(self,instrument):
        if instrument.__class__.__name__ == 'DummyNetzteil':
            self.removeNetzteil(instrument)

    def getNetzteil(self,index):
        if (index < len(self.__netzteil)):
            return self.__netzteil[index]
        else:
            return None

    def getNetzteilList(self):
        return self.__netzteil

    def addNetzteil(self,netzteil):
        if netzteil not in self.__netzteil:
            self.__netzteil.append(netzteil)

    def removeNetzteil(self,netzteil):
        if netzteil in self.__netzteil:
            self.__netzteil.remove(netzteil)

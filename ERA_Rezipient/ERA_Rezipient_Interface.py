from Lib.Rezipient.Rezipient import Rezipient
from abc import abstractmethod

class ERA_Rezipient_Interface(Rezipient):
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
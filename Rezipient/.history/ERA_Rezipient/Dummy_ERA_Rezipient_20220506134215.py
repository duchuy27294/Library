from ERA_Rezipient.ERA_Rezipient_Interface import ERA_Rezipient_Interface
from Netzteil.DummyNetzteil import DummyNetzteil
from typing import List
import csv
import os

class Dummy_ERA_Rezipient(ERA_Rezipient_Interface):
    count:int = 0

    def __init__(self,name = 'Rezipient'):
        self.__name = name
        self.__netzteil:List[DummyNetzteil] = []
        self.__id:List[int] = []
        self.__path = os.getcwd() + '\\' + self.__name + '.csv'
        Dummy_ERA_Rezipient.count += 1

    @classmethod
    def getCount(cls):
        return Dummy_ERA_Rezipient.count

    def size(self):
        return len(self.__netzteil)

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def getPath(self):
        return self.__path

    def setPath(self,path):
        if path.endswith('.csv'):
            self.__path = path

    def autoId(self):
        for i in range(1,len(self.__id)+1,1):
            if i not in self.__id:
                return i
        return len(self.__id)+1

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
            self.__id.append(self.autoId())

    def removeNetzteil(self,netzteil):
        if netzteil in self.__netzteil:
            self.__netzteil.remove(netzteil)

    def write(self):
        with open(self.__path,'w',newline = '') as data:
            header = ['ID',]
            write = csv.DictWriter(data,dele)

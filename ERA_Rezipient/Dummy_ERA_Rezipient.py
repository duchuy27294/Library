try:
    from .ERA_Rezipient_Interface import ERA_Rezipient_Interface
except (ModuleNotFoundError,ImportError):
    from ERA_Rezipient_Interface import ERA_Rezipient_Interface
from ..Netzteil.DummyNetzteil import DummyNetzteil
from ..Netzteil.DummyNetzteil import Tdk
from ..Netzteil.DummyNetzteil import Syskon
from typing import List
import csv
import os

class Dummy_ERA_Rezipient(ERA_Rezipient_Interface):
    def __init__(self,name = 'Rezipient'):
        self.__name = name
        self.__netzteil:List[DummyNetzteil] = []
        self.__id:List[int] = []
        self.__path = os.getcwd() + '\\' + self.__name + '.csv'

    def count(self):
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
            self.write()

    def removeNetzteil(self,netzteil):
        if netzteil in self.__netzteil:
            index = self.__netzteil.index(netzteil)
            self.__netzteil.remove(netzteil)
            self.__id.pop(index)
            self.write()

    def write(self):
        with open(self.__path,'w',newline = '') as data:
            header = ['ID','Name','Type','PrivateID']
            write = csv.DictWriter(data,delimiter = ';',fieldnames = header)
            write.writeheader()
            for i in range (0,len(self.__netzteil),1):
                info = {
                    'ID':str(self.__id[i]),
                    'Name':self.__netzteil[i].get_name(),
                    'Type':self.__netzteil[i].__class__.__name__,
                    'PrivateID':self.__netzteil[i].get_private_id()
                }
                write.writerow(info)
            data.close()

    def load(self):
        self.__id.clear()
        self.__netzteil.clear()
        with open(self.__path,'r',newline = '') as data:
            read = csv.reader(data,delimiter = ';')
            i = 0
            for line in read:
                if i != 0:
                    id = int(line[0])
                    name = line[1]
                    type = line[2]
                    if type.lower() == 'tdk':
                        netzteil = Tdk(name = name)
                    elif type.lower() == 'syskon':
                        netzteil = Syskon(name = name)
                    else:
                        netzteil = DummyNetzteil(name = name)
                    self.__netzteil.append(netzteil)
                    self.__id.append(id)
            data.close()

    def update(self,netzteil):
        if (netzteil in self.__netzteil):
            if ( (netzteil.get_voltage() - netzteil.measure_voltage()) >= 0.2 ):
                print("Fehler: Spannungsabweichung zu gross")
            elif (netzteil.measure_voltage() > netzteil.get_voltage()):
                print("Fehler: Istspannung groesser als Sollspannung")
            if ( (netzteil.get_current() - netzteil.measure_current()) >= 0.2 ):
                print("Fehler: Stromabweichung zu gross")
            elif (netzteil.measure_current() > netzteil.get_current()):
                print("Fehler: Iststrom groesser als Sollstrom")


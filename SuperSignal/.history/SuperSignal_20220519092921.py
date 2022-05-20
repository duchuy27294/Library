from ..MathSignal import MathSignal
from typing import List

class SuperSignal():
    def __init__(self,signalList:List[MathSignal] = []):
        self.__signalList = signalList

    def count(self):
        return len(self.__signalList)

    def getSignal(self,index:int):
        try:
            return self.__signalList[index]
        except IndexError:
            return None
    
    def getSignalList(self):
        return self.__signalList

    def addSignal(self,signal):
        if signal not in self.__signalList:
            self.__signalList.append(signal)

    def removeSignal(self,signal):
        if signal in self.__signalList:
            self.__signalList.remove(signal)
from Event import Event
from MathSignal import MathSignal
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
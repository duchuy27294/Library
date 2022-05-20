from MathSignal import *
from typing import List

class SuperSignal(MathSignal):
    def __init__(self):
        self.__signal:List[MathSignal] = []
    
    def getValue(self,time:float):
        pass

    def getDuration(self)->float:
        duration = 0
        for sig in self.__signal:
            duration += sig.getDuration()
        return duration

    def getSignal(self,index):
        try:
            return self.__signal[index]
        except IndexError:
            return None
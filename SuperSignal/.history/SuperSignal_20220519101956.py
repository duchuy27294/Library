from MathSignal import *
from typing import List

class SuperSignal(MathSignal):
    def __init__(self):
        self.__signal:List[MathSignal] = []

    def count(self):
        return len(self.__signal)
    
    def getValue(self,time:float):
        if (time <= 0):
            raise InvalidTime
        else:
            if (time > self.getDuration()):
                raise TimeGreaterThanDuration
            else:
                duration = 0
                for sig in self.__signal:
                    if (time >= duration) and (time < (duration + sig.getDuration())):
                        return sig.getValue()
                    else:
                        duration += sig.getDuration()
                return None

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
try:
    from ..MathSignal import *
except (ModuleNotFoundError,ImportError):
    from MathSignal import *
from typing import List
import numpy as np

class SignalAlreadyExist(Exception):
    def __init__(self):
        self.message = 'Signal already exists in this Super Signal'
        super().__init__(self.message)

class SignalNotExist(Exception):
    def __init__(self):
        self.message = 'Signal does not exist in this Super Signal'
        super().__init__(self.message)

class SuperSignal(MathSignal):
    def __init__(self):
        self.__signal:List[MathSignal] = []

    def count(self):
        return len(self.__signal)
    
    def getValue(self,time:float):
        if (time < 0):
            raise InvalidTime
        else:
            if (time > self.getDuration()):
                raise TimeGreaterThanDuration(time,self.getDuration())
            else:
                duration = 0
                for sig in self.__signal:
                    if (time >= duration) and (time < (duration + sig.getDuration())):
                        return sig.getValue(time - duration)
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

    def add(self,signal:MathSignal):
        if signal not in self.__signal:
            self.__signal.append(signal)
        else:
            raise SignalAlreadyExist

    def remove(self,signal:MathSignal):
        if signal in self.__signal:
            self.__signal.remove(signal)
        else:
            raise SignalNotExist

    def getSignalList(self):
        return self.__signal

    def isEmpty(self):
        if (len(self.__signal) == 0):
            return True
        else:
            return False

    def generate(self):
        duration = self.__signal.getDuration()
        t = np.arange(0,duration,0.1,dtype = float)
        y = []
        for i in t:
            y.append(self.__signal.getValue(i))
        constantSignalList = []
        tempDuration = 0.0
        tempValue = 0.0
        for i in range (0,len(y),1):
            if (i==0):
                tempValue = y[i]
                tempDuration = 0
            else:
                if (y[i] != y[i-1]):
                    constantSignal = ConstantSignal(duration = tempDuration,value = tempValue)
                    constantSignalList.append(constantSignal)
                    tempDuration = 0
                    tempValue = y[i]
                else:
                    tempDuration += 0.1
        return constantSignalList
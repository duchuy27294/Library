try:
    from .SuperSignal import *
    from ..MathSignal import *
except (ModuleNotFoundError,ImportError):
    from SuperSignal import *
    from MathSignal import *
from typing import List
import numpy as np

class Builder(object):
    def __init__(self,signal:SuperSignal = None):
        self.__signal = signal

    def add(self,signal:MathSignal):
        try:
            self.__signal.add(signal)
        except SignalAlreadyExist:
            pass
        return self

    def remove(self,signal:MathSignal):
        try:
            self.__signal.remove(signal)
        except SignalNotExist:
            pass
        return self
    
    def getSignal(self):
        return self.__signal

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
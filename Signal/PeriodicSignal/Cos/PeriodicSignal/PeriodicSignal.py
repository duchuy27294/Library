from abc import abstractmethod
from Signal.Signal import Signal
from Signal.Event import Event
from typing import List

class PeriodicSignal(Signal):
    def __init__(self,duration:float = 0.1,xOffset:float = 0.0,yOffset:float = 0.0):
        self.__duration = duration
        self.__xOffset = xOffset
        self.__yOffset = yOffset

    def getDuration(self):
        return self.__duration

    def setDuration(self,duration:float):
        if duration >= 0.1:
            self.__duration = duration

    def getXOffset(self):
        return self.__xOffset

    def setXOffset(self,xOffset:float):
        self.__xOffset = xOffset

    def getYOffset(self):
        return self.__yOffset

    def setYOffset(self,yOffset:float):
        self.__yOffset = yOffset

    @abstractmethod
    def getValue(self,time:float):
        pass

    @abstractmethod
    def generate(self)->List[Event]:
        pass
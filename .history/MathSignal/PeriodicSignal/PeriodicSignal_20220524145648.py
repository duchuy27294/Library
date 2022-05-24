from abc import abstractmethod
from ..MathSignal import MathSignal
from typing import List

class PeriodicSignal(MathSignal):
    def __init__(self,duration:float = 0.1,xOffset:float = 0.0,yOffset:float = 0.0):
        self.__duration = duration
        self.__xOffset = xOffset
        self.__yOffset = yOffset

    def getDuration(self):
        return self.__duration

    def setDuration(self,duration:float):
        pass

    @abstractmethod
    def getValue(self,time:float):
        pass

    def getXOffset(self):
        return self.__xOffset

    def setXOffset(self,xOffset:float):
        self.__xOffset = xOffset

    def getYOffset(self):
        return self.__yOffset

    def setYOffset(self,yOffset:float):
        self.__yOffset = yOffset

    @abstractmethod
    def generate(self):
        pass
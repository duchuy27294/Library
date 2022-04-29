from SignalGenerator.SignalStrategy.Strategy import Strategy
import math
import numpy as np

class PeriodicSignal(Strategy):
    def __init__(self,duration: float = 0.2, xOffset = 0, yOffset = 0, amplitude = 1, step = 0.1):
        self.__duration = duration
        self.__xOffset = xOffset
        self.__yOffset = yOffset
        self.__amplitude = amplitude
        self.__step = step

    def getDuration(self):
        return self.__duration

    def setDuration(self,duration:float):
        if (duration >= 0.1):
            self.__duration = duration

    def getStep(self):
        return self.__step

    def setStep(self,step:float):
        if (step > 0) and (step < self.__duration):
            self.__step = step

    def getValue(self,time:float):
        pass

    def getXOffset(self):
        return self.__xOffset

    def setXOffset(self,offset:float):
        self.__xOffset = offset

    def getYOffset(self):
        return self.__yOffset

    def setYOffset(self,offset:float):
        self.__yOffset = offset

    def getAmplitude(self):
        return self.__amplitude

    def setAmplitude(self,amplitude):
        self.__amplitude = amplitude

    def generate(self):
        pass
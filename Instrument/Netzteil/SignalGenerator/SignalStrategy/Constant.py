from Strategy import Strategy
import numpy as np

class Constant(Strategy):
    def __init__(self,duration:float = 0.2,value:float = 0.0):
        self.__duration = duration
        self.__value = value

    def getDuration(self):
        return self.__duration

    def setDuration(self,duration:float):
        if (duration >= 0.1):
            self.__duration = duration

    def getValue(self):
        return self.__value

    def setValue(self,value:float):
        self.__value = value

    def generate(self):
        x = np.arange(0,self.__duration,0.1,dtype = float)
        y = []
        for i in x:
            y.append(self.__value)
        return x,y
try:
    from .MathSignal import *
except (ModuleNotFoundError,ImportError):
    from MathSignal import *

class ConstantSignal(MathSignal):
    def __init__(self,duration:float = 0.1,value:float = 0.0):
        self.__duration = duration
        self.__value = value

    def getValue(self,time):
        if (time <= self.__duration):
            return self.__value
        else:
            raise TimeGreaterThanDuration(time,self.getDuration())

    def getDuration(self):
        return self.__duration

    def setDuration(self,duration:float):
        if (duration <= 0):
            raise DurationZero
        else:
            self.__duration = duration
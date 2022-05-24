try:
    from .MathSignal import *
except (ModuleNotFoundError,ImportError):
    from MathSignal import *

class ConstantSignal(MathSignal):
    def __init__(self,duration = 0.1, value = 0.0):
        self.__duration = duration
        self.__value = value
        
    def getValue(self,time:float):
        try:
            if (time < 0):
                raise InvalidTime
            elif (time > self.__duration):
                raise TimeGreaterThanDuration(time,self.__duration)
            else:
                return self.__value
        except (InvalidTime,TimeGreaterThanDuration):
            return None

    @abstractmethod
    def getDuration(self)->float:
        pass

    @abstractmethod
    def generate(self):
        pass
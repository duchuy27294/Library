try:
    from .MathSignal import *
except (ModuleNotFoundError,ImportError):
    from MathSignal import *

class ConstantSignal(MathSignal):
    def __init__(self,duration = 0.1, value = 0.0):
        self.__duration = duration
        self.__value = value
        
    def getValue(self,time = None):
        try:
            if (time is not None):
                if (time < 0):
                    raise InvalidTime
                elif (time > self.__duration):
                    raise TimeGreaterThanDuration(time,self.__duration)
                else:
                    return self.__value
            else:
                return self.__value
        except (InvalidTime,TimeGreaterThanDuration):
            return None

    def getDuration(self)->float:
        return self.__duration
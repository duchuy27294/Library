try:
    from .MathSignal import MathSignal
except (ModuleNotFoundError,ImportError):
    from MathSignal import MathSignal

class ConstantSignal(MathSignal):
    def __init__(self,duration = 0.1, value = 0.0):
        self.__duration = duration
        self.__value = value
        
    def getValue(self,time:float):
        try:
            if (time < self.__duration):

    @abstractmethod
    def getDuration(self)->float:
        pass

    @abstractmethod
    def generate(self):
        pass
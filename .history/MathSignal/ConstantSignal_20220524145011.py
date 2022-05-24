try:
    from .MathSignal import MathSignal
except (ModuleNotFoundError,ImportError):
    from MathSignal import MathSignal
from typing import List

class ConstantmSignal(MathSignal):
    def __init__(self,eventList = None):
        if eventList is None:
            self.__event = []
        else:
            self.__event = eventList

    @abstractmethod
    def getValue(self,time:float):
        pass

    @abstractmethod
    def getDuration(self)->float:
        pass

    @abstractmethod
    def generate(self):
        pass
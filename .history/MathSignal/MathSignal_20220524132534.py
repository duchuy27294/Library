from abc import ABC,abstractmethod

class InvalidTime(Exception):
    def __init__(self):
        self.message = "Time moment must be greater than or equal to 0 "

class MathSignal(ABC):

    @abstractmethod
    def getValue(self,time:float):
        pass

    @abstractmethod
    def getDuration(self)->float:
        pass

    @abstractmethod
    def generate(self):
        pass
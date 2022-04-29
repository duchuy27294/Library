from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def getDuration(self):
        pass

    @abstractmethod
    def setDuration(self,duration:float):
        pass

    @abstractmethod
    def generate(self):
        pass
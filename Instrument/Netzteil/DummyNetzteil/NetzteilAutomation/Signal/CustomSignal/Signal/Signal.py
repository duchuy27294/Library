from abc import ABC,abstractmethod
from Event import Event

class Signal(ABC):

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def getValue(self,time:float):
        pass

    @abstractmethod
    def duration(self)->float:
        pass
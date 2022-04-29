from abc import ABC,abstractmethod
from Event import Event
from typing import List

class Signal(ABC):
    
    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def getValue(self,time:float):
        pass

    @abstractmethod
    def getDuration(self)->float:
        pass

    @abstractmethod
    def generate(self)->List[Event]:
        pass
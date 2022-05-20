from abc import ABC,abstractmethod

class DurationZero(Exception):
    def __init__(self):
        self.message = 'Duration must be greater than 0'
        super().__init__(self.message)

class MathSignal(ABC):

    @abstractmethod
    def getValue(self,time:float):
        pass

    @abstractmethod
    def getDuration(self)->float:
        pass

    # @abstractmethod
    # def generate(self):
    #     pass
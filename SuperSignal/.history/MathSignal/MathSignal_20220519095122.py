from abc import ABC,abstractmethod

class DurationZero(Exception):
    def __init__(self):
        self.message = 'Duration must be greater than 0'
        super().__init__(self.message)

class TimeGreaterThanDuration(Exception):
    def __init__(self,time,duration):
        self.message = 'Moment ' + str(time) + 's out of signal duration (' + str(duration) + 's)'
        super().__init__(self.message)

class MathSignal(ABC):

    @abstractmethod
    def getValue(self,time:float):
        pass

    @abstractmethod
    def getDuration(self)->float:
        pass

    @abstractmethod
    def setDuration(self,duration:float):
        pass

    # @abstractmethod
    # def generate(self):
    #     pass
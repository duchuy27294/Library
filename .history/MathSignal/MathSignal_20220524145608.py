from abc import ABC,abstractmethod

class InvalidTime(Exception):
    def __init__(self):
        self.message = "Time moment must be greater than or equal to 0 "
        super().__init__(self.message)

class TimeGreaterThanDuration(Exception):
    def __init__(self,time,duration):
        self.message = "Time moment " + str(time) + "s out of duration (" + str(duration) + "s)"
        super().__init__(self.message)

class MathSignal(ABC):

    @abstractmethod
    def getValue(self,time:float):
        pass

    @abstractmethod
    def getDuration(self)->float:
        pass

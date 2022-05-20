try:
    from ..MathSignal import *
    from .PeriodicSignal import PeriodicSignal
except (ModuleNotFoundError,ImportError):
    from MathSignal import *
    from PeriodicSignal import PeriodicSignal
import math

class Cos(PeriodicSignal):
    def __init__(self,duration:float = 0.1, xOffset:float = 0.0, yOffset:float = 0.0):
        super().__init__(duration = duration, xOffset = xOffset,yOffset = yOffset)

    def getValue(self,time):
        if (time < self.getDuration()):
            return math.cos(time-self.getXOffset()) + self.getYOffset()
        else:
            raise TimeGreaterThanDuration(time,self.getDuration())
